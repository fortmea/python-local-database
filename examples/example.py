from pylocaldatabase import pylocaldatabase

dbcontroll = pylocaldatabase.databasecontroller(path="file.json", isEncrypted=False)

# trying to load file. if unable, creates the file.
try:
    dbcontroll.load()
except:
    dbcontroll.makeDatabase()

# assigning document to a var. if not found, creates one.
document = dbcontroll.getDocument("test")
if(document == False):
    dbcontroll.insertDocument({}, "test")
    # assigning again, now with an instance of pylocaldatabase.databaseDocument instead of the boolean False return when the document was not found.
    document = dbcontroll.getDocument("test")

print(document.get())  # printing it's contents

# inserting item of name "Color" with value "Deep purple", basically this json structure: {"Color" : "Deep purple"}
document.insertItem("Color", "Deep purple")

print(document.get())  # printing document contents again

# inserting new item, this time with this JSON structure: {"Item1": {"Property": "Value"}}
document.insertItem("Item1", {"Property": "Value"})

print(document.get())  # printing document contents again

document.removeItem("Color")  # removing item of name "Color"

print(document.getItem('Item1').get())  # printing the contents of item "Item1"

print(document.getHash())  # printing the document's hash

document.insertItem("NewItem", {})  # inserting new item

item1 = document.getItem("NewItem")  # assigning it to variable item1

print(item1.hash())  # printing it's hash


item1.insertProperty("user_name", "João Walter Amadeu") # inserting new property in item1

print(item1.get()["user_name"])  # printing value of the property "user_name"

item1.removeProperty("user_name") # removing property "user_name"

document.removeItem("Item1") # removing item from document

dbcontroll.save()  # saving the operations on the file

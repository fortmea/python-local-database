from pylocaldatabase import pylocaldatabase

#creating our instance of databasecontroller, specifying a file name for our data storage
dbcontroll = pylocaldatabase.databasecontroller("nfile.edb", True)

# specify key path 
keypath = "key.key"
# (you might wanna use dbcontroll.generateKey(keypath) to generate one, if one doesn't exist already. But be careful, you don't wanna overwrite your keys.)

try:
    dbcontroll.decryptLoad(keyPath=keypath)
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

print(document.getItem("Color").get())

#saving the contents in a encrypted file
dbcontroll.save_encrypted(keypath)

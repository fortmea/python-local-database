import databasecontroller

dbcontroll = databasecontroller.databasecontroller(caminho="arquivo.json")
# try:
dbcontroll.load()
document = dbcontroll.getDocument("Teste2")
print(document.get())
document.insertProperty("Camisa", "Azul")
#document.remove("Cafe")
print(document.get()['Cafe'])
print(document.getHash())
dbcontroll.save()
# except:
# dbcontroll.makeDatabase()

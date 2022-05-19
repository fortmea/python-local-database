import databasecontroller

dbcontroll = databasecontroller.databasecontroller(caminho="arquivo.json")
# try:
dbcontroll.load()
document = dbcontroll.getDocument("Teste2")
document.remove("Cafe")
print(document.get()['Suco'])
# dbcontroll.save()
# except:
# dbcontroll.makeDatabase()

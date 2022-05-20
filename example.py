from random import randint
import databasecontroller

dbcontroll = databasecontroller.databasecontroller(caminho="arquivo.json")
# try:
dbcontroll.load()
document = dbcontroll.getDocument("Teste")
print(document.get())
document.insertProperty("Camisa", "Preta")
# document.remove("Cafe")
print(document.getItem('Propriedade'))
print(document.getHash())
print(document.containsValue("Valor"))
dbcontroll.save()
# except:
# dbcontroll.makeDatabase()

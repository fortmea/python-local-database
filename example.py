from random import randint
import databasecontroller

dbcontroll = databasecontroller.databasecontroller(caminho="arquivo.json")
# try:
dbcontroll.load()
document = dbcontroll.getDocument("Teste")
print(document.get())
document.insertItem("Camisa", "Preta")
#document.insertItem("Item1", {"Propriedade": "Valor"})
# document.remove("Cafe")
print(document.get())
print(document.getItem('Propriedade'))
print(document.getHash())
#print(document.containsValue("Valor"))
document.insertItem(
    "NovoDocumento", databasecontroller.item({}, "NovoDocumento"))
print(type(document.get().get("NovoDocumento")))
documento2 = document.get().get("NovoDocumento")
documento2.setData({"Cuzinho": "Daora"})
dbcontroll.save()
# except:
# dbcontroll.makeDatabase()

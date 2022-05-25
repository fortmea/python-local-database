import databasecontroller
dbcontroll = databasecontroller.databasecontroller(caminho="arquivo3.json")
try:
    dbcontroll.load()
except:
    dbcontroll.makeDatabase()

#dbcontroll.insertDocument({}, "Obj1")
documento = dbcontroll.getDocument("Obj1")
documento.insertItem("Obj4", {"Cor":input("Informe uma cor: ")})
print(documento.getItem("Obj4").get())

dbcontroll.save()
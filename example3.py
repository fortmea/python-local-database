import databasecontroller
dbcontroll = databasecontroller.databasecontroller(caminho="arquivo3.json")
try:
    dbcontroll.load()
except:
    dbcontroll.makeDatabase()

dbcontroll.insertDocument({}, "Obj1")
documento = dbcontroll.getDocument("Obj1")
documento.insertItem("Obj2", {"Cor":"Azul"})
print(documento.getItem("Obj2").get())

dbcontroll.save()
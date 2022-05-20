import databasecontroller
import shortuuid
dbcontroll = databasecontroller.databasecontroller(caminho="arquivo2.json")
try:
    dbcontroll.load()
except:
    dbcontroll.makeDatabase()
if dbcontroll.getWhere("email", "joao.amadeu@unifio.edu.br") and (dbcontroll.getWhere("senha", "blablabla")):
    print("Logado com sucesso!")
else:
    print("Credênciais incorretas!")
    exit()
    uuid = shortuuid.uuid()
    dbcontroll.insertDocument({"nome": "João Walter Amadeu",
                               "email": "joao.amadeu@unifio.edu.br", "senha": "blablabla", "status": "0"}, uuid)
    print(dbcontroll.getDocument(uuid).get())
    dbcontroll.save()

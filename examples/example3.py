from pydoc import doc
from pylocaldatabase import pylocaldatabase

dbcontroll = pylocaldatabase.databasecontroller(path="file.json", isEncrypted=False)

# trying to load file. if unable, creates the file.
try:
    dbcontroll.load()
except:
    dbcontroll.makeDatabase()

dbcontroll.insertDocument(content={"iduseridk":{"Name":"João", "Email": "joao.amadeu@unifio.edu.br"}}, name="Documento")
documento = dbcontroll.getDocument("Documento")
print(documento.containsValue("joao.amadeu@unifio.edu.br"))
print(documento.containsKey("Name"))
dbcontroll.save()
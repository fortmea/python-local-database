from pydoc import doc
from pylocaldatabase import pylocaldatabase

dbcontroll = pylocaldatabase.databasecontroller(path="file.json", isEncrypted=False)
pylocaldatabase.logo()
# trying to load file. if unable, creates the file.
try:
    dbcontroll.load()
except:
    dbcontroll.makeDatabase()


# creates document if not present
if(dbcontroll.documentExists("Documento")!=True):
    dbcontroll.insertDocument(content={"iduseridk":{"Name":"João", "Email": "joao.amadeu@unifio.edu.br"}}, name="Documento")

# added on 1.2.0: getDocuments() method return all docs in database
documentos = dbcontroll.getDocuments()
print(len(documentos))

for documento in documentos:
    print(documento)
    doc = documentos[documento].get()
    for item in doc:
        print(doc[item].get())



dbcontroll.save()
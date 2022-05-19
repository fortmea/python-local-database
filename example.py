import databasecontroller

dbcontroll = databasecontroller.databasecontroller(caminho="arquivo.json")
#try:
dbcontroll.load()
dbcontroll.save()
#except:
    #dbcontroll.makeDatabase()
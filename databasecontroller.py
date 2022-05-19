
import json


class databaseDocument:
    __name = ""
    __data = {}

    def __init__(self, data, name):
        self.__data = data
        self.__name = name

    def getName(self):
        return self.__name

    def set(self, property, data):
        self.__data[property] = data

    def remove(self, property):
        self.__data.pop(property)

    def get(self):
        return self.__data

    class item(super):
        def hash():
            # Todo: Implement hash function
            return 0


class databasecontroller:
    from databasecontroller import databaseDocument
    __path = ""
    __docs = {}

    def __init__(self, caminho):
        self.__path = caminho

    def makeDatabase(self):
        fs = open(self.__path, "w+")
        fs.close()

    def generateDocuments(self, data):
        for x in data:
            self.__docs[x] = databaseDocument(data[x], x)

    def load(self):
        try:
            fs = open(self.__path)
            data = json.loads(fs.read())
            fs.close()
            print("Arquivo carregado com sucesso!")
            # print(self.__data)
            if(data):
                self.generateDocuments(data)
            for x in self.__docs:
                print(self.__docs[x].getName())
        except:
            raise Exception(
                "Arquivo não encontrado ou corrompido-> "+self.__path)

    def save(self):
        #print(self.__docs)
        try:
            fs = open(self.__path, "w+")
            fs.write('{')
            for x in self.__docs:
                #print(x)
                #print(self.__docs[x])
                fs.write('"'+x+'":"'+self.__docs[x].get()+'"')
            fs.write('}')
            fs.close()
        except:
            raise Exception("Arquivo não encontrado -> "+self.__path)

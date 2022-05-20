
import json
import hashlib


class item():
    __data = {}
    __name = ""

    def getName(self):
        return self.__name

    def get(self):
        return self.__data

    def __init__(self, data, name):
        self.__data = data
        self.__name = name

    def hash():
        # Todo: Implement hash function
        return 0


class databaseDocument:
    __name = ""
    __data = {}

    def __getWritable__(self):
        writable = ''
        for x in self.__data:
            writable += self.__data

    def __init__(self, data, name):
        self.__data = data
        self.__name = name

    def insertItem(self, name, data):
        self.__data[name] = item(data, name)

    def insertProperty(self, name, data):
        self.__data[name] = data

    def getName(self):
        return self.__name

    def set(self, property, data):
        self.__data[property] = data

    def remove(self, property):
        self.__data.pop(property)

    def get(self):
        return self.__data

    def getHash(self):
        return hashlib.md5((str(self.getName()+str(self.get()))).encode('utf-8')).hexdigest()


class databasecontroller:
    __path = ""
    __docs = {}

    def getDocument(self, name):
        return self.__docs[name]

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
            if(data):
                self.generateDocuments(data)
        except:
            raise Exception(
                "Arquivo não encontrado ou corrompido-> "+self.__path)

    def save(self):
        try:
            pos = 1
            fs = open(self.__path, "w+")
            fs.write('{')
            for x in self.__docs:
                if(pos != len(self.__docs.keys())):
                    fs.write('"'+x+'":'+json.dumps(self.__docs[x].get())+',')
                else:
                    fs.write('"'+x+'":'+json.dumps(self.__docs[x].get()))
                pos += 1
            fs.write('}')
            fs.close()
        except:
            raise Exception("Arquivo não encontrado -> "+self.__path)

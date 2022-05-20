
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
        return 0


class databaseDocument:
    __name = ""
    __data = {}

    def __dictKeysToList__(self, dict):
        _lista = []
        for x in dict:
            _lista.append(x)
        _lista.sort()
        return _lista

    def __dictToList__(self, dict):
        _lista = []
        for x in dict:
            _lista.append(dict[x])
        _lista.sort()
        return _lista

    def binarySearch(self, vetor, valor):
        meio = vetor[len(vetor)//2]
        try:
            if meio == valor:
                return 1
            elif valor < meio:
                return self.binarySearch(vetor[:len(vetor)//2], valor)
            elif valor > meio:
                return self.binarySearch(vetor[len(vetor)//2:], valor)
        except:
            return 0

    def __doKeyBinarySearch__(self, value):
        return 0 != self.binarySearch(self.__dictKeysToList__(self.__data), value)

    def __doValueBinarySearch__(self, value):
        return 0 != self.binarySearch(self.__dictToList__(self.__data), value)

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

    def containsKey(self, name):
        return self.__doKeyBinarySearch__(name)

    def containsValue(self, name):
        return self.__doValueBinarySearch__(name)

    def set(self, property, data):
        self.__data[property] = data

    def remove(self, property):
        self.__data.pop(property)

    def get(self):
        return self.__data

    def getItem(self, name):
        return self.__data[name]

    def getHash(self):
        return hashlib.md5((str(self.getName()+str(self.get()))).encode('utf-8')).hexdigest()


class databasecontroller:
    __path = ""
    __docs = {}

    def getDocument(self, name) -> databaseDocument:
        return self.__docs[name]

    def __init__(self, caminho):
        self.__path = caminho

    def makeDatabase(self):
        fs = open(self.__path, "w+")
        fs.close()

    def generateDocuments(self, data):
        for x in data:
            self.__docs[x] = databaseDocument(data[x], x)

    def insertDocument(self, content, name):
        self.__docs[name] = databaseDocument(content, name)

    def getWhere(self, field, value) -> databaseDocument:
        try:
            for x in self.__docs:
                if(self.__docs[x].get()[field] == value):
                    return self.__docs[x]
        except:
            print("boy")

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

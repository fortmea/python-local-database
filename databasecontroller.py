
import json
import hashlib


class item():
    __data = {}
    __name = ""

    def getName(self):
        return self.__name

    def get(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def __init__(self, data, name):
        self.__data = data
        self.__name = name

    def hash():
        return 0


class databaseDocument(object):

    def __dictKeysToList__(self, dict):
        _lista = []
        for x in dict:
            _lista.append(x)
        _lista.sort()
        return _lista

    def __dictToList__(self, dict):
        _lista = []
        for x in dict:
            if(type(dict[x]) == str):
                _lista.append(dict[x].getName())
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
        if(len(self.__data) > 1):
            return 0 != self.binarySearch(self.__dictKeysToList__(self.__data), value)
        else:
            print("A document must be bigger than 1 item to be searchable.")

    def __doValueBinarySearch__(self, value):
        if(len(self.__data) > 1):
            return 0 != self.binarySearch(self.__dictToList__(self.__data), value)
        else:
            print("A document must be bigger than 1 item to be searchable.")

    def __init__(self, data, name):
        self.__data = data
        self.__name = name

    def insertItem(self, name: str, data: dict):
        self.__data[name] = item(data, name)

    def insertProperty(self, name, data):
        self.__data[name] = data

    def getName(self):
        return self.__name

    def containsKey(self, name) -> bool:
        return self.__doKeyBinarySearch__(name)

    def containsValue(self, name) -> bool:
        """Return true if a string is found in any of the documents."""
        return self.__doValueBinarySearch__(name)

    def set(self, property, data):
        self.__data[property] = data

    def remove(self, property):
        self.__data.pop(property)

    def get(self) -> dict:
        return self.__data

    def getItem(self, name) -> item:
        try:
            return self.__data[name]
        except:
            return item({"Err": True}, "Err")

    def getHash(self) -> hashlib.md5:
        return hashlib.md5((str(json.dumps(self.get(), default=databasecontroller.serialize))).encode('utf-8')).hexdigest()


class databasecontroller:
    __path = ""
    __docs = {}

    def serialize(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, databaseDocument):
            serial = obj.get()
            return serial

        if isinstance(obj, item):
            serial = obj.get()
            return serial

        return obj.__dict__

    def getDocument(self, name) -> databaseDocument:
        try:
            return self.__docs[name]
        except:
            return False

    def __init__(self, caminho):
        self.__path = caminho

    def makeDatabase(self):
        fs = open(self.__path, "w+")
        fs.close()

    def generateDocuments(self, data):
        for x in data:
            self.__docs[x] = databaseDocument({}, x)
            try:
                for y in x:
                    x.insertItem(y, x[y])
            except:
                pass

    def insertDocument(self, content, name):
        self.__docs[name] = databaseDocument(content, name)

    def getWhere(self, field, value) -> databaseDocument:
        try:
            for x in self.__docs:
                if(self.__docs[x].get()[field] == value):
                    return self.__docs[x]
        except:
            return False

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
                data = self.__docs[x]
                if(pos != len(self.__docs.keys())):
                    fs.write(
                        '"'+x+'":'+json.dumps(data, default=databasecontroller.serialize)+',')
                else:
                    fs.write(
                        '"'+x+'":'+json.dumps(data, default=databasecontroller.serialize))
                pos += 1
            fs.write('}')
            fs.close()
        except:
            raise Exception("Erro salvando arquivo -> "+self.__path)
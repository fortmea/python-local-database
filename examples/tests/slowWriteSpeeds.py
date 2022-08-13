from datetime import datetime
from pylocaldatabase import pylocaldatabase
import tracemalloc
def main():
    print("Executing write speed tests")
    init = datetime.now()
    tracemalloc.start()
    #implementation of a slow, but more memory efficient way of writing data
    for x in range(0,10000):
        dbcontroll =  pylocaldatabase.databasecontroller(path="writespeeds.json", isEncrypted=False)
        dbcontroll.load()
        doc = dbcontroll.getDocument('testdoc')
        doc.insertItem(x, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        dbcontroll.save()
        current, peak = tracemalloc.get_traced_memory()
        if(x % 1000 == 0): print(str(x)+" -> "+ str(datetime.now()) + "MEM: "+ "Current memory usage is "+ str(current/ 10**6)+"MB" + " Peak usage: " +str(peak/ 10**6))
        del dbcontroll
        
    end = datetime.now();
    print(init)
    print(end)

main()
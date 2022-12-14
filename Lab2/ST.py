from HashTable import HashTable

class SymbolTable:
    def __init__(self, size):
        self.__size = size
        self.__simtable = HashTable(size)

    def addSymTable(self, identifier):
        return self.__simtable.add(identifier)

    def hasIdentifier(self, key):
        return self.__simtable.get(key)

    def deleteIdentifier(self, key):
        return self.__simtable.delete(key)

    def __str__(self):
        return "SymbolTable:\n" + str(self.__simtable)


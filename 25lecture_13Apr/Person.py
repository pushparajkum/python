class Person:
    def __init__(self, name, addr, dob):
        self.__name = name
        self.__addr = addr
        self.__dob = dob
    
    def getName(self):
        return self.__name
    
    def getAddr(self):
        return self.__addr

    def getdob(self):
        return self.__dob

    def UpdateAddress(self, address):
        self.__addr = address
        return True

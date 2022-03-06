class person:

    #deklarasi var
    __nik = 0
    __nama = ""
    __gender = ""
    __sleep = 0

    #konstruktor
    def __init__(self, nik=0, nama="", gender="", sleep=0):
        self.__nik = nik
        self.__nama = nama
        self.__gender = gender
        self.__sleep = sleep

    #Prosedur setter data
    def setNik(self, nik):
        self.__nik = nik
    
    def setNama(self, nama):
        self.__nama = nama

    def setGender(self, gender):
        self.__gender = gender

    def setSleep(self, sleep):
        self.__sleep = sleep
    
    #Prosedur getter data
    def getNik(self):
        return self.__nik

    def getNama(self):
        return self.__nama
    
    def getGender(self):
        return self.__gender
    
    def getSleep(self):
        if(self.__sleep == 0):
            return "Berangkat"
        elif(self.__sleep == 1):
            return "Istirahat"
        return self.__sleep
    
    #Prosedur menentukan sleep atau tidak
    def sleep(self):
        if(self.__sleep == 1):
            self.__sleep = 0
        elif(self.__sleep == 2):
            self.__sleep = 1
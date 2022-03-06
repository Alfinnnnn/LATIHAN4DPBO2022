#import kelas
from person import person

class driver(person):
    #deklarasi var
    __licence = ""
    __activeUntil= ""
    __vecType = ""

    #konstruktor
    def __init__(self, licence="", activeUntil="", vecType=""):
        self.__licence = licence
        self.__activeUntil = activeUntil
        self.__vecType = vecType
    
    #Prosedur setter data
    def setLicence(self, licence):
        self.__licence = licence
    
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def setVecType(self, vecType):
        self.__vecType = vecType
    
    #prosedur getter data
    def getLicence(self):
        return self.__licence

    def getActiveUntile(self):
        return self.__activeUntil
    
    def getvecType(self):
        return self.__vecType


    #prosedur menginput Driver
    def inputDriver(self, nik=0, nama="", gender="", sleep=0, licence="", activeUntil="", vecType=""):
        self.setNik(nik)
        self.setNama(nama)
        self.setGender(gender)
        self.setSleep(sleep)
        self.setLicence(licence)
        self.setActiveUntil(activeUntil)
        self.setVecType(vecType)
    
    #print data driver
    def printDriver(self):
        print("NIK             : " + str(self.getNik()))
        print("Nama            : " +str(self.getNama()))
        print("Gender          : " +str(self.getGender()))
        print("Lisensi         : " + str(self.getLicence()))
        print("Aktif Sampai    : " +str(self.getActiveUntile()))
        print("Jenis Kendaraan : " +str(self.getvecType()))
        print("Status          : " +str(self.getSleep()))
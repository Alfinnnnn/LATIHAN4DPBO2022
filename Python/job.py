#import kelas
from person import person

class job(person):
    #deklarasi var
    __nip = ""
    __company = ""
    __position = ""

    #konstruktor
    def __init__(self, nip="", company="", position=""):
        self.__nip = nip
        self.__company = company
        self.__position = position
    
    #prosedur setter data
    def setNip(self, nip):
        self.__nip = nip
    
    def setCompany(self, company):
        self.__company = company

    def setPosition(self, position):
        self.__position = position
    
    #prosedur getter data
    def getNip(self):
        return self.__nip
    
    def getCompany(self):
        return self.__company
    
    def getPosition(self):
        return self.__position
    
    #prosedur menginput job
    def inputJob(self, nik=0, nama="", gender="", sleep=0, nip="", company="", position=""):
        self.setNik(nik)
        self.setNama(nama)
        self.setGender(gender)
        self.setSleep(sleep)
        self.setNip(nip)
        self.setCompany(company)
        self.setPosition(position)
    
    #print data job
    def printJob(self):
        print("NIK     : " + str(self.getNik()))
        print("Nama    : " +str(self.getNama()))
        print("Gender  : " +str(self.getGender()))
        print("NIP     : " + str(self.getNip()))
        print("Company : " +str(self.getCompany()))
        print("Jabatan : " +str(self.getPosition()))
        print("Status  : " +str(self.getSleep()))

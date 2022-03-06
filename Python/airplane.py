#import kelas
from vehicle import vehicle

class airplane(vehicle):

    #deklarasi var
    __wingsLength = ""

    #konstruktor
    def __init__(self, wingsLength=""):
        self.__wingsLength = wingsLength
    
    #prosedur setter dan getter data
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    
    def getWingsLength(self):
        return self.__wingsLength

    #Input data airplane
    def inputPlane(self, type=0, fuelType="", age="", MaxPass="", move=0, wingsLength=""):
        self.setType(type)
        self.setfuelType(fuelType)
        self.setAge(age)
        self.setMaxPass(MaxPass)
        self.setMove(move)
        self.setWingsLength(wingsLength)

    #print data ship
    def printPlane(self):
        print("Tipe Pesawat        : " + str(self.getType()))
        print("Jenis Bahan Bakar   : " + str(self.getfuelType()))
        print("Usia Pesawat        : " +str(self.getAge()))
        print("Kapasitas Maksimal  : " +str(self.getMaxPass()))
        print("Status              : " +str(self.getMove()))
        print("Lebar Sayap Pesawat : " +(self.getWingsLength()))
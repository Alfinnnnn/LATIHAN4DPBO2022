#import kelas
from vehicle import vehicle

class ship(vehicle):

    #deklarasi var
    __country = ""

    #konstruktor
    def __init__(self, country=""):
        self.__country = country
    
    #prosedur setter dan getter country
    def setCountry(self, country):
        self.__country = country
    
    def getCountry(self):
        return self.__country
    
    #Input data ship
    def inputShip(self, type=0, fuelType="", age="", MaxPass="", move=0, country=""):
        self.setType(type)
        self.setfuelType(fuelType)
        self.setAge(age)
        self.setMaxPass(MaxPass)
        self.setMove(move)
        self.setCountry(country)
    
    #print data ship
    def printShip(self):
        print("Tipe Kapal         : " + str(self.getType()))
        print("Jenis Bahan Bakar  : " + str(self.getfuelType()))
        print("Usia Kapal         : " +str(self.getAge()))
        print("Kapasitas Maksimal : " +str(self.getMaxPass()))
        print("Status             : " +str(self.getMove()))
        print("Negara Asal        : " +(self.getCountry()))

class vehicle:
    #Deklarasi var
    __type = 0
    __fuelType = ""
    __age = ""
    __MaxPass = 0
    __move = 0

    #Constructor
    def __init__(self, type=0, fuelType="", age="", MaxPass=0, move=0):
        self.__type = type
        self.__fuelType = fuelType
        self.__age = age
        self.__MaxPass = MaxPass
        self.__move = move

    #Prosedur setter data
    def setType(self, type):
        self.__type = type

    def setfuelType(self, fuelType):
        self.__fuelType = fuelType

    def setAge(self, age):
        self.__age = age
    
    def setMaxPass(self, MaxPass):
        self.__MaxPass = MaxPass
    
    def setMove(self, move):
        self.__move = move
    
    #Prosedur getter data
    def getType(self):
        if(self.__type == 0):
            return "Pesawat Barang"
        elif(self.__type == 1):
            return "Pesawat Penumpang"
        elif(self.__type == 2):
            return "Kapal Barang"
        elif(self.__type == 3):
            return "Kapal Penumpang"
        return self.__type

    def getfuelType(self):
        return self.__fuelType
    
    def getAge(self):
        return self.__age

    def getMaxPass(self):
        return self.__MaxPass
    
    def getMove(self):
        if(self.__move == 0):
            return "Berangkat"
        elif(self.__move == 1):
            return "Tidak Berangkat"
        return self.__move

    #Prosedur mengatur type kendaraan 
    def type(self):
        if(self.__type == 0):
            self.__type = 0
        elif(self.__type == 1):
            self.__type = 1
        elif(self.__type == 2):
            self.__type = 2
        elif(self.__type == 3):
            self.__type = 3
    
    #Prosedur mengatur move
    def move(self):
        if(self.__move == 1):
            self.__move = 0
        elif(self.__move == 2):
            self.__move = 1
#import kelas
from asyncio.windows_events import NULL
from vehicle import vehicle
from ship import ship
from airplane import airplane
from person import person
from job import job
from driver import driver

#Memanggil + membuat list sebanyak data
vech_in = [NULL] * 5
ship_in = [NULL] * 5
plane_in = [NULL] * 5
person_in = [NULL] * 5
job_in = [NULL] * 5
driver_in = [NULL] * 5

for i in range (5) :
    vech_in[i] = vehicle()
    ship_in[i] = ship()
    plane_in[i] = airplane()
    person_in[i] = person()
    job_in[i] = job()
    driver_in[i] = driver()

#mengisi data kapal
ship_in[0].inputShip(3, "MDF", "3 Tahun", "200 Penumpang", 0, "Indonesia")
ship_in[1].inputShip(3, "MSD", "6 Tahun", "150 Penumpang", 0, "Indonesia")
ship_in[2].inputShip(2, "MFO", "4 Tahun", "70 Penumpang", 0, "USA")
ship_in[3].inputShip(2, "MFO", "8 Tahun", "20 Penumpang", 1, "Ukraine")
ship_in[4].inputShip(3, "MDF", "2 Tahun", "320 Penumpang", 0, "Rusia")

#Menampilkan data kapal
print("Data Kapal \n")
for i in range(5):
    print("Data ", i+1)
    ship_in[i].printShip()
    print("\n")
print("-----------------------------------------")

#mengisi data Pesawat
plane_in[0].inputPlane(1, "AVTUR", "1 Tahun", "150 Penumpang", 0, "30.4 m")
plane_in[1].inputPlane(1, "AVTUR", "3 Tahun", "170 Penumpang", 0, "34.7 m")
plane_in[2].inputPlane(0, "Avgas", "4 Tahun", "30 Penumpang", 0, "40.2 ,")
plane_in[3].inputPlane(0, "Avgas", "7 Tahun", "20 Penumpang", 1, "28.7 m")
plane_in[4].inputPlane(1, "AVTUR", "2 Tahun", "320 Penumpang", 0, "60.4 m")

#Menampilkan data Pesawat
print("Data Pesawat \n")
for i in range(5):
    print("Data ", i+1)
    plane_in[i].printPlane()
    print("\n")
print("-----------------------------------------")


#mengisi data Job
job_in[0].inputJob(320711,"Surya", "Laki-Laki", 0, "0001", "Garuda", "Pilot")
job_in[1].inputJob(320712, "Alfin" ,"Laki-Laki", 1, "0002", "IndoSinga", "Co-Pilot")
job_in[2].inputJob(320713, "Maoludin", "Laki-Laki", 1, "0003", "pinguinAir", "Supir")
job_in[3].inputJob(320714, "Neneng", "Perempuan", 1, "0004", "NagaAir", "Pramugari")
job_in[4].inputJob(320715, "Nisin" ,"Perempuan", 0, "0005", "Liomar" ,"Pramugari")

#Menampilkan data Job
print("Data Pegawai \n")
for i in range(5):
    print("Data ", i+1)
    job_in[i].printJob()
    print("\n")
print("-----------------------------------------")

#mengisi data Driver
driver_in[0].inputDriver(3420711,"Joko", "Laki-Laki", 0, "Licenced", "18 Mei 2025", "Mobil")
driver_in[1].inputDriver(3420712, "Dodo" ,"Laki-Laki", 1, "Licenced", "17 Agustus 2026", "Bus")
driver_in[2].inputDriver(3420713, "Amin", "Laki-Laki", 1, "UnLicenced", "-", "Bajaj")
driver_in[3].inputDriver(3420714, "Mega", "Perempuan", 1, "UnLicenced", "-", "Truk")
driver_in[4].inputDriver(3420715, "Wati" ,"Perempuan", 0, "Licenced", "8 April 2023" ,"Motor")

#Menampilkan data Driver
print("Data Driver \n")
for i in range(5):
    print("Data ", i+1)
    driver_in[i].printDriver()
    print("\n")
print("-----------------------------------------")

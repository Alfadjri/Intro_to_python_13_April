from abc import ABC, abstractclassmethod

class Kendaraan:
    @abstractclassmethod
    def menyalakan_mesin(self):
        pass


class Mobil(Kendaraan):
    def menyalakan_mesin(self): #overrider
        return "Start"

class Motor(Kendaraan):
    def menyalakan_mesin(self): ##overrider
        return "Motor Mogok"
    
Kendaraan = Kendaraan()
print(Kendaraan.menyalakan_mesin())
motor = Motor()
print(motor.menyalakan_mesin())
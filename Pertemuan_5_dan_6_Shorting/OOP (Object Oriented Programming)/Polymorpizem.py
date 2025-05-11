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
    


def start(Mobil): #polymorphism
    print(Mobil.menyalakan_mesin())

Motor = Motor()
Mobil = Mobil()

start(Motor)
start(Mobil)




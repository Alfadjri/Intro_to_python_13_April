class Ibu: 
    panggilan = "ini punya ibu"
    __sifat = "Baik"
    
    def memanggil(self):
        print("Iya , Ada apa ? ")
    
    def setSifat(self,sifat):
        self.__sifat = sifat
    
    def getSifat(self):
        print(f"Sifat ibu {self.__sifat}")
        
class Anak(Ibu): #inharitance
    def suruh(self):
        print("Nanti dulu lah !!!!!")
        

#Cara manggil 
Toni = Anak()
Toni.panggilan = "Toni"
print(f"Siapa nama anak ini : {Toni.panggilan}")
Toni.memanggil()
Toni.suruh()
Toni.setSifat("Pelwan")
Toni.getSifat()
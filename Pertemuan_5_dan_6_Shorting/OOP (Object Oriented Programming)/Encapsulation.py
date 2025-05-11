#mobil 

class Mobil:
    nama_mobil = "default"
    _defulat_ban = 4 #encapsulation 
    #encapsulation itu teknik penyembunyian nilai agak tidak di gangu
    
    def __init__(self,nama):
        self.nama_mobil = nama
    # get untuk ambil nilai
    def getMerek(self):
        return f"Merek mobil : {self.nama_mobil}\nJumlah ban : {self._defulat_ban} Ban"
    # Set untuk ganti nilai
    def setBan(self,jumlah_ban):
        self._defulat_ban = jumlah_ban
    

honda = Mobil("Puso")
honda.setBan(8)
print(f"{honda.getMerek()}")
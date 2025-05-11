# case
# Kita mengamati hewan 

class Hewan : # hewan itu nama_dari kelas
    nama_hewan = "default" # nama_hewan ini property (sifat) public object nama_hewan 
    _umur_hewan = 10 # _ ini untuk propery private (sifat)
    
    def __init__(self,nama_hewan): #constuctor ini di pakai untuk menyertakan nilai atau syarat saat memanggil kelas
        self.nama_hewan = nama_hewan
    
    def makan(self) : #method
        print("Hewan sedang makan !!!!")


#cara panggilnya
# kucing = Hewan()
# kucing.nama_hewan = "Tom"
kucing = Hewan("Tom")
print(f"Nama kucing {kucing.nama_hewan}")
# print(f"umur hewan {kucing.umur_hewan}")
print("kucing sedang apa ? ")
kucing.makan()

    
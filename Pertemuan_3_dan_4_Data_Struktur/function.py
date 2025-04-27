# function
# paramter adalah syarat yang di berikan kalau memanggil fuction
# def namaFunction(paramter):
    # apa yang akan kamu lakukan di dalam code sifat putus (void) atau berproses atau menghasilkan sesuatu
    
# Contoh void
def pemanggilan(nama_lengkap):
    print(f"Helo selamat {nama_lengkap}")
    

pemanggilan("Alfadjri")
pemanggilan("Dwi")
pemanggilan("Fadilah")

# contoh no void

def penjumlahan(a , b):
    return a + b
hasli = penjumlahan(10,10)
print(f"Hasil nya adalah : {hasli}")
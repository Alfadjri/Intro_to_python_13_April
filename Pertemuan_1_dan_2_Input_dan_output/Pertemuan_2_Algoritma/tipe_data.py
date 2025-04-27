#tipe data primitif
#integer adalah bilang bulat
x = 32767
print("ini contoh tipe data integer : {0}".format(x))
#float atau bubble adalah bilang desimal 
f = 3.14
print("ini contoh tipe data float : {0}".format(f))
# kompleks
z = 2 + 3j
print("ini contoh tipe data kompleks : {0}".format(z))

#tipe data text
#char , varchar , karakter adalah satuan huruf A , B , C , D
c = 'A'
print("ini contoh tipe data karakter : {0}".format(c))
# tipe data non primitif
# strings => char(255)
nama = "Alfadjri Dwi Fadhilah"
print("ini contoh tipe data String : {0}".format(nama))

#squence type
#list ini bisanya di gunakan untuk menampung tipe data yang sama dalam jumlah banyak
a = [24,25,32,20]
print("ini contoh tipe data list : {0}".format(a))
b = (4,5,6) # sifatnya tidak bisa ubah
print("ini contoh tipe data truplet : {0}".format(b))
e = range(0,5)
print("ini contoh tipe data range : {0}".format(e)) 

#tipe data maping
#dict kata lainnya vector (c) , array(java)
profile = { "nama" : "Alfadjri Dwi Fadhilah" , "age" : 24 }
print("ini contoh tipe data dict  ambil nama : {0}".format(profile["nama"]))

# set 
# tipe data yang tidak bisa di ubah lagi atau final 
f = {1,2,3}
print("ini contoh tipe data set : {0}".format(f))
g = frozenset({4,5,6})
print("ini contoh tipe data frozenset : {0}".format(g))

# tipe data kondisi
# boolean nilai ada 2 True(1) dan False(0)
kondisi_angka = 1
kondisi_angka_setelah_di_terjemahkan = bool(kondisi_angka)
kondisi = True
print("ini contoh tipe data boolean using simbolic : {0}".format(kondisi_angka_setelah_di_terjemahkan))
print("ini contoh tipe data boolean : {0}".format(kondisi))

#binary
i = 0b01000001
# desimal = int(i)
# karakter = chr(desimal)
karakter = chr(int(i))
print("ini contoh tipe data binary : {0}".format(karakter))
j = bytearray(a)
print("ini contoh tipe data bytearray : {0}".format(j))
z = memoryview(j)
print("ini contoh tipe data memoryview : {0}".format(z))


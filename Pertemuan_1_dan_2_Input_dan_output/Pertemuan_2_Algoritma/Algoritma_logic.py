# case check nilai siswa

#if
#format
# if kondisi : 
#   apa yang akan di lakukan kalau kondisi terpenuhi
print("===========if=============")
nilai = 70
if nilai > 80:
    print("Siswa ini lulus")

#if else
# di gunakan saat kamu mau memaksa kalau tidak tidak terpenuhi mau ke mana
print("===========if else=============")
try : # try and except di gunakan untuk membuat program tetatp berjalan walapun salah 
    nilai = 100
    if nilai  > 80 or nilai < 89:
        print("Siswa ini lulus")
    else : 
        print("Siswa ini tidak lulus")
except :
    print("Siswa ini tidak lulus")

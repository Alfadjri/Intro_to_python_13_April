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

print("===========Tenery (Lambda)=============")
pesan = "Siswa ini lulus" if nilai > 80 else "Siswa ini tidak lulus"
print(f"{pesan}")
print("===========if elif else (Bersarang)=============")
nilai = 50
if nilai > 80:
    print("Nilai anda lulus sempurna ")
elif nilai >= 70 and nilai < 80 :
    if nilai >= 75 : # if else bersarang
        print("Kurang 2 gagal ni!")
    else:
        print("Sedikit lagi kamu tidak lulus")
else :
    print("Kamu tidak lulus")


# kasus untuk menu
# match and case
print("===========match and case=============")
print("1. Start")
print("2. Exit")
selection = input("Selection >> ")
match selection:
    case "1":
        print("Start Game")
    case "2":
        print("Exit")
    case _ :
        print("Input not valid")
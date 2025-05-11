# while
# while di pakai jika kamu tau kapan berhenti tapi kapan prosesnya dan di check di petama kali
#format
# while syarat_berhenti :
    #  Apa yang akan di ulangi jika syarat belum terpenuhi
    
print("===========while========")
index = 0
while index <= 200 :
    print(f"Index of value {index}")
    index += 1

#for
# di pakai kalau kamu tahu semuanya mulai kapan berhenti sampai cara berhenti
print("===========for========")
# for index in range(1,201):
#      print(f"Index of value {index}")
    
makanan = ["baso","mie","sayur","daging","Buah"]
for value in makanan:
    print(f"{value}")

# break dan continue
bilangan = 1
while bilangan <= 100 :
    if bilangan % 2 == 0 :
        bilangan += 1 # penjabaran : bilangan = bilangan + 1
        continue # teknik untuk skip 1 putaran
    print(f"{bilangan}")
    bilangan += 1
    
    if bilangan > 40 :
        break #teknik untuk memberhentikan paksa looping
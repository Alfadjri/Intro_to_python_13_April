x = 10
y = 10

hasil = (x > y)
print(f"Apakah  {x} besar(>) dari {y} : {hasil}")
hasil = (x >= y)
print(f"Apakah  {x} besar sama dengan(>=) dari {y} : {hasil}")
hasil = (x < y)
print(f"Apakah  {x} kecil(<) dari {y} : {hasil}")
hasil = (x <= y)
print(f"Apakah  {x} kecil sama dengan (<=) dari {y} : {hasil}")
hasil = (x == y)
print(f"Apakah  {x} sama dengan (==) dari {y} : {hasil}")

x = False
hasil = (x != False) # ! (not) bertugas untuk menukar nilai yang ada saat ini 
print(f"Apakah nilai hasil : {hasil}")
x = None
hasil = (x != "")
print(f"Apakah nilai hasil : {hasil}")
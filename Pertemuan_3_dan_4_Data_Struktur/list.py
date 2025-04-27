# inlisalisai
makanans = ["Nasi","Sayur","Daging","puding"]

# Read (R)
# print all
print(f"{makanans}")
# read spesifik
print(f"Isi dari Index ke 1 adalah : {makanans[1]}")
print(f"isi dari index ini : {makanans[-3]}")

# add 
makanans.append("jeli")
print(f"{makanans}")
# delete
makanans.remove("puding")
print(f"{makanans}")
list_2 = ["pisang", "Semangka"]
makanans += list_2 # makanans = makanans + list_2 (incerment)
print(f"{makanans}")
profile = {
    "nama" : "alfadjri dwi Fadhilah",
    "umur" : 24,
    "Jabatan" : ["IT Support","Maestro"],
}

# Read
print(f"{profile}")
# Read spesifik
print(f"nama Lengkap : {profile["nama"]}")
print(f"Jabatan : {profile["Jabatan"][1]}")
# add value
profile["divisi"] = "Academic Codingstudio"
print(f"{profile}")
# delete
del profile["Jabatan"]
print(f"{profile}")
import datetime

tanggal_dibuat = datetime.datetime.now()
nama_atassan = "Gea Saskia"
nama_perusahaan = "PT Ruang Keahlian"
alamat_perusahaan = "Jalan Radin inten II No.66 RT01/RW07,Duren Sawit\nJakarta Timue 13440"

# \n = new line
# \t = tab (4 spasi)
# \i = italik
# \b = bold

# Posisional 
print("================== posisional ===========")
print("\t{0}\nYTH.IBU {1}\nManager SDM {2}\n{3}".format(tanggal_dibuat,nama_atassan,nama_perusahaan,alamat_perusahaan))
# keyword
print("================== Keyword ===========")
print("\t{tanggal}\nYTH.IBU {atasan}\nManager SDM {pt}\n{alamat}".format(pt=nama_perusahaan,tanggal=tanggal_dibuat,atasan = nama_atassan,alamat=alamat_perusahaan))
# cara singkat 
print("================== carasingkat ===========")
print(f"\t{tanggal_dibuat}\nYTH.IBU {nama_atassan}\nManager SDM {nama_perusahaan}\n{alamat_perusahaan}")
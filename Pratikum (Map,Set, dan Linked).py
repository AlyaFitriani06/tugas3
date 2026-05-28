#====Partikum Pertama==
kalimat = "ini adalah contoh kalimat untuk menghitung frekuensi kata"
kata_frekuensi = {}

for kata in kalimat.split():
    if kata in kata_frekuensi:
        kata_frekuensi[kata] += 1
    else:
        kata_frekuensi[kata] = 1

print(kata_frekuensi)


#======Pratikum Kedua======
print("=" * 5, "CONTOH 1", "=" * 5)

# Tipe Data: Set (Himpunan) :
StokMobil = {"Toyota",
             "Kijang",
             "Karimun",
             "Daihatsu"}

StokMobil.add("Hyundai")
StokMobil.add("Daihatsu")  # Tidak akan ditambahkan
StokMobil.add("Daihatsuu")

print(StokMobil)
print("\n")

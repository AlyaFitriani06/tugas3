#=================================
#DATA BELANJA (DICT + LIST + TUPLE
#Format:(nama_barang, jumlah, harga
#=================================

belanjaan={
    "senin":[
        ("beras",5,12000),
        ("gula",2, 14000),
        ("minyak", 3, 15000)
        ],
    "selasa":[
        ("beras",2, 12000),
        ("telur",10,2000),
        ("mie",2, 3000)
        ],
    "rabu":[
        ("gula",1, 14000),
        ("mie",3, 3000),
        ("kopi",2, 10000)
        ]
}

#=============================
#FUNGSI HITUNG TOTAL PER HARI
#=============================
def hitung_total_per_hari(data_hari):
    total = 0
    for nama, jumlah, harga in data_hari:
        total += jumlah * harga
    return total

#================================
# FUNGSI REKAP SEMUA BARANG
#================================
def cari_barang(data, keyword):
    hasil=[]
    for hari in data:
        for nama, jumlah, harga in data[hari]:
            if keyword.lower() in nama.lower():
                hasil.append((hari, nama, jumlah, harga))
    return hasil

#=================================
#FUNGSI SORTING BARANG TERBANYAK
#=================================
def urutkan_barang_terbanyak(rekap):
    return sorted(rekap.items(), key=lambda x: x[1]["jumlah"], reverse=True)

#=============================
#TAMPILKAN DATA
#=============================
print("\n==== DATA BELANJA ====")
for hari, items in belanjaan.items():
    print(f"\nHari: {hari}")
    for nama, jumlah, harga in items:
        print(f"-{nama} | jumlah: {jumlah} | harga: {harga}")

#============================
#TOTAK PER HARI
#============================
print(f"\n==== TOTAL PER HARI =====")
for hari in belanjaan:
    total= hitung_total_per_hari(belanjaan[hari])
    print(f"{hari}: Rp {total}")
#===================
#REKAP KESELURUHAN
#===================
total_semua = sum(hitung_total_per_hari(belanjaan[h]) for h in belanjaan)
print(f"\nTOTAL SEMUA BELANJA: Rp {total_semua}")

#===================
#REKAP DATA
#===================
def rekap_semua_barang(data):
    rekap={}
    for hari in data:
       for nama, jumlah, harga in data[hari]:
           if nama not in rekap:
               rekap[nama]={"jumlah":0,"total_harga": 0}
           rekap[nama]["jumlah"] += jumlah
           rekap[nama]["total_harga"] += jumlah * harga
    return rekap
print("\n==== REKAP SEMUA BARANG ====")
#=========================
# BARANG TERBANYAK
#=========================
rekap = rekap_semua_barang(belanjaan)
terbanyak = urutkan_barang_terbanyak(rekap)
print(F"\n==== BARANG TERBANYAK ====")
for nama, info in terbanyak:
    print(f"{nama} ({info['jumlah']} pcs)")

#=========================
#PENCARIAN BARANG
#=========================
keyword = input("\nMasukkan nama barang yang ingin dicari: ")
hasil = cari_barang(belanjaan, keyword)

print("\n==== HASIL PENCARIAN ====")
if hasil:
    for hari, nama, jumlah, harga in hasil:
        print(f"{hari} -> {nama} | jumlah: {jumlah} | harga: {harga}")
else:
    print("Barang tidak ditemukan")

#=====================
#BONUS:  DISKON
#=====================
if total_semua > 100000:
    diskon = total_semua * 0.1
    total_akhir = total_semua - diskon
    print(f"\nAnda mendapatkan diskon 10%: Rp {diskon}")
    print(f"Total setelah diskon: RP {total_akhir}")
else:
    print("\nTidak ada diskon")

print("===========================================")
print("SISTEM NILAI MAHASISWA")
print("============================================")

daftar_nilai = []   
def tambah_nilai(nilai):
    daftar_nilai.append(nilai)
    
def hitung_rata_rata():
    if len(daftar_nilai) == 0:
        return 0
    return sum(daftar_nilai)/len(daftar_nilai)

def cari_tertinggi():
    if len(daftar_nilai) ==0:
        return 0
    return max (daftar_nilai)
def cari_terendah():
    if len(daftar_nilai) ==0:
        return 0
    return min (daftar_nilai)
def tampilkan_nilai():
    print("\n=== Daftar Nilai Mahasiswa ===")
    for i, nilai in enumerate(daftar_nilai, start=1):
        print(f"{i}. {nilai}")

print("=== Input Nilai Mahasiswa ===")
n = int(input("Masukkan jumlah mahasiswa: "))

for i in range(n):
    nilai = float(input(f"Nilai mahasiswa ke-{i+1}: "))
    tambah_nilai(nilai)

tampilkan_nilai()
print(f"\nRata-rata nilai  : {hitung_rata_rata():.2f}")
print(f"Nilai tertinggi : {cari_tertinggi()}")
print(f"Nilai terendah : {cari_terendah()}")

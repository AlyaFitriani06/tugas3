antrian=["Budi","Sari","Dian","Eko"]#akses satu elemen berdasarkan index
print("pelanggan pertama:",antrian[0])#index 0= depan
print("pelanggan terakhir:",antrian[-1])#index -1 = belakang
print("pelanggan ke-3:",antrian[2])#index 2 #akses panjang antrian
print("jumlah antrian:",len(antrian))#akses seluruh isi(looping)
print("\nDaftar antrian:")
for i, nama in enumerate(antrian):#enumerate akses beserta indexnya
    print(f"[{i}] {nama}")

#cek apakah seseorang ada dalam antrian
    print("\nApakah Sari ada di antrian?","Sari" in antrian)
    print("Apakah Tono ada di antrian?", "Tono"in antrian)

print(antrian[1:4])
print(antrian[1:3])

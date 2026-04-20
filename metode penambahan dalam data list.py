buah=["apel","mangga"]#append()- menambahkan satu elemen di akhir list
buah.append("jeruk")
print(buah)

buah=["apel","mangga"]#inser(index,nilai)- tambah di index tertentu
buah.insert(1, "pisang")
print(buah)

buah=["apel","mangga"]#extend()-menambahkan semua elemen dari list lain atau menggabungkan 2 list
tambahan=["jeruk","semangka"]
buah.extend(tambahan)
print(buah)

buah=["apel","mangga"]#operator(+) menggabungkan dua list dan membuat list baru
tambahan=["jeruk","anggur"]
semua= buah + tambahan
print(semua)

angka=[1, 2, 3, 4, 5]#list comprehension-buat list dari hasil proses
kuadrat=[x**2 for x in angka]#- ** di artikan pangkat jika * itu di artikan kali
print(kuadrat)

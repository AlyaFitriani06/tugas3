print("Nama: Alya Fitriani")
print("NIM : TI22250004")

from collections import deque

#----1. DATA BUKU-----
buku_list = [] #Menggunakan List karena buku jumlahnya banyak, bisa ditambah/dihapus dan bisa ditampilkan semua

kategori = ("Novel", "Komik", "Pelajaran", "Teknologi") #menggunakan Tuple karena Tuple  bersifat tetap

# ----2. ANTRIAN & STACK----
antrian = []
riwayat = []
antrian_prioritas = deque()


#-----FUNGSI BUKU------
def tambah_buku():
    judul = input("Judul: ")
    penulis = input("Penulis: ")
    kategori_input = input("Kategori: ")

    if kategori_input not in kategori:
        print("Kategori tidak valid!")
        return

    buku = {
        "judul": judul,
        "penulis": penulis,
        "kategori": kategori_input
    } #Menggunakan Dictionary untuk menyimpan detail setiap (judul,penulis,kategori) dan lebih rapi

    buku_list.append(buku) #saat pengguna menambahkan buku, sistem menerima input lalu menyimpan dalam bentuk dictionary,kemudian di masukkan ke list ketika ditambahkan akan berada diakhir, karena list bersifat dinamis dan urutan tidak terlalu penting
    print("Buku berhasil ditambahkan!")

def hapus_buku():
    judul = input("Masukkan judul buku: ")
    for buku in buku_list:
        if buku["judul"] == judul:
            buku_list.remove(buku) #Saat menghapus buku mencari buku berdasarkan judul jika ketemu maka dihapus,jika tidak di temukan maka diberikan keterangan dan harus dilooping satu per satu karena list tidak punya pencarian otomatis
            print("Buku dihapus")
            return
    print("Buku tidak ditemukan")

def tampil_buku():
    if not buku_list: #untuk menampilkan semua buku, sistem melakukan perulangan pada list dan menampilkan setiap data buku
        print("Tidak ada buku")
    else:
        for b in buku_list:
            print(b)

def cari_buku(): #untuk mencari buku, sistem membandingkan judul input dengan data yang ada di dalam list
    judul = input("Cari judul: ")
    ditemukan = False
    for b in buku_list:
        if b["judul"] == judul:
            print(b)
            ditemukan = True
    if not ditemukan:
        print("Tidak ditemukan")


#-----ANTRIAN PEMINJAMAN-----

def tambah_antrian(): #menggunakan konsep Queue(FIFO)-> yang datang duluan dilayani lebih dulu
    nama = input("Nama peminjam: ")
    antrian.append(nama) #pengguna yang akan meminjam buku akan masuk antrian kedalam antrian bagian belakang
    print("Masuk antrian")

def proses_antrian(): #Saat proses peminjaman dilakukan, sistem mengambil data dari bagian depan antrian
    if not antrian:
        print("Antrian kosong")
    else:
        data = antrian.pop(0)
        print("Diproses:", data)

def lihat_antrian(): #sistem dapat menampilkan siapa yang berada di urutan paling depan
    if not antrian:
        print("Kosong")
    else:
        print("Terdepan:", antrian[0])


#-----STACK RIWAYAT------

def tambah_riwayat(): #menggunakan Stack(LIFO) setiap pengambilan buku disimpan kedalam stack
    data = input("Data pengembalian: ")
    riwayat.append(data)
    print("Riwayat disimpan")

def batal_terakhir(): #jika terjadi kesalahan, sistem bisa membatalkan data terakhir dengan menghapus elemen paling atas
    if not riwayat:
        print("Kosong")
    else:
        riwayat.pop()
        print("Data terakhir dibatalkan")

def lihat_terakhir(): #sistem juga dapat melihat data pengembalian terakhir
    if not riwayat:
        print("Kosong")
    else:
        print("Terakhir:", riwayat[-1])


#-----DEQUE PRIORITAS-----

def tambah_prioritas(): #Menggunakan Deque karena bisa menambahkan dan menghapus data dari dua sisi
    nama = input("Nama: ")
    jenis = input("Jenis (dosen/mahasiswa): ") #mahasiswa masuk antrian ke belakang

    if jenis == "dosen":
        antrian_prioritas.appendleft(nama) #dosen memiliki prioritas lebih tinggi jadi masukkan ke antrian terdepan
    else:
        antrian_prioritas.append(nama)

    print("Masuk antrian prioritas")

def proses_prioritas():
    if not antrian_prioritas:
        print("Kosong")
    else:
        print("Diproses:", antrian_prioritas.popleft())

def batal_prioritas():
    if not antrian_prioritas:
        print("Kosong")
    else:
        antrian_prioritas.pop()
        print("Antrian belakang dibatalkan")

#---BONUS---
def jumlah_buku():
    print("Jumlah buku:", len(buku_list)) #sistem menghitung total buku dengan melihat jumlah elemen dalam list

def kategori_terbanyak(): #sistem menghitung jumlah masing-masing kategori kemudian mencari kategori dengan jumlah paling besar
    hitung = {}
    for b in buku_list:
        k = b["kategori"]
        hitung[k] = hitung.get(k, 0) + 1

    if hitung:
        terbanyak = max(hitung, key=hitung.get)
        print("Kategori terbanyak:", terbanyak)
    else:
        print("Belum ada data")


def menu(): #Disini user/pengguna untuk memilih menu yanng tersedia atau di tampilkan
    while True:
        print("\n=== MENU ===")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampil Buku")
        print("4. Cari Buku")
        print("5. Antrian Peminjaman")
        print("6. Riwayat Pengembalian")
        print("7. Antrian Prioritas")
        print("8. Bonus")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_buku()
        elif pilih == "2":
            hapus_buku()
        elif pilih == "3":
            tampil_buku()
        elif pilih == "4":
            cari_buku()
        elif pilih == "5":
            tambah_antrian()
            proses_antrian()
            lihat_antrian()
        elif pilih == "6":
            tambah_riwayat()
            lihat_terakhir()
            batal_terakhir()
        elif pilih == "7":
            tambah_prioritas()
            proses_prioritas()
            batal_prioritas()
        elif pilih == "8":
            jumlah_buku()
            kategori_terbanyak()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid")

menu()

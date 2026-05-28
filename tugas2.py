"""
PROGRAM KERANGKA (BELUM SELESAI)
Mahasiswa diminta melengkapi algoritma & struktur data
(Boleh menggunakan: Stack / Queue / Dequeue / Kombinasi)
"""

# =========================================
# BAGIAN 1 — STRUKTUR DATA (PILIH / BUAT SENDIRI)
# =========================================

class StrukturData:
    def __init__(self):
        self.data = []

    def tambah(self, item):
        # TODO: tentukan apakah ini enqueue / push / add_front / add_rear
        pass

    def ambil(self):
        # TODO: tentukan apakah ini dequeue / pop / remove_front / remove_rear
        pass

    def lihat(self):
        # TODO: peek (opsional)
        pass

    def kosong(self):
        return len(self.data) == 0


# =========================================
# BAGIAN 2 — MANAJEMEN PESANAN
# =========================================

class SistemRestoran:
    def __init__(self):
        # TODO: mahasiswa menentukan struktur data yang digunakan
        self.antrian = StrukturData()

        # TODO: jika ingin fitur undo → tambahkan stack
        self.riwayat = None  

    def tambah_pelanggan(self, nama, tipe):
        """
        tipe:
        - 'normal'
        - 'vip'
        """
        # TODO:
        # - jika VIP → prioritas?
        # - jika normal → biasa?
        pass

    def batalkan_pesanan(self):
        """
        Undo pesanan terakhir
        """
        # TODO: gunakan konsep stack
        pass

    def proses_dapur(self):
        """
        Dapur memproses pesanan
        """
        # TODO:
        # - ambil dari antrian
        # - tampilkan siapa yang diproses
        pass

    def tampilkan_antrian(self):
        # TODO: tampilkan isi antrian
        pass


# =========================================
# BAGIAN 3 — SIMULASI / MENU PROGRAM
# =========================================

def menu():
    sistem = SistemRestoran()

    while True:
        print("\n=== SISTEM RESTORAN ===")
        print("1. Tambah Pelanggan")
        print("2. Proses Pesanan")
        print("3. Batalkan Pesanan (Undo)")
        print("4. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama pelanggan: ")
            tipe = input("Tipe (normal/vip): ")

            # TODO: panggil method tambah_pelanggan
            pass

        elif pilihan == "2":
            # TODO: proses dapur
            pass

        elif pilihan == "3":
            # TODO: undo pesanan
            pass

        elif pilihan == "4":
            # TODO: tampilkan antrian
            pass

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


# =========================================
# ENTRY POINT
# =========================================
if _name_ =="_main_":
    menu()

from collections import deque

# =========================================
# BAGIAN 1 — STRUKTUR DATA (DEQUE)
# =========================================

class StrukturData:
    def __init__(self):
        self.data = deque()

    def tambah_belakang(self, item):  # enqueue
        self.data.append(item)

    def tambah_depan(self, item):  # VIP
        self.data.appendleft(item)

    def ambil(self):  # dequeue
        if not self.kosong():
            return self.data.popleft()
        return None

    def lihat(self):
        if not self.kosong():
            return self.data[0]
        return None

    def kosong(self):
        return len(self.data) == 0

    def tampil(self):
        return list(self.data)


# =========================================
# BAGIAN 2 — MANAJEMEN PESANAN
# =========================================

class SistemRestoran:
    def __init__(self):
        self.antrian = StrukturData()
        self.riwayat = []  # stack

    def tambah_pelanggan(self, nama, tipe):
        pelanggan = (nama, tipe)

        if tipe == "vip":
            self.antrian.tambah_depan(pelanggan)
            print(f"{nama} (VIP) masuk ke depan antrian")
        else:
            self.antrian.tambah_belakang(pelanggan)
            print(f"{nama} masuk ke antrian biasa")

        self.riwayat.append(pelanggan)  # simpan ke stack

    def batalkan_pesanan(self):
        if not self.riwayat:
            print("Tidak ada pesanan untuk dibatalkan")
            return

        terakhir = self.riwayat.pop()

        try:
            self.antrian.data.remove(terakhir)
            print(f"Pesanan {terakhir[0]} dibatalkan")
        except ValueError:
            print("Pesanan sudah diproses, tidak bisa dibatalkan")

    def proses_dapur(self):
        if self.antrian.kosong():
            print("Tidak ada pesanan")
            return

        pelanggan = self.antrian.ambil()
        print(f"Memproses pesanan: {pelanggan[0]} ({pelanggan[1]})")

    def tampilkan_antrian(self):
        if self.antrian.kosong():
            print("Antrian kosong")
        else:
            print("Daftar Antrian:")
            for i, (nama, tipe) in enumerate(self.antrian.tampil(), 1):
                print(f"{i}. {nama} ({tipe})")


# =========================================
# BAGIAN 3 — MENU
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
            sistem.tambah_pelanggan(nama, tipe)

        elif pilihan == "2":
            sistem.proses_dapur()

        elif pilihan == "3":
            sistem.batalkan_pesanan()

        elif pilihan == "4":
            sistem.tampilkan_antrian()

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


# =========================================
# ENTRY POINT
# =========================================

menu()

#----algoritma----
#1.mulai
#2.-buat deque antrian
# -buat stack untuk undo
#3.selama ada pelanggan:
#-input nama & jenis
#jika vip: masukkan ke depan antrian
#jika biasa:masukkan ke belakang
#4.simpan ke stack
#5.jika ada proses dapur: ambil dari depan antrian
#6.jika undo:
#-ambil dari stack
#-hapus dari antrian
#7.selesai

#---flow proses
#1.pelanggan datang
#2.cek jenis:
#-vip:masuk depan antrian
#-biasa:masuk belakang antrian
#3.simpan pesanan ke stack(untuk undo)
#4.dapur ambil dari depan antrian
#5.jika batal ambil dari stack(undo)

from collections import deque
antrian = deque()#antrian utama

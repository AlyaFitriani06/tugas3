import string

kata_spam = {"promo", "diskon", "gratis", "hadiah", "voucher"}

while True:

    print("\n=== CEK EMAIL SPAM ===")
    print("Ketik 'keluar' untuk berhenti")

    email = input("Masukkan isi email: ")

    if email.lower() == "keluar":
        break

    # Menghapus tanda baca
    email = email.lower().translate(
        str.maketrans("", "", string.punctuation)
    )

    kata_email = set(email.split())

    spam_ditemukan = kata_spam.intersection(kata_email)

    print("\n=== HASIL CEK EMAIL ===")

    if spam_ditemukan:
        print("EMAIL SPAM")
        print("Kata spam ditemukan:", spam_ditemukan)
    else:
        print("EMAIL NORMAL")

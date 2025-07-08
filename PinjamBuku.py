# List Book (code, title, author, year, genre, publisher, page)
ListBook = {
    "BIO01": {"Title": "Dianaworld: An Obsession", "Author": "Edward White",  "Year": 2025, "Genre": "Biography", "Publisher": "W. W. Norton & Company", "Page": 416},
    "BIO02": {"Title": "We Are The Beatles", "Author": "Brad Meltzer",  "Year": 2025, "Genre": "Biography", "Publisher": "Rocky Pond Books", "Page": 40},
    "HIS01": {"Title": "Genghis Khan", "Author": "Jack Weatherford",  "Year": 2004, "Genre": "History", "Publisher": "Broadway Books", "Page": 352},
    "HIS02": {"Title": "The Silk Roads", "Author": "Peter Frankopan",  "Year": 2015, "Genre": "History", "Publisher": "Bloomsbury", "Page": 636},
    "PSY01": {"Title": "The Pyschology of Money", "Author": "Morgan Housel",  "Year": 2020, "Genre": "Psychology", "Publisher": "Harriman House", "Page": 242},
    "PSY02": {"Title": "The Power of Habit", "Author": "Charless Duhigg",  "Year": 2012, "Genre": "Psychology", "Publisher": "Random House", "Page": 375},
    "FIC01": {"Title": "The da Vinci Code", "Author": "Dan Brown",  "Year": 2003, "Genre": "Fiction", "Publisher": "Anchor", "Page": 480},
    "FIC02": {"Title": "The Hunger Games", "Author": "Suzanne Collins",  "Year": 2008, "Genre": "Fiction", "Publisher": "Scholastic Press", "Page": 374},
    "ROM01": {"Title": "Pride and Prejudice", "Author": "Jane Austen",  "Year": 1813, "Genre": "Romance", "Publisher": "Peter Pauper Press", "Page": 400},
    "ROM02": {"Title": "The Notebook", "Author": "Nicholas Sparks",  "Year": 1996, "Genre": "Romance", "Publisher": "Grand Central Publishing", "Page": 227},
    "SCI01": {"Title": "Sapiens", "Author": "Yuval Noah Harari",  "Year": 2011, "Genre": "Science", "Publisher": "Vintage", "Page": 512},    
    "SCI02": {"Title": "Why We Sleep", "Author": "Matthew Walker",  "Year": 2017, "Genre": "Science", "Publisher": "Scribner", "Page": 368},
    "THR01": {"Title": "The Girl With the Dragon Tatoo", "Author": "Stieg Larsson",  "Year": 2005, "Genre": "Thriller", "Publisher": "Viking Canada", "Page": 480},
    "THR02": {"Title": "The Girl on the Train", "Author": "Paula Hawkins",  "Year": 2015, "Genre": "Thriller", "Publisher": "Riverhead Books", "Page": 336},
    "TRA01": {"Title": "Lost on Planet China", "Author": "J. Maarten Troost",  "Year": 2008, "Genre": "Travel", "Publisher": "Broadway Books", "Page": 382},
    "TRA02": {"Title": "A Walk in the Woods", "Author": "Bill Bryson",  "Year": 1998, "Genre": "Travel", "Publisher": "Vintage", "Page": 397},
}


# Menu tampilkan semua buku
def tampilkan_semua_buku():
    print("Daftar Buku".center(120))
    print("\n")
    print(f"{'Kode':<6} | {'Judul':<30} | {'Penulis':<20} | {'Tahun':<5} | {'Genre':<10} | {'Penerbit':<25} | {'Hal.':<4}")
    print("-" * 120)
    
    for code, info in sorted(ListBook.items()):
        print(f"{code:<6} | {info['Title']:<30} | {info['Author']:<20} | {info['Year']:<5} | {info['Genre']:<10} | {info['Publisher']:<25} | {info['Page']:<4}")


# Menu cari buku
def cari_buku():
    kata_kunci = input("Masukkan kata kunci pencarian (kode, judul, penulis, tahun, genre, penerbit): ").lower()
    ditemukan = False

    print("\nHasil Pencarian:")
    print("="*120)
    print(f"{'Kode':<6} | {'Judul':<30} | {'Penulis':<20} | {'Tahun':<5} | {'Genre':<10} | {'Penerbit':<25} | {'Hal.':<4}")
    print("-" * 120)

    for kode, info in ListBook.items():
        if (kata_kunci in kode.lower() or
            kata_kunci in info["Title"].lower() or
            kata_kunci in info["Author"].lower() or
            kata_kunci in str(info["Year"]).lower() or
            kata_kunci in info["Genre"].lower() or
            kata_kunci in info["Publisher"].lower()):
            
            print(f"{kode:<6} | {info['Title']:<30} | {info['Author']:<20} | {info['Year']:<5} | {info['Genre']:<10} | {info['Publisher']:<25} | {info['Page']:<4}")
            ditemukan = True

    if not ditemukan:
        print("Tidak ada buku yang cocok dengan kata kunci tersebut.")


# Menu tambah buku baru
def tambah_buku():
    kode = input("Masukkan kode buku (contoh: FIC03): ").upper()
    if kode in ListBook:
        print("Data sudah ada.")
    else:
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun = input("Masukkan tahun terbit: ")
        genre = input("Masukkan genre: ")
        penerbit = input("Masukkan nama penerbit: ")
        halaman = input("Masukkan jumlah halaman: ")
        ListBook[kode] = {
            "Title": judul,
            "Author": penulis,
            "Year": int(tahun),
            "Genre": genre,
            "Publisher": penerbit,
            "Page": int(halaman)
    }
   
    print("Buku berhasil ditambahkan!\n")


# Menu update data buku
def update_buku():
    kode = input("Masukkan kode buku yang ingin diedit: ").upper()
    if kode in ListBook:
        print("Data lama:", ListBook[kode])
        judul = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
        penulis = input("Masukkan penulis baru: ")
        tahun = input("Masukkan tahun terbit baru: ")
        genre = input("Masukkan genre baru: ")
        penerbit = input("Masukkan penerbit baru: ")
        halaman = input("Masukkan jumlah halaman baru: ")

        if judul:
            ListBook[kode]["Title"] = judul
        if penulis:
            ListBook[kode]["Author"] = penulis
        if tahun:
            ListBook[kode]["Year"] = int(tahun)
        if genre:
            ListBook[kode]["Genre"] = genre
        if penerbit:
            ListBook[kode]["Publisher"] = penerbit
        if halaman:
            ListBook[kode]["Page"] = int(halaman)

        print("Data buku berhasil diperbarui!\n")
    else:
        print("Kode buku tidak ditemukan.")

# Menu hapus buku
def hapus_buku():
    kode = input("Masukkan kode buku yang ingin dihapus: ").upper()
    if kode in ListBook:
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus buku '{ListBook[kode]['Title']}'? (y/n): ").lower()
        if konfirmasi == 'y':
            del ListBook[kode]
            print("Buku berhasil dihapus.\n")
        else:
            print("Penghapusan dibatalkan.\n")
    else:
        print("Kode buku tidak ditemukan.\n")


# Menu pinjam buku
def pinjam_buku():
    kode = input("Masukkan kode buku yang ingin dipinjam: ").upper()
    if kode in ListBook:
        if ListBook[kode].get("Status") == "Dipinjam":
            print("Maaf, buku sedang dipinjam.")
        else:
            nama = input("Masukkan nama peminjam: ")
            tanggal = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
            ListBook[kode]["Status"] = "Dipinjam"
            ListBook[kode]["Peminjam"] = nama
            ListBook[kode]["Tanggal Pinjam"] = tanggal
            print(f"Buku '{ListBook[kode]['Title']}' berhasil dipinjam oleh {nama} pada {tanggal}.")
    else:
        print("Kode buku tidak ditemukan.")


def kembalikan_buku():
    kode = input("Masukkan kode buku yang ingin dikembalikan: ").upper()
    if kode in ListBook and ListBook[kode].get("Status") == "Dipinjam":
        ListBook[kode]["Status"] = "Tersedia"
        ListBook[kode].pop("Peminjam", None)
        ListBook[kode].pop("Tanggal Pinjam", None)
        print(f"Buku '{ListBook[kode]['Title']}' berhasil dikembalikan.")
    else:
        print("Buku tidak sedang dipinjam atau kode tidak ditemukan.")


# MAIN MENU

def menu():
    print("\n" + "=== MENU PERPUSTAKAAN ===".center(120))
    print("1. Tampilkan semua buku")
    print("2. Cari buku")
    print("3. Tambah buku baru")
    print("4. Update buku")
    print("5. Hapus buku")
    print("6. Pinjam buku")
    print("7. Pengembalian buku")
    print("8. Keluar")

# Program utama
while True:
    menu()
    pilihan = input("Masukkan pilihan (1-8): ")
    
    if pilihan == "1":
        tampilkan_semua_buku()
    elif pilihan == "2":
        cari_buku()
    elif pilihan == "3":
        tambah_buku()
    elif pilihan == "4":
        update_buku()
    elif pilihan == "5":
        hapus_buku()
    elif pilihan == "6":
        pinjam_buku()
    elif pilihan == "7":
        kembalikan_buku()
    elif pilihan == "8":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
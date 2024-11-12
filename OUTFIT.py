def rekomendasi_outfit():
    print("Selamat datang di sistem rekomendasi mix and match outfit!")
    print("Pilih menu pertanyaan:")
    print("1. Pilih berdasarkan tren")
    print("2. Pilih berdasarkan preferensi")
    print("3. Pilih berdasarkan warna")

    pilihan_menu = input("Masukkan pilihan (1/2/3): ")

    if pilihan_menu == '1':
        pilih_tren()
    elif pilihan_menu == '2':
        pilih_preferensi()
    elif pilihan_menu == '3':
        pilih_warna()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        rekomendasi_outfit()  # Menambahkan rekursi untuk mengulangi menu

def pilih_tren():
    print("Pilih tren: (Korean/Western)")
    tren = input("Masukkan pilihan: ").lower()

    if tren == 'korean':
        print("Pilih gaya: Feminin, Manis, Kasual, Chic, Nyaman, Stylish, Modis, Bohemian, Trendy, Santai, Street, Siluet, Smart, Sporty")
        gaya = input("Masukkan gaya: ").lower()
        rekomendasi_korean(gaya)
    elif tren == 'western':
        print("Pilih gaya: Stylish, Chic, Santai, Nyaman, Street, Acara, Elegan, Youthful, Layered, Rapi, Winter, Edgy, Classy, Kasual")
        gaya = input("Masukkan gaya: ").lower()
        rekomendasi_western(gaya)
    else:
        print("Pilihan tren tidak valid.")
        pilih_tren()  # Menambahkan rekursi untuk mengulangi pilihan tren

def rekomendasi_korean(gaya):
    outfit_korean = {
        'feminin': "Blouse Berenda + Rok A-Line",
        'manis': "Dress Midi Floral + Cardigan Oversized",
        'kasual': "Kaos Grafis + Celana Jeans High-Waisted",
        'chic': "Kemeja Klasik + Suspender Skirt",
        'nyaman': "Sweater Rajut + Celana Kulot",
        'stylish': "Dress Mini + Kaos Lengan Panjang",
        'modis': "Kemeja Lengan Pendek + Celana Palazzo",
        'bohemian': "Kimono + Tank Top + Skinny Jeans",
        'trendy': "Rok Midi Plisket + Sweater Crop",
        'santai': "Kaftan + Celana Panjang",
        'street': "T-shirt Oversized + Celana Cargo",
        'siluet': "Dress Satin + Belt",
        'smart': "Blazer + Tank Top + Ripped Jeans",
        'sporty': "Skirt Mini + Hoodie"
    }
    print("Rekomendasi outfit:", outfit_korean.get(gaya, "Gaya tidak ditemukan."))

def rekomendasi_western(gaya):
    outfit_western = {
        'stylish': "T-shirt Graphic + Jeans Straight Leg",
        'chic': "Blazer + Tank Top + Skirt Mini",
        'santai': "Dress Maxy Bohemian + Sandal Gladiator",
        'nyaman': "Sweater Chunky + Legging",
        'street': "Kemeja Flanel + Celana Jogger",
        'acara': "Jumpsuit Formal + Heels",
        'elegan': "Rok Midi + Kemeja Putih",
        'youthful': "Kaos Crop + Celana High-Waisted",
        'layered': "Kimono + Dress Pendek",
        'rapi': "Sweater V-Neck + Celana Chino",
        'winter': "Puffer Jacket + Celana Denim",
        'edgy': "Rok Leather + Turtleneck",
        'classy': "Duster Coat + Jeans",
        'kasual': "Overalls Denim + T-shirt Lengan Pendek"
    }
    print("Rekomendasi outfit:", outfit_western.get(gaya, "Gaya tidak ditemukan."))

def pilih_preferensi():
    print("Pilih preferensi: (gelap/terang)")
    preferensi = input("Masukkan pilihan: ").lower()

    if preferensi == 'gelap':
        print("Pilih kategori: Sleek, Cozy, Edgy, Chic, Santai, Sporty, Formal, Profesional, Hangat")
        kategori = input("Masukkan kategori: ").lower()
        rekomendasi_gelap(kategori)
    elif preferensi == 'terang':
        print("Pilih kategori: Ceria, Segar, Cerah, Lembut, Sleek, Cozy, Sporty, Bohemian, Berani, Santai")
        kategori = input("Masukkan kategori: ").lower()
        rekomendasi_terang(kategori)
    else:
        print("Pilihan preferensi tidak valid.")
        pilih_preferensi()  # Menambahkan rekursi untuk mengulangi pilihan preferensi

def rekomendasi_gelap(kategori):
    outfit_gelap = {
        'sleek': "Kemeja Hitam + Celana Panjang Hitam",
        'cozy': "Sweater Abu-abu Tua + Rok Midi Hitam",
        'edgy': "T-shirt Hitam + Jaket Kulit + Jeans Gelap",
        'chic': "Dress Midi Hitam + Sepatu Boot Hitam",
        'santai': "Kemeja Flanel Merah Tua + Celana Jogger Hitam",
        'sporty': "Cardigan Hitam + Tank Top Hitam + Legging Hitam",
        'formal': "Jumpsuit Hitam + Sepatu Heels Hitam",
        'profesional': "Blazer Hitam + Turtleneck Abu-abu + Rok Pensil Hitam",
        'hangat': "Sweater Hitam + Celana Chino Cokelat Tua"
    }
    print("Rekomendasi outfit:", outfit_gelap.get(kategori, "Kategori tidak ditemukan."))

def rekomendasi_terang(kategori):
    outfit_terang = {
        'ceria': "Kaos Putih + Rok Paduan Warna Pastel",
        'segara': "Blouse Kuning Cerah + Celana Jeans Biru Muda",
        'cerah': "Dress Floral Berwarna Cerah + Sandal Putih",
        'lembut': "Sweater Pink Muda + Celana Chino Beige",
        'sleek': "Kemeja Hijau Lime + Rok Denim",
        'cozy': "T-shirt Orange + Celana Pendek Putih",
        'sporty': "Jumpsuit Biru Langit + Sneakers Putih",
        'bohemian': "Kimono Berwarna Cerah + Tank Top Hitam + Jeans",
        'berani': "Rok Midi Merah + Sweater Putih"
    }
    print("Rekomendasi outfit:", outfit_terang.get(kategori, "Kategori tidak ditemukan."))

# Fungsi untuk rekomendasi berdasarkan warna
def pilih_warna():
    warna_data = {
        'merah': {
            'bold': "Merah & Hitam",
            'segara': "Merah & Putih",
            'modern': "Merah & Abu-abu",
            'chic': "Merah & Navy",
            'ceria': "Merah & Kuning"
        },
        'kuning': {
            'bold': "Kuning & Hitam",
            'ceria': "Kuning & Putih",
            'modern': "Kuning & Abu-abu",
            'stylish': "Kuning & Biru Navy",
            'playful': "Kuning & Merah Muda"
        },
        'hijau': {
            'cerah': "Hijau & Putih",
            'earthy': "Hijau & Coklat",
            'modern': "Hijau & Abu-abu",
            'sejuk': "Hijau & Biru",
            'vibrant': "Hijau & Kuning"
        },
        'biru': {
            'klasik': "Biru & Putih",
            'playful': "Biru & Kuning",
            'modern': "Biru & Abu-abu",
            'dinamis': "Biru & Merah",
            'hangat': "Biru & Coklat"
        },
        'hitam': {
            'elegan': "Hitam & Putih",
            'glamour': "Hitam & Merah",
            'sleek': "Hitam & Abu-abu",
            'mewah': "Hitam & Emas",
            'stylish': "Hitam & Biru Navy"
        },
        'putih': {
            'chic': "Putih & Hitam",
            'ceria': "Putih & Biru",
            'natural': "Putih & Coklat",
            'berani': "Putih & Merah",
            'modern': "Putih & Abu-abu"
        },
        'abu-abu': {
            'sleek': "Abu-abu & Hitam",
            'elegan': "Abu-abu & Putih",
            'berani': "Abu-abu & Merah",
            'stylish': "Abu-abu & Biru",
            'playful': "Abu-abu & Kuning"
        },
        'ungu': {
            'glamour': "Ungu & Emas",
            'elegan': "Ungu & Putih",
            'modern': "Ungu & Abu-abu",
            'playful': "Ungu & Merah Muda",
            'segar': "Ungu & Hijau"
        },
        'coklat': {
            'klasik': "Coklat & Putih",
            'energik': "Coklat & Kuning",
            'polo': "Coklat & Biru",
            'natural': "Coklat & Hijau",
            'berani': "Coklat & Merah"
        },
        'oranye': {
            'ceria': "Oranye & Putih",
            'bold': "Oranye & Hitam",
            'modern': "Oranye & Abu-abu",
            'energik': "Oranye & Biru",
            'earthy': "Oranye & Coklat"
        },
        'pink': {
            'feminin': "Pink & Putih",
            'playful': "Pink & Abu-abu",
            'chic': "Pink & Hitam",
            'energik': "Pink & Kuning",
            'modern': "Pink & Biru"
        },
        'biru muda': {
            'feminin': "Biru Muda & Putih",
            'energik': "Biru Muda & Abu-abu",
            'modern': "Biru Muda & Kuning",
            'earthy': "Biru Muda & Merah Muda",
            'ceria': "Biru Muda & Coklat"
        },
        'hijau tua': {
            'segar': "Hijau Tua & Putih",
            'earthy': "Hijau Tua & Coklat",
            'stylish': "Hijau Tua & Abu-abu",
            'energik': "Hijau Tua & Kuning",
            'chic': "Hijau Tua & Biru Navy"
        }
    }

    print("Pilih warna: (merah, kuning, hijau, biru, hitam, putih, abu-abu, ungu, coklat, oranye, pink, biru muda, hijau tua)")
    warna = input("Masukkan pilihan: ").lower()

    if warna in warna_data:
        print(f"Pilih kategori untuk {warna}: {', '.join(warna_data[warna].keys())}")
        kategori = input("Masukkan kategori: ").lower()

        if kategori in warna_data[warna]:
            print(f"Rekomendasi outfit {warna} untuk kategori {kategori}: {warna_data[warna][kategori]}")
        else:
            print("Kategori tidak valid.")
            pilih_warna()  # Rekursi jika kategori tidak valid
    else:
        print("Warna tidak valid.")
        pilih_warna()  # Rekursi jika warna tidak valid

# Menjalankan program utama
rekomendasi_outfit()

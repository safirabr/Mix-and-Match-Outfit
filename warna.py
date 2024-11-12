import json

# Fungsi untuk memuat data outfit dari file JSON
def load_outfits_data():
    with open('outfits.json', 'r') as file:
        return json.load(file)

def pilih_warna():
    # Memuat data outfits
    outfits_data = load_outfits_data()

    # Menanyakan warna yang ingin dipilih
    print("Pilih warna: (merah, kuning, hijau, biru, hitam, putih, abu-abu, ungu, coklat, oranye, pink, biru muda, hijau tua)")
    warna = input("Masukkan pilihan warna: ").lower()

    # Memeriksa apakah warna yang dipilih ada dalam data
    if warna in outfits_data['warna']:
        # Mendapatkan daftar kategori untuk warna yang dipilih
        kategori_list = outfits_data['warna'][warna].keys()
        print(f"Pilih kategori untuk warna {warna}: {', '.join(kategori_list)}")
        
        # Menanyakan kategori untuk warna yang dipilih
        kategori = input("Masukkan kategori: ").lower()
        
        # Memanggil fungsi untuk rekomendasi berdasarkan kategori yang dipilih
        rekomendasi_warna(outfits_data['warna'][warna], kategori)
    else:
        print("Warna tidak valid. Silakan pilih warna yang terdaftar.")
        pilih_warna()  # Memanggil ulang fungsi jika warna tidak valid

def rekomendasi_warna(outfits_warna, kategori):
    # Mendapatkan outfit berdasarkan kategori yang dipilih
    outfit = outfits_warna.get(kategori, "Kategori tidak ditemukan.")
    print(f"Rekomendasi outfit untuk kategori {kategori}: {outfit}")

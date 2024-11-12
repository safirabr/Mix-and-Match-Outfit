import json

# Fungsi untuk memuat data outfit dari file JSON
def load_outfits_data():
    with open('outfits.json', 'r') as file:
        return json.load(file)

def pilih_preferensi():
    # Memuat data outfits
    outfits_data = load_outfits_data()
    
    # Menanyakan preferensi pengguna
    preferensi = input("Pilih preferensi: (gelap/terang): ").lower()

    if preferensi == 'gelap':
        print("Pilih kategori: Sleek, Cozy, Edgy, Chic, Santai, Sporty, Formal, Profesional, Hangat")
        kategori = input("Masukkan kategori: ").lower()
        rekomendasi_gelap(outfits_data['preferensi']['gelap'], kategori)
    elif preferensi == 'terang':
        print("Pilih kategori: Ceria, Segar, Cerah, Lembut, Sleek, Cozy, Sporty, Bohemian, Berani, Santai")
        kategori = input("Masukkan kategori: ").lower()
        rekomendasi_terang(outfits_data['preferensi']['terang'], kategori)
    else:
        print("Pilihan preferensi tidak valid.")
        pilih_preferensi()  # Rekursi jika input tidak valid

def rekomendasi_gelap(outfits_gelap, kategori):
    outfit = outfits_gelap.get(kategori, "Kategori tidak ditemukan.")
    print(f"Rekomendasi outfit gelap untuk kategori {kategori}: {outfit}")

def rekomendasi_terang(outfits_terang, kategori):
    outfit = outfits_terang.get(kategori, "Kategori tidak ditemukan.")
    print(f"Rekomendasi outfit terang untuk kategori {kategori}: {outfit}")

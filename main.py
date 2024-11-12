import json
from menu import tampilkan_menu
from tren import pilih_tren
from preferensi import pilih_preferensi
from warna import pilih_warna

def load_outfits_data():
    # Memuat data dari file JSON
    with open('outfits.json', 'r') as f:
        return json.load(f)

def main():
    outfits_data = load_outfits_data()

    while True:
        pilihan_menu = tampilkan_menu()

        if pilihan_menu == '1':
            tren = pilih_tren()
            if tren == 'korean':
                print("Pilih gaya: Feminin, Manis, Kasual, Chic, Nyaman, Stylish, Modis, Bohemian, Trendy, Santai, Street, Siluet, Smart, Sporty")
                gaya = input("Masukkan gaya: ").lower()
                print("Rekomendasi outfit:", outfits_data['korean'].get(gaya, "Gaya tidak ditemukan"))
            elif tren == 'western':
                print("Pilih gaya: Stylish, Chic, Santai, Nyaman, Street, Acara, Elegan, Youthful, Layered, Rapi, Winter, Edgy, Classy, Kasual")
                gaya = input("Masukkan gaya: ").lower()
                print("Rekomendasi outfit:", outfits_data['western'].get(gaya, "Gaya tidak ditemukan"))
            else:
                print("Pilihan tren tidak valid. Silakan coba lagi.")

        elif pilihan_menu == '2':
            preferensi = pilih_preferensi()
            # Mengambil preferensi gelap/terang
            if preferensi == 'gelap' or preferensi == 'terang':
                print(f"Pilih kategori untuk preferensi {preferensi}: {', '.join(outfits_data['preferensi'][preferensi].keys())}")
                kategori = input("Masukkan kategori: ").lower()
                print("Rekomendasi outfit:", outfits_data['preferensi'][preferensi].get(kategori, "Kategori tidak ditemukan"))
            else:
                print("Preferensi tidak valid. Silakan pilih antara gelap atau terang.")

        elif pilihan_menu == '3':
            # Memanggil fungsi pilih_warna dari warna.py
            pilih_warna()

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        # Menanyakan apakah ingin melanjutkan
        lanjut = input("Ingin mencoba lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break

if __name__ == "__main__":
    main()

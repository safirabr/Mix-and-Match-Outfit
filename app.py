from gui.window import create_window
from data.data_loader import load_data

def main():
    # Memuat data dari file JSON
    outfits_data = load_data()

    # Membuat jendela aplikasi
    create_window(outfits_data)

if __name__ == "__main__":
    main()

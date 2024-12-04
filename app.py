from gui.window import create_window
from data.data_loader import load_data
import json

def load_outfits_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)
def main():
    # Memuat data dari file JSON
    outfits_data = load_data()

    # Membuat jendela aplikasi
    create_window(outfits_data)

if __name__ == "__main__":
    # Path ke file JSON
    filepath = r"data.json"

    # Load data JSON
    outfits_data = load_outfits_data(filepath)

    # Jalankan GUI
    main()
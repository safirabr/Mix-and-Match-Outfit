import json
import os
from datetime import datetime

# Fungsi untuk memuat data pengguna dari file JSON
def load_user_data(file_path="data/user_data.json"):
    """
    Memuat data pengguna dari file JSON.
    Jika file tidak ada, kembalikan data default.
    """
    if not os.path.exists(file_path):
        # Jika file tidak ditemukan, kembalikan data default
        return {"user_preferences": {"style": "", "substyle": "", "outfit_history": []}}
    
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        # Jika file rusak atau tidak dapat dibaca, kembalikan data default
        return {"user_preferences": {"style": "", "substyle": "", "outfit_history": []}}

# Fungsi untuk menyimpan data pengguna ke dalam file JSON
def save_user_data(data, file_path="data/user_data.json"):
    """
    Menyimpan data pengguna ke dalam file JSON.
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Fungsi untuk menambahkan outfit ke dalam riwayat dengan tanggal
def add_outfit_to_history(outfit, file_path="data/user_data.json"):
    """
    Menambahkan outfit yang dipilih oleh pengguna ke dalam riwayat outfit dengan tanggal.
    """
    # Mendapatkan tanggal saat ini
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Memuat data pengguna dari file JSON
    user_data = load_user_data(file_path)
    
    # Menambahkan tanggal ke dalam outfit
    outfit_with_date = {
        "outfit": outfit,
        "date_added": timestamp
    }
    
    # Menambahkan outfit yang sudah disertakan tanggal ke dalam riwayat
    user_data["user_preferences"]["outfit_history"].append(outfit_with_date)
    
    # Menyimpan data yang sudah diperbarui ke dalam file JSON
    save_user_data(user_data, file_path)

# Fungsi untuk memperbarui gaya dan subgaya pengguna
def update_user_preferences(style, substyle, file_path="data/user_data.json"):
    """
    Memperbarui gaya (style) dan subgaya (substyle) pengguna.
    """
    user_data = load_user_data(file_path)
    user_data["user_preferences"]["style"] = style
    user_data["user_preferences"]["substyle"] = substyle
    save_user_data(user_data, file_path)

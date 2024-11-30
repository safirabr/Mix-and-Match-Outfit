import json
import os
import sqlite3
from datetime import datetime

# Fungsi untuk memuat data pengguna dari file JSON
def load_user_data_json(file_path="user_data/user_data.json"):
    """
    Memuat data pengguna dari file JSON.
    Jika file tidak ada, kembalikan data default.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {"history": []}  # Kembalikan data default jika file tidak ada

# Fungsi untuk menyimpan data pengguna ke file JSON
def save_user_data_json(data, file_path="user_data/user_data.json"):
    """
    Menyimpan data pengguna ke file JSON.
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Fungsi untuk menginisialisasi database SQLite
def init_db(db_path="user_data/user_data.db"):
    """
    Menginisialisasi database SQLite untuk menyimpan riwayat pilihan pengguna.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Membuat tabel riwayat jika belum ada
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        sub_category TEXT,
        outfit TEXT,
        timestamp TEXT
    )
    ''')

    conn.commit()
    conn.close()

# Fungsi untuk menambahkan riwayat pengguna ke database SQLite
def add_user_history_to_db(category, sub_category, outfit, db_path="user_data/user_data.db"):
    """
    Menambahkan riwayat pilihan pengguna ke database SQLite.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Menambahkan riwayat pilihan pengguna ke tabel
    c.execute('''
    INSERT INTO user_history (category, sub_category, outfit, timestamp)
    VALUES (?, ?, ?, ?)
    ''', (category, sub_category, outfit, timestamp))

    conn.commit()
    conn.close()

# Fungsi untuk mengambil riwayat pengguna dari database SQLite
def get_user_history_from_db(db_path="user_data/user_data.db"):
    """
    Mengambil riwayat pilihan pengguna dari database SQLite.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('SELECT * FROM user_history ORDER BY timestamp DESC')
    rows = c.fetchall()

    conn.close()

    return rows

# Fungsi untuk menambahkan riwayat pengguna ke dalam JSON dan SQLite
def add_user_history(category, sub_category, outfit, use_json=True, use_db=True):
    """
    Menambahkan riwayat pilihan pengguna ke dalam file JSON dan/atau database SQLite.
    """
    # Menambahkan ke file JSON
    if use_json:
        user_data = load_user_data_json()
        user_data["history"].append({"category": category, "sub_category": sub_category, "outfit": outfit, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        save_user_data_json(user_data)
    
    # Menambahkan ke database SQLite
    if use_db:
        add_user_history_to_db(category, sub_category, outfit)

# Fungsi untuk menampilkan riwayat pengguna (dari JSON atau SQLite)
def display_user_history(use_json=True, use_db=True):
    """
    Menampilkan riwayat pilihan pengguna.
    """
    if use_json:
        user_data = load_user_data_json()
        print("Riwayat Pilihan (JSON):")
        for entry in user_data["history"]:
            print(f"Kategori: {entry['category']}, Sub-kategori: {entry['sub_category']}, Outfit: {entry['outfit']}, Timestamp: {entry['timestamp']}")
    
    if use_db:
        history = get_user_history_from_db()
        print("\nRiwayat Pilihan (Database):")
        for entry in history:
            print(f"ID: {entry[0]}, Kategori: {entry[1]}, Sub-kategori: {entry[2]}, Outfit: {entry[3]}, Timestamp: {entry[4]}")


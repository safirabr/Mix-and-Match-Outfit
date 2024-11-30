import json

def load_data(file_path="data.json"):
    """
    Fungsi untuk memuat data dari file JSON.
    
    Parameters:
        file_path (str): Lokasi file JSON yang akan dibaca. Default adalah 'data.json'.
    
    Returns:
        dict: Data yang dibaca dari file JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
        return None
    except json.JSONDecodeError:
        print("Error: File tidak dapat diparse sebagai JSON.")
        return None
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

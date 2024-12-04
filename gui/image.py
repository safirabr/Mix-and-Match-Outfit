from PIL import Image, ImageTk
import tkinter as tk
import os

def show_image(parent, image_name):
    # Ganti karakter '&' dengan 'dan' dan '+' dengan '_'
    # image_name = image_name.replace(" & ", "_dan_").replace(" + ", "_")  # Ganti & dan + dengan format yang valid
    
    # Menentukan path gambar
    image_path = os.path.join("images", f"{image_name}.jpeg")
    
    # Cek apakah file gambar ada
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((200, 200))  # Menyesuaikan ukuran gambar
        photo = ImageTk.PhotoImage(img)
        
        label = tk.Label(parent, image=photo)
        label.image = photo  # Menyimpan referensi gambar
        label.pack()
    else:
        # Jika gambar tidak ditemukan, tampilkan teks placeholder
        label = tk.Label(parent, text="Gambar tidak ditemukan", font=("Arial", 12), fg="#ff0000", bg="#f2f2f2")
        label.pack()
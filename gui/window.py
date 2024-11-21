import tkinter as tk
from tkinter import messagebox  # Mengimpor modul messagebox
from PIL import Image, ImageTk  # Mengimpor Image dan ImageTk dari Pillow
from gui.widgets import create_label, create_radio_button, create_category_radio_buttons
from gui.image import show_image
from data.outfits import get_outfit_suggestion

def create_window(outfits_data):
    window = tk.Tk()
    window.title("My Outfit Advisor")
    window.geometry("800x600")
    window.config(bg="#f2f2f2")  # Warna pastel

    # Menampilkan Message Box Selamat Datang
    messagebox.showinfo("Selamat Datang", "Selamat datang di Your Outfit Advisor!")  # Pesan selamat datang

    # Menambahkan Logo di bagian atas
    logo_path = "assets/logo.jpg"  # Ganti dengan path logo yang sesuai
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((800, 400))  # Ukuran logo disesuaikan
    logo_photo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(window, image=logo_photo, bg="#f2f2f2")
    logo_label.image = logo_photo  # Menyimpan referensi gambar agar tidak hilang
    logo_label.pack(pady=20)

    # Header
    create_label(window, text="My Outfit Advisor", font=("Arial", 24, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=20)

    # Menambahkan Frame untuk masing-masing halaman
    frame_utama = tk.Frame(window, bg="#f2f2f2")
    frame_tren = tk.Frame(window, bg="#f2f2f2")
    frame_preferensi = tk.Frame(window, bg="#f2f2f2")
    frame_warna = tk.Frame(window, bg="#f2f2f2")
    frame_tren_substyle = tk.Frame(window, bg="#f2f2f2")
    frame_preferensi_substyle = tk.Frame(window, bg="#f2f2f2")
    frame_warna_substyle = tk.Frame(window, bg="#f2f2f2")

    # Menampilkan frame pertama (Frame Utama)
    def show_frame(frame):
        # Sembunyikan semua frame
        for f in [frame_utama, frame_tren, frame_preferensi, frame_warna, frame_tren_substyle, frame_preferensi_substyle, frame_warna_substyle]:
            f.pack_forget()

        # Tampilkan frame yang diminta
        frame.pack(fill="both", expand=True)

    show_frame(frame_utama)  # Menampilkan Frame Utama di awal

    # Menambahkan pilihan kategori Tren, Preferensi, dan Warna
    category_variable = tk.StringVar()
    sub_category_variable = tk.StringVar()

    # Menghapus fungsi update_outfit, karena tombol Get Outfit sudah dihapus

    # Menambahkan tombol untuk berpindah antar kategori (Tren, Preferensi, Warna)
    tren_button = tk.Button(frame_utama, text="Tren", font=("Arial", 14), bg="#33b5b5", fg="white", command=lambda: show_frame(frame_tren))
    tren_button.pack(pady=10)

    preferensi_button = tk.Button(frame_utama, text="Preferensi", font=("Arial", 14), bg="#33b5b5", fg="white", command=lambda: show_frame(frame_preferensi))
    preferensi_button.pack(pady=10)

    warna_button = tk.Button(frame_utama, text="Warna", font=("Arial", 14), bg="#33b5b5", fg="white", command=lambda: show_frame(frame_warna))
    warna_button.pack(pady=10)

    # Tombol Kembali ke Halaman Utama
    def back_to_home():
        show_frame(frame_utama)

    # Menambahkan konten untuk masing-masing kategori
    def create_tren_content():
        create_label(frame_tren, text="Ini adalah halaman Tren", font=("Arial", 14), fg="#333333", bg="#f2f2f2")
        # Tombol untuk berpindah ke substyle tren
        substyle_button_tren = tk.Button(frame_tren, text="Pilih Substyle Tren", font=("Arial", 14), bg="#33b5b5", fg="white", command=lambda: show_frame(frame_tren_substyle))
        substyle_button_tren.pack(pady=10)
        # Tombol Kembali
        back_button_tren = tk.Button(frame_tren, text="Kembali", font=("Arial", 12), bg="#ff6f61", fg="white", command=lambda: show_frame(frame_utama))
        back_button_tren.pack(pady=10)
    
    def create_preferensi_content():
        create_label(frame_preferensi, text="Ini adalah halaman Preferensi", font=("Arial", 14), fg="#333333", bg="#f2f2f2")
        # Tombol untuk berpindah ke substyle preferensi
        substyle_button_preferensi = tk.Button(frame_preferensi, text="Pilih Substyle Preferensi", font=("Arial", 14), bg="#33b5b5", fg="white", command=lambda: show_frame(frame_preferensi_substyle))
        substyle_button_preferensi.pack(pady=10)
        # Tombol Kembali
        back_button_preferensi = tk.Button(frame_preferensi, text="Kembali", font=("Arial", 12), bg="#ff6f61", fg="white", command=lambda: show_frame(frame_utama))
        back_button_preferensi.pack(pady=10)

    def create_warna_content():
        create_label(frame_warna, text="Ini adalah halaman Warna", font=("Arial", 14), fg="#333333", bg="#f2f2f2")
        # Tombol untuk berpindah ke substyle warna
        substyle_button_warna = tk.Button(frame_warna, text="Pilih Substyle Warna", font=("Arial", 14), bg="#33b5b5", fg="white", command=lambda: show_frame(frame_warna_substyle))
        substyle_button_warna.pack(pady=10)
        # Tombol Kembali
        back_button_warna = tk.Button(frame_warna, text="Kembali", font=("Arial", 12), bg="#ff6f61", fg="white", command=lambda: show_frame(frame_utama))
        back_button_warna.pack(pady=10)

    # Menambahkan konten untuk substyle masing-masing kategori
    def create_tren_substyle_content():
        create_label(frame_tren_substyle, text="Pilih Substyle Tren", font=("Arial", 14), fg="#333333", bg="#f2f2f2")
        create_category_radio_buttons(frame_tren_substyle, ["Western", "Korean"], lambda: None, sub_category_variable)
        back_button_tren_substyle = tk.Button(frame_tren_substyle, text="Kembali", font=("Arial", 12), bg="#ff6f61", fg="white", command=lambda: show_frame(frame_tren))
        back_button_tren_substyle.pack(pady=10)

    def create_preferensi_substyle_content():
        create_label(frame_preferensi_substyle, text="Pilih Substyle Preferensi", font=("Arial", 14), fg="#333333", bg="#f2f2f2")
        create_category_radio_buttons(frame_preferensi_substyle, ["Gelap", "Korean"], lambda: None, sub_category_variable)
        back_button_preferensi_substyle = tk.Button(frame_preferensi_substyle, text="Kembali", font=("Arial", 12), bg="#ff6f61", fg="white", command=lambda: show_frame(frame_preferensi))
        back_button_preferensi_substyle.pack(pady=10)

    def create_warna_substyle_content():
        create_label(frame_warna_substyle, text="Pilih Substyle Warna", font=("Arial", 14), fg="#333333", bg="#f2f2f2")
        create_category_radio_buttons(frame_warna_substyle, ["Merah", "Kuning", "Hijau", "Biru", "Hitam", "Putih", "Abu-abu", "Ungu", "Coklat", "Oranye", "Pink", "Biru Muda", "Hijau Tua"], lambda: None, sub_category_variable)
        back_button_warna_substyle = tk.Button(frame_warna_substyle, text="Kembali", font=("Arial", 12), bg="#ff6f61", fg="white", command=lambda: show_frame(frame_warna))
        back_button_warna_substyle.pack(pady=10)

    # Memanggil fungsi untuk menambahkan konten pada tiap halaman
    create_tren_content()
    create_preferensi_content()
    create_warna_content()
    create_tren_substyle_content()
    create_preferensi_substyle_content()
    create_warna_substyle_content()

    # Fungsi untuk menangani penutupan aplikasi
    def on_closing():
        if messagebox.askyesno("Konfirmasi", "Sampai jumpa, semoga membantu! Apakah Anda yakin ingin keluar?"):
            window.destroy()  # Menutup aplikasi jika pengguna memilih "Yes"

    # Mengaitkan fungsi on_closing dengan penutupan jendela
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Menampilkan window
    window.mainloop()

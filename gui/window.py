import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gui.widgets import create_label, create_radio_button
from gui.image import show_image
from data.outfits import get_outfit_suggestion

def create_window(outfits_data):
    # Inisialisasi jendela utama
    window = tk.Tk()
    window.title("My Outfit Advisor")
    window.geometry("800x600")
    window.config(bg="#f2f2f2")

    # Pesan selamat datang
    messagebox.showinfo("Selamat Datang", "Selamat datang di Your Outfit Advisor!")

    # Menambahkan logo
    try:
        logo_path = "assets/logo.jpg"
        logo_img = Image.open(logo_path).resize((800, 400))
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(window, image=logo_photo, bg="#f2f2f2")
        logo_label.image = logo_photo
        logo_label.pack(pady=20)
    except Exception as e:
        print(f"Error memuat logo: {e}")

    # Frame untuk setiap "Face"
    frames = {
        "utama": tk.Frame(window, bg="#f2f2f2"),
        "tren": tk.Frame(window, bg="#f2f2f2"),
        "preferensi": tk.Frame(window, bg="#f2f2f2"),
        "warna": tk.Frame(window, bg="#f2f2f2"),
        "result": tk.Frame(window, bg="#f2f2f2"),
    }

    def show_frame(frame_name):
        for frame in frames.values():
            frame.pack_forget()
        frames[frame_name].pack(fill="both", expand=True)

    # Halaman utama (Face 1)
    def create_main_page():
        create_label(
            frames["utama"], 
            text="Pilih Kategori", 
            font=("Arial", 24, "bold"), 
            fg="#33b5b5", 
            bg="#f2f2f2", 
            pady=20
        )
        categories = {
            "Tren": "tren",
            "Preferensi": "preferensi",
            "Warna": "warna",
        }
        for category, frame_name in categories.items():
            tk.Button(
                frames["utama"], 
                text=category, 
                font=("Arial", 14), 
                bg="#33b5b5", 
                fg="white", 
                command=lambda name=frame_name: show_frame(name)
            ).pack(pady=10)

    create_main_page()

    # Subkategori untuk setiap kategori (Face 2)
    subcategories = {
        "tren": ["Western", "Korean"],
        "preferensi": ["Gelap", "Casual"],
        "warna": [
            "Merah", "Kuning", "Hijau", "Biru", "Hitam", "Putih", "Abu-abu",
            "Ungu", "Coklat", "Oranye", "Pink", "Biru Muda", "Hijau Tua"
        ],
    }

    selected_subcategory = tk.StringVar()

    def create_subcategory_page(category):
        create_label(
            frames[category],
            text=f"Pilih {category.capitalize()}",
            font=("Arial", 20, "bold"),
            fg="#33b5b5",
            bg="#f2f2f2",
            pady=20
        )

        for sub in subcategories[category]:
            create_radio_button(
                frames[category], 
                text=sub, 
                variable=selected_subcategory, 
                value=sub
            )

        tk.Button(
            frames[category], 
            text="Lanjutkan", 
            font=("Arial", 14), 
            bg="#33b5b5", 
            fg="white", 
            command=lambda: show_frame("result")
        ).pack(pady=20)

        tk.Button(
            frames[category], 
            text="Kembali", 
            font=("Arial", 12), 
            bg="#ff6f61", 
            fg="white", 
            command=lambda: show_frame("utama")
        ).pack(pady=10)

    for category in subcategories.keys():
        create_subcategory_page(category)

    # Halaman hasil (Face 3 & 4)
    def create_result_page():
        def display_result():
            choice = selected_subcategory.get()
            suggestion = get_outfit_suggestion(outfits_data, choice)

            for widget in frames["result"].winfo_children():
                widget.destroy()

            if suggestion:
                create_label(
                    frames["result"], 
                    text=f"Rekomendasi untuk {choice}", 
                    font=("Arial", 20, "bold"), 
                    fg="#33b5b5", 
                    bg="#f2f2f2", 
                    pady=20
                )
                try:
                    image_path = suggestion["image"]
                    show_image(frames["result"], image_path)
                except KeyError:
                    create_label(
                        frames["result"], 
                        text="Gambar tidak tersedia.", 
                        font=("Arial", 14), 
                        fg="red", 
                        bg="#f2f2f2"
                    )
            else:
                create_label(
                    frames["result"], 
                    text="Tidak ada rekomendasi ditemukan.", 
                    font=("Arial", 14), 
                    fg="red", 
                    bg="#f2f2f2"
                )

            tk.Button(
                frames["result"], 
                text="Kembali", 
                font=("Arial", 14), 
                bg="#ff6f61", 
                fg="white", 
                command=lambda: show_frame("utama")
            ).pack(pady=20)

        selected_subcategory.trace("w", lambda *args: display_result())

    create_result_page()

    # Fungsi untuk menangani penutupan aplikasi
    def on_closing():
        if messagebox.askyesno("Konfirmasi", "Sampai jumpa! Apakah Anda yakin ingin keluar?"):
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    show_frame("utama")
    window.mainloop()

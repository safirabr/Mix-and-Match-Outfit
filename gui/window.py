from tkinter import messagebox
from gui.widgets import create_button, create_label, create_radio_button
from gui.image import show_image
from data.outfits import get_outfit_suggestion

def create_window(outfits_data):
    window = tk.Tk()
    window.title("My Outfit Advisor")
    window.geometry("800x600")
    window.config(bg="#f2f2f2")  # Warna pastel

    # Header
    create_label(window, text="My Outfit Advisor", font=("Arial", 24, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=20)

    # Pilihan Kategori Tren, Preferensi, dan Warna
    category_variable = tk.StringVar()
    sub_category_variable = tk.StringVar()

    def update_outfit():
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        outfit = get_outfit_suggestion(category, sub_category, outfits_data)
        
        # Tampilkan outfit sebagai label
        create_label(window, text=outfit, font=("Arial", 12), fg="#333333", bg="#f2f2f2", pady=20)

        # Tampilkan gambar outfit yang dipilih
        show_image(window, outfit)

    # Menambahkan pilihan kategori (tren, preferensi, warna)
    create_label(window, text="Pilih Kategori:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2")
    create_category_radio_buttons(window, ["tren", "preferences", "colors"], update_outfit, category_variable)

    # Menambahkan pilihan sub-kategori
    def update_sub_categories():
        selected_category = category_variable.get()
        sub_categories = []
        if selected_category == "tren":
            sub_categories = list(outfits_data["trends"].keys())
        elif selected_category == "preferences":
            sub_categories = list(outfits_data["preferences"].keys())
        elif selected_category == "colors":
            sub_categories = list(outfits_data["colors"].keys())
        
        # Menghapus RadioButton lama dan menambahkan yang baru
        for widget in window.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()
        
        create_radio_button(window, sub_categories, update_outfit, sub_category_variable)

    # Update sub kategori saat kategori utama berubah
    category_variable.trace("w", lambda *args: update_sub_categories())

    # Tombol untuk mendapatkan outfit
    create_button(window, text="Get Outfit", font=("Arial", 14), bg="#ff6f61", fg="white", command=update_outfit, pady=10)
    
    # Menampilkan window
    window.mainloop()

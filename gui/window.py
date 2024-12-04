import json
import tkinter as tk
from tkinter import messagebox, PhotoImage
from gui.widgets import create_button, create_label, create_radio_button, create_category_radio_buttons
from gui.image import show_image

# Fungsi untuk mendapatkan rekomendasi outfit
def get_outfit_suggestion(category, sub_category, sub_style, outfits_data):
    try:
        return outfits_data[category][sub_category][sub_style]
    except KeyError:
        return None

# Fungsi untuk membuat window wajah (face) 1
def create_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_categories, frame):
    # Face 1: Kategori
    create_label(frame, text="Select Category:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    create_category_radio_buttons(frame, list(outfits_data.keys()), update_sub_categories, category_variable)

# Fungsi untuk membuat window wajah (face) 2
def create_sub_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_styles, frame):
    # Face 2: Subcategory
    def update_sub_styles(*args):
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        if category and sub_category:
            sub_styles = list(outfits_data[category][sub_category].keys())
        else:
            sub_styles = []
        
        # Menghapus radio button lama dan membuat yang baru
        for widget in frame.winfo_children():
            if hasattr(widget, "radio_sub_style"):
                widget.destroy()

        create_radio_button(frame, sub_styles, update_outfit, sub_style_variable)

    create_label(frame, text="Select Subcategory:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    create_radio_button(frame, [], update_sub_styles, sub_category_variable)

# Fungsi untuk membuat window wajah (face) 3
def create_sub_style_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_outfit, frame):
    # Face 3: Sub-style
    create_label(frame, text="Select Sub-Style:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    create_radio_button(frame, [], update_outfit, sub_style_variable)

# Fungsi untuk membuat window wajah (face) 4
def create_outfit_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, frame, update_outfit):
    # Face 4: Outfit Suggestion
    def update_outfit_inner():
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        sub_style = sub_style_variable.get()

        if category and sub_category and sub_style:
            outfit = get_outfit_suggestion(category, sub_category, sub_style, outfits_data)
            if outfit:
                create_label(frame, text=f"Recommended Outfit: {outfit}", font=("Arial", 12), fg="#333333", bg="#f2f2f2", pady=20)
                show_image(frame, outfit)  # Tampilkan gambar outfit
            else:
                messagebox.showwarning("Warning", "No outfit found for the selected options.")
        else:
            messagebox.showwarning("Warning", "Please select all options.")

    create_button(frame, text="Get Outfit", font=("Arial", 14), bg="#ff6f61", fg="white", command=update_outfit_inner, pady=10)

# Fungsi untuk membuat window utama
def create_window(outfits_data):
    # Inisialisasi window utama
    window = tk.Tk()
    window.title("My Outfit Advisor")
    window.geometry("800x600")
    window.config(bg="#f2f2f2")  # Warna pastel

    # Header
    create_label(window, text="My Outfit Advisor", font=("Arial", 24, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=20)

    # Variabel untuk kategori dan subkategori
    category_variable = tk.StringVar()
    sub_category_variable = tk.StringVar()
    sub_style_variable = tk.StringVar()

    # Create frames for each face
    frame_category = tk.Frame(window, bg="#f2f2f2")
    frame_sub_category = tk.Frame(window, bg="#f2f2f2")
    frame_sub_style = tk.Frame(window, bg="#f2f2f2")
    frame_outfit = tk.Frame(window, bg="#f2f2f2")

    # Add all frames to the window
    frame_category.pack(fill="both", expand=True)
    frame_sub_category.pack(fill="both", expand=True)
    frame_sub_style.pack(fill="both", expand=True)
    frame_outfit.pack(fill="both", expand=True)

    # Function to raise frames based on the steps
    def raise_frame(frame):
        frame.tkraise()

    # Define the update_sub_categories function here
    def update_sub_categories(*args):
        category = category_variable.get()
        if category:
            sub_categories = list(outfits_data[category].keys())
        else:
            sub_categories = []
        
        # Menghapus radio button lama dan membuat yang baru
        for widget in frame_category.winfo_children():
            if hasattr(widget, "radio_sub_category"):
                widget.destroy()

        create_radio_button(frame_category, sub_categories, update_sub_styles, sub_category_variable)
        raise_frame(frame_sub_category)  # Switch to sub-category face

    # Define the update_sub_styles function here
    def update_sub_styles(*args):
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        if category and sub_category:
            sub_styles = list(outfits_data[category][sub_category].keys())
        else:
            sub_styles = []
        
        # Menghapus radio button lama dan membuat yang baru
        for widget in frame_sub_category.winfo_children():
            if hasattr(widget, "radio_sub_style"):
                widget.destroy()

        create_radio_button(frame_sub_category, sub_styles, update_outfit, sub_style_variable)
        raise_frame(frame_sub_style)  # Switch to sub-style face

    # Define the update_outfit function here
    def update_outfit():
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        sub_style = sub_style_variable.get()

        if category and sub_category and sub_style:
            outfit = get_outfit_suggestion(category, sub_category, sub_style, outfits_data)
            if outfit:
                create_label(frame_outfit, text=f"Recommended Outfit: {outfit}", font=("Arial", 12), fg="#333333", bg="#f2f2f2", pady=20)
                show_image(frame_outfit, outfit)  # Tampilkan gambar outfit
            else:
                messagebox.showwarning("Warning", "No outfit found for the selected options.")
        else:
            messagebox.showwarning("Warning", "Please select all options.")
        raise_frame(frame_outfit)  # Switch to outfit suggestion face

    # Call the functions to create faces
    create_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_categories, frame_category)
    create_sub_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_styles, frame_sub_category)
    create_sub_style_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_outfit, frame_sub_style)
    create_outfit_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, frame_outfit, update_outfit)

    # Show the category face first
    raise_frame(frame_category)

    # Menjalankan window utama
    window.mainloop()

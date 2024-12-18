import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Fungsi untuk memuat data dari file JSON
def load_outfits_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get("outfits", [])
    except Exception as e:
        print(f"Error loading file {filepath}: {e}")
        return []


# Fungsi untuk memuat kategori yang dipilih
def load_selected_category(filepath="selected_category.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("selected_category")
    except Exception as e:
        print(f"Error loading selected category: {e}")
        return None


# Fungsi untuk memuat sub-kategori yang dipilih
def load_selected_sub_category(filepath="selected_sub_category.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("selected_sub_category")
    except Exception as e:
        print(f"Error loading selected sub-category: {e}")
        return None


# Fungsi untuk memuat gaya yang dipilih
def load_selected_style(filepath="selected_style.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("selected_style")
    except Exception as e:
        print(f"Error loading selected style: {e}")
        return None


# Fungsi untuk menyimpan sub-gaya yang dipilih
def save_selected_sub_style(sub_style, filepath="selected_sub_style.json"):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump({"selected_sub_style": sub_style}, file)
        print(f"Sub-Style '{sub_style}' saved successfully.")
    except Exception as e:
        print(f"Error saving selected sub style: {e}")


def on_exit(root):
    """Handle application exit with confirmation dialog."""
    confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit the application?")
    if confirm:
        root.quit()  # Close the application


# Fungsi untuk mengambil nilai unik dari data JSON
def get_unique_values(data, key):
    unique_values = sorted({item.get(key) for item in data if key in item})
    return unique_values


# Fungsi untuk memfilter data berdasarkan gaya yang dipilih
def filter_data_by_style(data, style):
    return [item for item in data if item.get("style") == style]


# Fungsi untuk menampilkan gambar berdasarkan sub-gaya
def display_image_for_sub_style(data, root, sub_style):
    # Hapus widget yang ada
    for widget in root.winfo_children():
        widget.destroy()

    # Filter data berdasarkan sub-gaya
    filtered_data = [item for item in data if item.get("sub_style") == sub_style]
    if not filtered_data:
        tk.Label(root, text="No images available for this sub-style.", font=("Arial", 14), bg="#CCC0A9").pack(pady=20)
        return

    # Ambil path gambar
    image_path = filtered_data[0].get("image_path", f"images/{sub_style}.jpeg")

    try:
        # Buka dan ubah ukuran gambar
        img = Image.open(image_path)
        img = img.resize((550, 550))
        img_tk = ImageTk.PhotoImage(img)

        # Frame untuk gambar
        frame = tk.Frame(root, bg="#CCC0A9")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=f"This is your outfit: {sub_style}", font=("Arial", 16, "bold"), bg="#CCC0A9").pack(pady=10)
        label = tk.Label(frame, image=img_tk, bg="#CCC0A9")
        label.image = img_tk
        label.pack(pady=10)

        # Tombol keluar
        exit_button = tk.Button(
            frame, text="Exit Aplikasi", font=("Arial", 14), bg="#ff6666", fg="white", command=lambda: on_exit(root)
        )
        exit_button.pack(pady=10)

    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        tk.Label(root, text=f"Error loading image: {e}", font=("Arial", 14), bg="#CCC0A9", fg="red").pack(pady=20)


# Fungsi untuk membuat frame sub-gaya
def create_sub_style_frame(data, root, selected_category, selected_sub_category, selected_style):
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Latar belakang
    canvas = tk.Canvas(frame, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)

    try:
        bg_image = ImageTk.PhotoImage(Image.open("images/background4.jpeg").resize(
            (root.winfo_screenwidth(), root.winfo_screenheight())))
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        frame.bg_image = bg_image  # Simpan referensi agar tidak dihapus GC
    except Exception as e:
        print(f"Error loading background image: {e}")

    # Tombol untuk setiap sub-gaya
    sub_styles = get_unique_values(data, "sub_style")
    for idx, sub_style in enumerate(sub_styles):
        btn = tk.Button(
            frame,
            text=sub_style,
            font=("Arial", 14),
            bg="#C6C09C",
            fg="white",
            command=lambda sub=sub_style: display_image_for_sub_style(data, root, sub)
        )
        canvas.create_window(600, 200 + idx * 50, window=btn)

    # Tombol keluar
    exit_button = tk.Button(
        frame, text="Exit Aplikasi", font=("Arial", 14), bg="#ff6666", fg="white", command=lambda: on_exit(root)
    )
    canvas.create_window(600, 250 + len(sub_styles) * 50, window=exit_button)


# Fungsi utama
def main():
    selected_category = load_selected_category()
    selected_sub_category = load_selected_sub_category()
    selected_style = load_selected_style()

    if not selected_category or not selected_sub_category or not selected_style:
        print("Error: No selected category, sub-category, or style found.")
        return

    outfits_data = load_outfits_data("data.json")
    if not outfits_data:
        print("Error: No data loaded.")
        return

    filtered_data = filter_data_by_style(outfits_data, selected_style)
    if not filtered_data:
        print(f"No sub-styles found for style: {selected_style}")
        return

    root = tk.Tk()
    root.title("Outfit Selection")
    root.geometry("1920x1080")
    root.config(bg="#CCC0A9")

    create_sub_style_frame(filtered_data, root, selected_category, selected_sub_category, selected_style)
    root.mainloop()


if __name__ == "__main__":
    main()

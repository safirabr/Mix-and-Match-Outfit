import json
import tkinter as tk
from gui.widgets import create_button, create_label
from gui.image import show_image
import os


def load_outfits_data(filepath):
    """Load outfit data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if "outfits" in data and isinstance(data["outfits"], list):
            print(f"Loaded {len(data['outfits'])} outfits.")  # Debug log
            return data["outfits"]
        else:
            raise ValueError("Invalid data format in JSON file. Expected a key 'outfits' with a list value.")
    except Exception as e:
        print(f"Error loading file {filepath}: {e}")
        return []


def get_unique_values(data, key):
    """Extract unique values for a specific key from the outfit data."""
    return sorted(set(item[key] for item in data if key in item))


def get_filtered_values(data, filters):
    """Filter values based on multiple criteria."""
    filtered = data
    for key, value in filters.items():
        if value:
            filtered = [item for item in filtered if item.get(key) == value]
    return filtered


def create_window(outfits_data):
    """Create the main GUI window."""
    window = tk.Tk()
    window.title("Outfit Advisor")
    window.geometry("800x600")
    window.config(bg="#f2f2f2")

    # Variables to store user selections
    selected_category = tk.StringVar()
    selected_sub_category = tk.StringVar()
    selected_style = tk.StringVar()
    selected_sub_style = tk.StringVar()

    # Frames for each face
    frame_home = tk.Frame(window, bg="#f2f2f2")
    frame_category = tk.Frame(window, bg="#f2f2f2")
    frame_sub_category = tk.Frame(window, bg="#f2f2f2")
    frame_style = tk.Frame(window, bg="#f2f2f2")
    frame_sub_style = tk.Frame(window, bg="#f2f2f2")
    frame_result = tk.Frame(window, bg="#f2f2f2")

    # Pack all frames
    for frame in [frame_home, frame_category, frame_sub_category, frame_style, frame_sub_style, frame_result]:
        frame.pack(fill="both", expand=True)

    def show_frame(frame):
        frame.tkraise()

    # Home Frame
    def setup_home():
        for widget in frame_home.winfo_children():
            widget.destroy()
        create_label(frame_home, text="Welcome to Outfit Advisor", font=("Arial", 24, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=20)
        tk.Button(frame_home, text="Start", font=("Arial", 14), bg="#33b5b5", fg="white",
                  command=start_button_pressed).pack(pady=50)

    def start_button_pressed():
        """Fungsi untuk memindahkan ke frame kategori setelah tombol Start ditekan"""
        window.destroy()  # Menutup window lama
        create_category_window()  # Membuka window baru yang menampilkan kategori

    # Category Window (window baru setelah start button ditekan)
    def create_category_window():
        """Membuka window kategori setelah tombol Start ditekan"""
        category_window = tk.Tk()
        category_window.title("Select Category")
        category_window.geometry("800x600")
        category_window.config(bg="#f2f2f2")

        categories = get_unique_values(outfits_data, "category")
        create_label(category_window, text="Select a Category", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(category_window, categories, command=select_category)

        category_window.mainloop()

    def select_category(category):
        selected_category.set(category)
        print(f"Selected Category: {category}")  # Debug
        setup_sub_category()
        show_frame(frame_sub_category)

    # Sub-Category Frame
    def setup_sub_category():
        sub_categories = get_unique_values(
            get_filtered_values(outfits_data, {"category": selected_category.get()}), "sub_category"
        )
        create_label(frame_sub_category, text="Select a Sub-Category", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_sub_category, sub_categories, command=select_sub_category)

    def select_sub_category(sub_category):
        selected_sub_category.set(sub_category)
        print(f"Selected Sub-Category: {sub_category}")  # Debug
        setup_style()
        show_frame(frame_style)

    # Style Frame
    def setup_style():
        styles = get_unique_values(
            get_filtered_values(outfits_data, {
                "category": selected_category.get(),
                "sub_category": selected_sub_category.get()
            }), "style"
        )
        create_label(frame_style, text="Select a Style", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_style, styles, command=select_style)

    def select_style(style):
        selected_style.set(style)
        print(f"Selected Style: {style}")  # Debug
        setup_sub_style()
        show_frame(frame_sub_style)

    # Sub-Style Frame
    def setup_sub_style():
        sub_styles = get_unique_values(
            get_filtered_values(outfits_data, {
                "category": selected_category.get(),
                "sub_category": selected_sub_category.get(),
                "style": selected_style.get()
            }), "sub_style"
        )
        create_label(frame_sub_style, text="Select a Sub-Style", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_sub_style, sub_styles, command=select_sub_style)

    def select_sub_style(sub_style):
        selected_sub_style.set(sub_style)
        print(f"Selected Sub-Style: {sub_style}")  # Debug
        show_result()

    # Result Frame
    def show_result():
        filters = {
            "category": selected_category.get(),
            "sub_category": selected_sub_category.get(),
            "style": selected_style.get(),
            "sub_style": selected_sub_style.get(),
        }
        outfit = get_filtered_values(outfits_data, filters)
        for widget in frame_result.winfo_children():
            widget.destroy()
        if outfit:
            outfit = outfit[0]
            create_label(frame_result, text=f"Selected Outfit: {outfit['sub_style']}",
                         font=("Arial", 16), fg="#333333", bg="#f2f2f2", pady=10)
            if os.path.exists(outfit['image']):
                show_image(frame_result, outfit['image'])
            else:
                create_label(frame_result, text="Image not found.", font=("Arial", 12), fg="red", bg="#f2f2f2", pady=5)
        else:
            create_label(frame_result, text="No outfit found.", font=("Arial", 12), fg="red", bg="#f2f2f2", pady=5)
        tk.Button(frame_result, text="Home", font=("Arial", 14), bg="#33b5b5", fg="white",
                  command=lambda: show_frame(frame_home)).pack(pady=20)

    # Initialize Home Frame
    setup_home()
    show_frame(frame_home)

    window.mainloop()


# Main execution
if __name__ == "__main__":
    filepath = "data.json"  # Path to the JSON file
    outfits_data = load_outfits_data(filepath)
    create_window(outfits_data)

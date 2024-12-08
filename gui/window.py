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

def create_dynamic_buttons(parent, options, window ,command):
    """
    Create a set of buttons dynamically based on the given options.
    Each button will trigger the provided command with its respective option.

    :param parent: The parent widget where the buttons will be placed.
    :param options: A list of options to create buttons for.
    :param command: The function to call when a button is clicked, with the option as an argument.
    """
    for widget in parent.winfo_children():
        widget.destroy()  # Clear previous buttons if any

    for option in options:
        tk.Button(
            parent,
            text=option,
            font=("Arial", 14),
            bg="#33b5b5",
            fg="white",
            command=lambda opt=option: command(window, opt)  # Pass the option as an argument
        ).pack(pady=5)


def get_filtered_values(data, filters):
    filtered = data
    for key, value in filters.items():
        if value:
            filtered = [item for item in filtered if item.get(key) == value]
    print(f"Filters applied: {filters}")  # Debug
    print(f"Filtered data: {filtered}")  # Debug
    return filtered

def get_unique_values(data, key):
    values = sorted(set(item[key] for item in data if key in item))
    print(f"Unique values for {key}: {values}")  # Debug
    return values


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
        create_dynamic_buttons(category_window, categories, category_window, create_sub_category_window)

        category_window.mainloop()
    
    def setup_category():
        for widget in frame_home.winfo_children():
            widget.destroy()
        categories = get_unique_values(
            get_filtered_values(outfits_data, {"category": selected_category.get()}), "category"
        )
        create_label(frame_category, text="Select a Category", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_category, categories, command=selected_category)

    def select_category(category):
        selected_category.set(category)
        print(f"Selected Category: {category}")  # Debug
        setup_sub_category()
        show_frame(frame_sub_category)

    def select_category_dynamic_button_pressed():
        """Fungsi untuk memindahkan ke frame kategori setelah tombol select_category ditekan"""
        window.destroy()  # Menutup window lama
        create_sub_category_window()  # Membuka window baru yang menampilkan kategori
    

    # Sub Category Window (window baru setelah select_category_button ditekan)
    def create_sub_category_window(window, opt):
        window.destroy()
        """Membuka window sub kategori setelah tombol select_category_button ditekan"""
        sub_category_window = tk.Tk()
        sub_category_window.title("Select Sub Category")
        sub_category_window.geometry("800x600")
        sub_category_window.config(bg="#f2f2f2")

        sub_categories = get_unique_values(outfits_data, "sub_category")
        create_label(sub_category_window, text="Select a Sub Category", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(sub_category_window, sub_categories, sub_category_window, select_style)

        sub_category_window.mainloop()
        
    def setup_sub_category():
        for widget in frame_category.winfo_children():
            widget.destroy()
        sub_categories = get_unique_values(
            get_filtered_values(outfits_data, {"sub_category": selected_sub_category.get()}), "sub_category"
        )
        create_label(frame_sub_category, text="Select a Sub-Category", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_sub_category, sub_categories, command=select_sub_category)

    def select_sub_category(sub_category):
        selected_sub_category.set(sub_category)
        print(f"Selected Sub Category: {sub_category}")  # Debug
        setup_sub_category()
        show_frame(frame_style)
    
    def select_sub_category_dynamic_button_pressed():
        """Fungsi untuk memindahkan ke frame sub kategori setelah tombol select_sub_category ditekan"""
        window.destroy()  # Menutup window lama
        create_style_window()  # Membuka window baru yang menampilkan kategori

    # Style Frame
    # Category Window (window baru setelah select_sub_category_dynamic_button ditekan)
    def create_style_window(window, opt):
        """Membuka window style setelah tombol select_sub_category_dynamic_button ditekan"""
        style_window = tk.Tk()
        style_window.title("Select Style")
        style_window.geometry("800x600")
        style_window.config(bg="#f2f2f2")

        styles = get_unique_values(outfits_data, "style")
        create_label(style_window, text="Select a Style", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(style_window, styles, style_window, create_sub_style_window)

        style_window.mainloop()
        
    def setup_style():
        for widget in frame_sub_category.winfo_children():
            widget.destroy()
        styles = get_unique_values(
            get_filtered_values(outfits_data, {"style": selected_style.get()}), "style"
        )
        create_label(frame_style, text="Select a Style", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_style, styles, command=selected_style)

    def select_style(style):
        selected_style.set(style)
        print(f"Selected Style: {style}")  # Debug
        setup_sub_style()
        show_frame(frame_sub_style)
    
    def select_style_dynamic_button_pressed():
        """Fungsi untuk memindahkan ke frame sub style setelah tombol select_sub_style ditekan"""
        window.destroy()  # Menutup window lama
        create_sub_style_window()  # Membuka window baru yang menampilkan sub style

    # Sub-Style Frame
    def create_sub_style_window(window, opt):
        """Membuka window sub style setelah tombol select_style_dynamic_button ditekan"""
        sub_style_window = tk.Tk()
        sub_style_window.title("Select Category")
        sub_style_window.geometry("800x600")
        sub_style_window.config(bg="#f2f2f2")

        sub_styles = get_unique_values(outfits_data, "sub_style")
        create_label(sub_style_window, text="Select a Sub Style", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(sub_style_window, sub_styles, sub_style_window, show_result)

        sub_style_window.mainloop()
    
    def setup_sub_style():
        for widget in frame_style.winfo_children():
            widget.destroy()
        sub_styles = get_unique_values(
            get_filtered_values(outfits_data, {"sub_style": selected_sub_style.get()}), "sub_style"
        )
        create_label(frame_sub_style, text="Select a Sub-Style", font=("Arial", 16, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=10)
        create_dynamic_buttons(frame_sub_style, sub_styles, command=selected_sub_style)

    def select_sub_style(sub_style):
        selected_sub_style.set(sub_style)
        print(f"Selected Sub-Style: {sub_style}")  # Debug
        setup_result()
        show_frame(frame_result)
        
    def select_sub_style_dynamic_button_pressed():
        """Fungsi untuk memindahkan ke frame result setelah tombol select_sub_style ditekan"""
        window.destroy()  # Menutup window lama
        show_result()  # Membuka window baru yang menampilkan result

    # Result Frame
    
    def setup_result():
        results = get_unique_values(
            get_filtered_values(outfits_data, {"image": selected_sub_style.get()})
        )
        
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
    filepath = "data.json"  # Path to the JSON file
    outfits_data = load_outfits_data(filepath)
    window.mainloop()


# Main execution
if __name__ == "_main_":
    filepath = "data.json"  # Path to the JSON file
    outfits_data = load_outfits_data(filepath)
    create_window(outfits_data)
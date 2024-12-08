import json
import tkinter as tk
from PIL import Image, ImageTk


def load_outfits_data(filepath):
    """Load outfit data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if "outfits" in data and isinstance(data["outfits"], list):
            print(f"Loaded outfits: {data['outfits']}")  # Debug
            return data["outfits"]
        else:
            raise ValueError("Invalid data format in JSON file. Expected a key 'outfits' with a list value.")
    except Exception as e:
        print(f"Error loading file {filepath}: {e}")
        return []


def load_selected_category():
    """Load the selected category from a JSON file."""
    try:
        with open("selected_category.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Loaded selected category: {data.get('selected_category')}")  # Debug
        return data.get("selected_category")
    except Exception as e:
        print(f"Error loading selected category: {e}")
        return None


def load_selected_sub_category():
    """Load the selected sub-category from a JSON file."""
    try:
        with open("selected_sub_category.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Loaded selected sub-category: {data.get('selected_sub_category')}")  # Debug
        return data.get("selected_sub_category")
    except Exception as e:
        print(f"Error loading selected sub-category: {e}")
        return None


def load_selected_style():
    """Load the selected style from a JSON file."""
    try:
        with open("selected_style.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Loaded selected style: {data.get('selected_style')}")  # Debug
        return data.get("selected_style")
    except Exception as e:
        print(f"Error loading selected style: {e}")
        return None


def save_selected_sub_style(sub_style):
    """Save the selected sub style to a JSON file."""
    try:
        with open("selected_sub_style.json", "w", encoding="utf-8") as file:
            json.dump({"selected_sub_style": sub_style}, file)
        print(f"Sub-Style '{sub_style}' saved successfully.")  # Debug
    except Exception as e:
        print(f"Error saving selected sub style: {e}")


def get_unique_values(data, key):
    """Extract unique values for a specific key from the filtered data."""
    unique_values = sorted({item.get(key) for item in data if key in item and item.get(key)})
    print(f"Unique values for key '{key}': {unique_values}")  # Debug
    return unique_values


def filter_data_by_style(data, style):
    """Filter data based on the selected style."""
    filtered = [item for item in data if item.get("style") == style]
    if not filtered:
        print(f"No data found for style '{style}'")
    return filtered


def display_image_for_sub_style(data, root, sub_style):
    """Display images based on the selected sub-style."""
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Filter data for the selected sub-style
    filtered_data = [item for item in data if item.get("sub_style") == sub_style]
    if not filtered_data:
        print(f"No images found for sub-style: {sub_style}")
        tk.Label(root, text="No images available for this sub-style.", font=("Arial", 14), bg="#CCC0A9").pack(pady=20)
        return

    # Get the image path
    image_path = filtered_data[0].get("image_path", f"images/{sub_style}.jpeg")

    print(f"Loading image from path: {image_path}")  # Debugging log

    try:
        # Open and resize the image
        img = Image.open(image_path)
        img = img.resize((400, 400))  # Adjust size as needed
        img_tk = ImageTk.PhotoImage(img)

        # Display the image
        frame = tk.Frame(root, bg="#CCC0A9")
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text=f"Sub-Style: {sub_style}",
            font=("Arial", 16, "bold"),
            bg="#CCC0A9",
            fg="#C6C09C"
        ).pack(pady=20)

        label = tk.Label(frame, image=img_tk, bg="#CCC0A9")
        label.image = img_tk  # Keep a reference to avoid garbage collection
        label.pack(pady=10)

    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        tk.Label(root, text=f"Failed to load image: {e}", font=("Arial", 14), bg="#CCC0A9", fg="red").pack(pady=20)
def display_image_for_sub_style(data, root, sub_style):
    """Display images based on the selected sub-style."""
    # Hapus widget yang ada
    for widget in root.winfo_children():
        widget.destroy()

    # Filter data untuk sub-style yang dipilih
    filtered_data = [item for item in data if item.get("sub_style") == sub_style]
    if not filtered_data:
        print(f"No images found for sub-style: {sub_style}")
        tk.Label(root, text="No images available for this sub-style.", font=("Arial", 14), bg="#CCC0A9").pack(pady=20)
        return

    # Ambil path gambar
    image_path = filtered_data[0].get("image_path", f"images/{sub_style}.jpeg")

    print(f"Loading image from path: {image_path}")  # Debugging log

    try:
        # Buka dan ubah ukuran gambar
        img = Image.open(image_path)
        img = img.resize((400, 400))  # Sesuaikan ukuran gambar
        img_tk = ImageTk.PhotoImage(img)

        # Tampilkan frame untuk gambar
        frame = tk.Frame(root, bg="#CCC0A9")
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text=f"Sub-Style: {sub_style}",
            font=("Arial", 16, "bold"),
            bg="#CCC0A9",
            fg="#C6C09C"
        ).pack(pady=20)

        label = tk.Label(frame, image=img_tk, bg="#CCC0A9")
        label.image = img_tk  # Simpan referensi untuk mencegah garbage collection
        label.pack(pady=10)

        # Tombol kembali untuk kembali ke frame sub-style
        tk.Button(
            frame,
            text="Back",
            font=("Arial", 14),
            bg="#C6C09C",
            fg="white",
            command=lambda: create_sub_style_frame(data, root, load_selected_category(), load_selected_sub_category(), load_selected_style())
        ).pack(pady=10)

    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        tk.Label(root, text=f"Failed to load image: {e}", font=("Arial", 14), bg="#CCC0A9", fg="red").pack(pady=20)




def create_sub_style_frame(data, root, selected_category, selected_sub_category, selected_style):
    """Create a frame with sub-style buttons dynamically and use an image as the background."""
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Create Canvas for the background image
    canvas = tk.Canvas(frame, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)

    try:
        # Load and resize the background image
        image = Image.open("images/background4.jpeg")  # Path to background image
        bg_image = ImageTk.PhotoImage(image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        # Keep a reference to avoid garbage collection
        frame.bg_image = bg_image
    except Exception as e:
        print(f"Error loading image: {e}")

    # Create header label
    canvas.create_text(
        400, 50,
        text=f"Category: {selected_category} | Sub-Category: {selected_sub_category} | Style: {selected_style}",
        font=("Arial", 16, "bold"),
        fill="#C6C09C"
    )

    # Get unique sub-styles
    sub_styles = get_unique_values(data, "sub_style")

    # Function to handle sub-style selection
    def on_sub_style_selected(sub_style):
        print(f"Sub-Style selected: {sub_style}")
        display_image_for_sub_style(data, root, sub_style)  # Display image and save sub-style

    # Create buttons for each sub-style and place them on the canvas
    for idx, sub_style in enumerate(sub_styles):
        btn = tk.Button(
            frame,
            text=sub_style,
            font=("Arial", 14),
            bg="#C6C09C",
            fg="white",
            command=lambda sub=sub_style: on_sub_style_selected(sub)
        )
        canvas.create_window(400, 100 + idx * 50, window=btn)  # Position the button dynamically

    # Create the "Exit Aplikasi" button
    def exit_application():
        root.quit()  # Close the Tkinter window

    exit_button = tk.Button(
        frame,
        text="Exit Aplikasi",
        font=("Arial", 14),
        bg="#ff6666",
        fg="white",
        command=exit_application
    )
    canvas.create_window(400, 100 + len(sub_styles) * 50 + 20, window=exit_button)  # Position the exit button

    return frame


def main():
    """Main function to create the Tkinter app and load sub-style frame."""
    # Load selected category, sub-category, and style
    selected_category = load_selected_category()
    selected_sub_category = load_selected_sub_category()
    selected_style = load_selected_style()

    if not selected_category or not selected_sub_category or not selected_style:
        print("Error: No selected category, sub-category, or style found.")
        return

    # Load data
    filepath = "data.json"  # Adjust to your JSON file path
    outfits_data = load_outfits_data(filepath)

    if not outfits_data:
        print("Error: No data loaded.")
        return

    # Filter data by selected style
    filtered_data = filter_data_by_style(outfits_data, selected_style)

    if not filtered_data:
        print(f"No sub-styles found for style: {selected_style}")
        return

    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Sub-Style Frame")
    root.geometry("800x600")
    root.config(bg="#CCC0A9")

    # Create sub-style frame
    create_sub_style_frame(filtered_data, root, selected_category, selected_sub_category, selected_style)
    
    # Add a "Close" button to allow the user to close the window manually
    close_button = tk.Button(create_sub_style_frame, text="Close", command=root.quit, font=("Arial", 14), bg="#C6C09C", fg="white")
    close_button.pack(pady=10)


    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()

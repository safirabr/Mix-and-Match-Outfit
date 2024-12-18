import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk

def load_outfits_data(filepath):
    """Load outfit data from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if "outfits" in data and isinstance(data["outfits"], list):
            return data["outfits"]
        else:
            raise ValueError("Invalid data format in JSON file. Expected a key 'outfits' with a list value.")
    except Exception as e:
        print(f"Error loading file {filepath}: {e}")
        return []

def get_unique_values(data, key):
    """Extract unique values for a specific key from the outfit data."""
    return sorted(set(item[key] for item in data if key in item))

def save_selected_category(category):
    """Save the selected category to a JSON file."""
    try:
        with open("selected_category.json", "w", encoding="utf-8") as file:
            json.dump({"selected_category": category}, file)
        print(f"Category '{category}' saved successfully.")  # Debug
    except Exception as e:
        print(f"Error saving selected category: {e}")

def on_exit(root):
    """Handle application exit with confirmation dialog."""
    confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit the application?")
    if confirm:
        root.quit()  # Close the application

def create_category_frame(data, root):
    """Create a frame with category buttons dynamically and use an image as the background."""
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Create Canvas for the background image
    canvas = tk.Canvas(frame, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)

    try:
        image = Image.open("images/background1.jpeg")  # Specify the image path here
        bg_image = ImageTk.PhotoImage(image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        # Keep a reference to avoid garbage collection
        frame.bg_image = bg_image
    except Exception as e:
        print(f"Error loading image: {e}")

    # Create Category Label
    tk.Label(frame, text="Select a Category", font=("Arial", 16, "bold"), fg="#33b5b5").pack(pady=20)

    categories = get_unique_values(data, "category")

    def on_category_selected(category):
        save_selected_category(category)
        root.destroy()

    # Create buttons for each category and place them on the canvas
    for category in categories:
        btn = tk.Button(
            frame,
            text=category,
            font=("Arial", 14),
            bg="#33b5b5",
            fg="white",
            command=lambda cat=category: on_category_selected(cat)
        )
        canvas.create_window(600, 150 + categories.index(category) * 60, window=btn)  # Position the button

    # Exit Button with Confirmation
    exit_btn = tk.Button(
        frame,
        text="Exit Aplikasi",
        font=("Arial", 14),
        bg="#ff6666",
        fg="white",
        command=lambda: on_exit(root)  # Call the on_exit function for confirmation
    )
    canvas.create_window(600, 350, window=exit_btn)  # Place the Exit button in the canvas

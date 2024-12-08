import json
import tkinter as tk
from gui.category import create_category_frame, load_outfits_data


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
            data_selected = json.load(file)
        print(f"Loaded selected category: {data_selected.get('selected_category')}")  # Debug
        return data_selected.get("selected_category")
    except Exception as e:
        print(f"Error loading selected category: {e}")
        return None


def save_selected_sub_category(sub_category):
    """Save the selected sub-category to a JSON file."""
    try:
        with open("selected_sub_category.json", "w", encoding="utf-8") as file:
            json.dump({"selected_sub_category": sub_category}, file)
        print(f"Sub-Category '{sub_category}' saved successfully.")  # Debug
    except Exception as e:
        print(f"Error saving selected sub-category: {e}")

def get_unique_values(data, key):
    """Extract unique values for a specific key from the outfit data."""
    return sorted(set(item[key] for item in data if key in item))

def filter_data_by_category(data, category):
    """Filter data based on the selected category."""
    filtered = [item for item in data if item.get("category") == category]
    print(f"Filtered data for category '{category}': {filtered}")  # Debug
    return filtered


import tkinter as tk
from PIL import Image, ImageTk

def create_sub_category_frame(data, root, selected_category):
    """Create a frame with sub-category buttons dynamically and use an image as the background."""
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Create Canvas for the background image
    canvas = tk.Canvas(frame, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)

    try:
        image = Image.open("images/background2.jpeg")  # Specify the image path here
        bg_image = ImageTk.PhotoImage(image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        # Keep a reference to avoid garbage collection
        frame.bg_image = bg_image
    except Exception as e:
        print(f"Error loading image: {e}")

    # Header Label
    tk.Label(
        frame,
        text=f"Category: {selected_category}",
        font=("Arial", 16, "bold"),
        bg="#CCC0A9",  # Use a background color that matches the background image
        fg="#C6C09C"
    ).pack(pady=20)

    # Get unique sub-categories
    sub_categories = get_unique_values(data, "sub_category")

    # Function to handle sub-category selection
    def on_sub_category_selected(sub_category):
        save_selected_sub_category(sub_category)  # Save the selected sub-category
        print(f"Sub-Category selected: {sub_category}")
        root.destroy()  # Close the current Tkinter window

    # Create buttons for each sub-category and place them on the canvas
    for sub_category in sub_categories:
        btn = tk.Button(
            frame,
            text=sub_category,
            font=("Arial", 14),
            bg="#C6C09C",
            fg="white",
            command=lambda sub=sub_category: on_sub_category_selected(sub)
        )
        canvas.create_window(600, 100 + sub_categories.index(sub_category) * 60, window=btn)  # Position the button

    # Back button to return to Category window
    def go_back():
        frame.destroy()  # Destroy the current frame
        create_category_frame(data, root)  # Recreate the category frame with all categories

    back_button = tk.Button(
        frame,
        text="Back to Category",
        font=("Arial", 14),
        bg="#ffcc66",
        fg="white",
        command=go_back  # Navigate back to the category frame
    )
    canvas.create_window(600, 400, window=back_button)  # Place the back button

    # Exit button
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
    canvas.create_window(600, 500, window=exit_button)  # Place the Exit button

    return frame

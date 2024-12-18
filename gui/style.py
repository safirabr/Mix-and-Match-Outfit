import json
import tkinter as tk
from tkinter import messagebox
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

def save_selected_style(style):
    """Save the selected style to a JSON file."""
    try:
        with open("selected_style.json", "w", encoding="utf-8") as file:
            json.dump({"selected_style": style}, file)
        print(f"Style '{style}' saved successfully.")  # Debug
    except Exception as e:
        print(f"Error saving selected style: {e}")

def on_exit(root):
    """Handle application exit with confirmation dialog."""
    confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit the application?")
    if confirm:
        root.quit()  # Close the application

def get_unique_values(data, key):
    """Extract unique values for a specific key from the outfit data."""
    return sorted(set(item[key] for item in data if key in item))


def filter_data_by_sub_category(data, sub_category):
    """Filter data based on the selected sub-category."""
    filtered = [item for item in data if item.get("sub_category") == sub_category]
    print(f"Filtered data for sub-category '{sub_category}': {filtered}")  # Debug
    return filtered


def create_style_frame(data, root, selected_category, selected_sub_category):
    """Create a frame with style buttons dynamically and use an image as the background."""
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Create Canvas for the background image
    canvas = tk.Canvas(frame, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)

    try:
        # Load and resize the background image
        image = Image.open("images/background3.jpeg")  # Path to background image
        bg_image = ImageTk.PhotoImage(image.resize((root.winfo_screenwidth(), root.winfo_screenheight())))
        canvas.create_image(0, 0, image=bg_image, anchor="nw")

        # Keep a reference to avoid garbage collection
        frame.bg_image = bg_image
    except Exception as e:
        print(f"Error loading image: {e}")

    
    

    # Get unique styles
    styles = get_unique_values(data, "style")

    # Function to handle style selection
    def on_style_selected(style):
        save_selected_style(style)  # Save the selected style
        print(f"Style selected: {style}")
        root.destroy()  # Close the Tkinter window after saving the style

    # Create buttons for each style and place them on the canvas
    for idx, style in enumerate(styles):
        btn = tk.Button(
            frame,
            text=style,
            font=("Arial", 10),
            bg="#C6C09C",
            fg="white",
            command=lambda st=style: on_style_selected(st)
        )
        canvas.create_window(600, 160 + idx * 40, window=btn)  # Position the button dynamically

    # Create the "Exit Aplikasi" button
    def exit_application():
        root.quit()  # Close the Tkinter window

    exit_btn = tk.Button(
    frame,
    text="Exit Aplikasi",
    font=("Arial", 14),
    bg="#ff6666",
    fg="white",
    command=lambda: on_exit(root)
)

    canvas.create_window(600, 120, window=exit_btn)  # Position the exit button

    return frame


def main():
    """Main function to create the Tkinter app and load style frame."""
    # Load selected category and sub-category
    selected_category = load_selected_category()
    selected_sub_category = load_selected_sub_category()

    if not selected_category or not selected_sub_category:
        print("Error: No selected category or sub-category found.")
        return

    # Load data
    filepath = "data.json"  # Adjust to your JSON file path
    outfits_data = load_outfits_data(filepath)

    if not outfits_data:
        print("Error: No data loaded.")
        return

    # Filter data by selected sub-category
    filtered_data = filter_data_by_sub_category(outfits_data, selected_sub_category)

    if not filtered_data:
        print(f"No styles found for sub-category: {selected_sub_category}")
        return

    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Style Frame")
    root.geometry("1920x1080")
    root.config(bg="#CCC0A9")

    # Create style frame
    create_style_frame(filtered_data, root, selected_category, selected_sub_category)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()

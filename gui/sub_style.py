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
    filtered_data = [item for item in data if item.get("sub_style") == sub_style]
    if not filtered_data:
        print(f"No images found for sub-style: {sub_style}")
        return

    # Load and display the first image for the selected sub-style
    # Assuming the image path is stored as 'image_path' in the filtered data
    # Make sure the image path is correctly constructed
    image_path = filtered_data[0].get("image_path")  # assuming 'image_path' is in the data
    if not image_path:
        # If image path is not available, build the path manually
        image_path = f"images/{sub_style}.jpeg"  # assuming images are stored in the 'images' directory

    if image_path:
        try:
            # Open image with PIL and convert to Tkinter-compatible format
            img = Image.open(image_path)
            img = img.resize((400, 400))  # Resize image to fit the window (optional)
            img_tk = ImageTk.PhotoImage(img)

            # Create a frame to display the image
            frame = tk.Frame(root, bg="#f2f2f2")
            frame.pack(fill="both", expand=True)

            tk.Label(
                frame,
                text=f"Sub-Style: {sub_style}",
                font=("Arial", 16, "bold"),
                bg="#f2f2f2",
                fg="#33b5b5"
            ).pack(pady=20)

            label = tk.Label(frame, image=img_tk, bg="#f2f2f2")
            label.image = img_tk  # Keep a reference to the image
            label.pack(pady=10)

            # Save sub-style selection and exit after displaying the image
            save_selected_sub_style(sub_style)
            # root.after(3000, root.quit)  # Wait 3 seconds and then close the window

        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            return

    else:
        print(f"No image path found for sub-style: {sub_style}")



def create_sub_style_frame(data, root, selected_category, selected_sub_category, selected_style):
    """Create a frame with sub-style buttons dynamically."""
    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(fill="both", expand=True)

    tk.Label(
        frame,
        text=f"Category: {selected_category} | Sub-Category: {selected_sub_category} | Style: {selected_style}",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2",
        fg="#33b5b5"
    ).pack(pady=20)

    sub_styles = get_unique_values(data, "sub_style")

    def on_sub_style_selected(sub_style):
        print(f"Sub-Style selected: {sub_style}")
        display_image_for_sub_style(data, root, sub_style)  # Display image and save sub-style

    for sub_style in sub_styles:
        tk.Button(
            frame,
            text=sub_style,
            font=("Arial", 14),
            bg="#33b5b5",
            fg="white",
            command=lambda sub=sub_style: on_sub_style_selected(sub)
        ).pack(pady=5)

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
    root.config(bg="#f2f2f2")

    # Create sub-style frame
    create_sub_style_frame(filtered_data, root, selected_category, selected_sub_category, selected_style)
    
    # Add a "Close" button to allow the user to close the window manually
    close_button = tk.Button(create_sub_style_frame, text="Close", command=root.quit, font=("Arial", 14), bg="#33b5b5", fg="white")
    close_button.pack(pady=10)


    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
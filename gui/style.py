import json
import tkinter as tk


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

def get_unique_values(data, key):
    """Extract unique values for a specific key from the outfit data."""
    return sorted(set(item[key] for item in data if key in item))


def filter_data_by_sub_category(data, sub_category):
    """Filter data based on the selected sub-category."""
    filtered = [item for item in data if item.get("sub_category") == sub_category]
    print(f"Filtered data for sub-category '{sub_category}': {filtered}")  # Debug
    return filtered


def create_style_frame(data, root, selected_category, selected_sub_category):
    """Create a frame with style buttons dynamically."""
    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(fill="both", expand=True)

    tk.Label(
        frame,
        text=f"Category: {selected_category} | Sub-Category: {selected_sub_category}",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2",
        fg="#33b5b5"
    ).pack(pady=20)

    styles = get_unique_values(data, "style")

    def on_style_selected(style):
        save_selected_style(style)  # Save the selected style
        print(f"Style selected: {style}")
        root.destroy()  # Close the Tkinter window after saving the style

    for style in styles:
        tk.Button(
            frame,
            text=style,
            font=("Arial", 14),
            bg="#33b5b5",
            fg="white",
            command=lambda st=style: on_style_selected(st)
        ).pack(pady=5)

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
    root.geometry("800x600")
    root.config(bg="#f2f2f2")

    # Create style frame
    create_style_frame(filtered_data, root, selected_category, selected_sub_category)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()

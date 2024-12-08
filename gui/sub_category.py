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


def create_sub_category_frame(data, root, selected_category):
    """Create a frame with sub-category buttons dynamically."""
    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(fill="both", expand=True)

    tk.Label(
        frame,
        text=f"Category: {selected_category}",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2",
        fg="#33b5b5"
    ).pack(pady=20)

    sub_categories = get_unique_values(data, "sub_category")

    def on_sub_category_selected(sub_category):
        save_selected_sub_category(sub_category)  # Save the selected sub-category
        print(f"Sub-Category selected: {sub_category}")
        root.destroy()  # Close the current Tkinter window

    for sub_category in sub_categories:
        tk.Button(
            frame,
            text=sub_category,
            font=("Arial", 14),
            bg="#33b5b5",
            fg="white",
            command=lambda sub=sub_category: on_sub_category_selected(sub)
        ).pack(pady=5)

    return frame


def main():
    """Main function to create the Tkinter app and load sub-category frame."""
    # Load selected category
    selected_category = load_selected_category()
    if not selected_category:
        print("Error: No selected category found.")
        return

    # Load data
    filepath = "data.json"  # Adjust to your JSON file path
    outfits_data = load_outfits_data(filepath)

    if not outfits_data:
        print("Error: No data loaded.")
        return

    # Filter data by selected category
    filtered_data = filter_data_by_category(outfits_data, selected_category)

    if not filtered_data:
        print(f"No sub-categories found for category: {selected_category}")
        return

    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Sub-Category Frame")
    root.geometry("800x600")
    root.config(bg="#f2f2f2")

    # Create sub-category frame
    create_sub_category_frame(filtered_data, root, selected_category)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()

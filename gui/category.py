import json
import tkinter as tk


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


def create_category_frame(data, root):
    """Create a frame with category buttons dynamically."""
    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Select a Category", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#33b5b5").pack(pady=20)

    categories = get_unique_values(data, "category")

    def on_category_selected(category):
        save_selected_category(category)
        print(f"Category selected: {category}")
        root.destroy()  # Close the current Tkinter window

    for category in categories:
        tk.Button(
            frame,
            text=category,
            font=("Arial", 14),
            bg="#33b5b5",
            fg="white",
            command=lambda cat=category: on_category_selected(cat)
        ).pack(pady=5)

    return frame


def main():
    """Main function to create the Tkinter app and load category frame."""
    # Load data
    filepath = "data.json"  # Adjust to your JSON file path
    outfits_data = load_outfits_data(filepath)

    if not outfits_data:
        print("Error: No data loaded.")
        return

    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Category Frame")
    root.geometry("1700x1100")
    root.config(bg="#f2f2f2")
    

    # Create category frame
    create_category_frame(outfits_data, root)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()

import os
import tkinter as tk
from gui.category import create_category_frame, load_outfits_data
from gui.sub_category import create_sub_category_frame, load_selected_category, filter_data_by_category
from gui.style import create_style_frame, load_selected_sub_category, filter_data_by_sub_category
from gui.sub_style import create_sub_style_frame, load_selected_style, filter_data_by_style


# def reset_selections():
#     """Delete previously saved selections to start fresh."""
#     for file in ["selected_category.json", "selected_sub_category.json", "selected_style.json"]:
#         if os.path.exists(file):
#             os.remove(file)

def reset_selections():
    """Clear the contents of previously saved selections to start fresh."""
    for file in ["selected_category.json", "selected_sub_category.json", "selected_style.json"]:
        if os.path.exists(file):
            with open(file, "w", encoding="utf-8") as f:
                f.write("{}")  # Clear the file content with an empty JSON object

def main():
    reset_selections()  # Ensure fresh start
    filepath = "data.json"
    outfits_data = load_outfits_data(filepath)

    if not outfits_data:
        print("Error: No outfit data loaded.")
        return

    # Step 1: Select Category
    selected_category = load_selected_category()
    if not selected_category:
        root = tk.Tk()
        root.title("Category")
        root.geometry("1700x1100")
        root.config(bg="#CCC0A9")
        create_category_frame(outfits_data, root)
        root.mainloop()
        # root.dei
        selected_category = load_selected_category()
    if not selected_category:
        print("Error: No category selected. Exiting.")
        return

    # Step 2: Select Sub-Category
    filtered_by_category = filter_data_by_category(outfits_data, selected_category)
    selected_sub_category = load_selected_sub_category()
    if not selected_sub_category:
        root = tk.Tk()
        root.title("Select Sub-Category")
        root.geometry("800x600")
        root.config(bg="#CCC0A9")
        create_sub_category_frame(filtered_by_category, root, selected_category)
        root.mainloop()
        selected_sub_category = load_selected_sub_category()
    if not selected_sub_category:
        print("Error: No sub-category selected. Exiting.")
        return

    # Step 3: Select Style
    filtered_by_sub_category = filter_data_by_sub_category(outfits_data, selected_sub_category)
    selected_style = load_selected_style()
    if not selected_style:
        root = tk.Tk()
        root.title("Select Style")
        root.geometry("800x600")
        root.config(bg="#CCC0A9")
        create_style_frame(filtered_by_sub_category, root, selected_category, selected_sub_category)
        root.mainloop()
        selected_style = load_selected_style()
    if not selected_style:
        print("Error: No style selected. Exiting.")
        return

    # Step 4: Select Sub-Style
    filtered_by_style = filter_data_by_style(outfits_data, selected_style)
    if not filtered_by_style:
        print("Error: No sub-style options available.")
        return
    root = tk.Tk()
    root.title("Select Sub-Style")
    root.geometry("800x600")
    root.config(bg="#CCC0A9")
    create_sub_style_frame(filtered_by_style, root, selected_category, selected_sub_category, selected_style)
    root.mainloop()


if __name__ == "__main__":
    main()




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
    frame = tk.Frame(root, bg="#CCC0A9")
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Select a Category", font=("Arial", 16, "bold"), bg="#CCC0A9", fg="#C6C09C").pack(pady=20, anchor="center")

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
            bg="#C6C09C",
            fg="white",
            command=lambda cat=category: on_category_selected(cat)
        ).pack(pady=5)
    
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
    exit_button.pack(pady=20)

    return frame


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


def create_sub_category_frame(data, root, selected_category):
    """Create a frame with sub-category buttons dynamically."""
    frame = tk.Frame(root, bg="#CCC0A9")
    frame.pack(fill="both", expand=True)

    # Header Label
    tk.Label(
        frame,
        text=f"Category: {selected_category}",
        font=("Arial", 16, "bold"),
        bg="#CCC0A9",
        fg="#C6C09C"
    ).pack(pady=20)

    # Get unique sub-categories
    sub_categories = get_unique_values(data, "sub_category")

    # Function to handle sub-category selection
    def on_sub_category_selected(sub_category):
        save_selected_sub_category(sub_category)  # Save the selected sub-category
        print(f"Sub-Category selected: {sub_category}")
        root.destroy()  # Close the current Tkinter window

    # Create buttons for each sub-category
    for sub_category in sub_categories:
        tk.Button(
            frame,
            text=sub_category,
            font=("Arial", 14),
            bg="#C6C09C",
            fg="white",
            command=lambda sub=sub_category: on_sub_category_selected(sub)
        ).pack(pady=5)

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
    back_button.pack(pady=10)

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
    exit_button.pack(pady=20)

    return frame

import os
import tkinter as tk
from tkinter import messagebox
from gui.category import create_category_frame, load_outfits_data
from gui.sub_category import create_sub_category_frame, load_selected_category, filter_data_by_category
from gui.style import create_style_frame, load_selected_sub_category, filter_data_by_sub_category
from gui.sub_style import create_sub_style_frame, load_selected_style, filter_data_by_style

def reset_selections():
    """Clear the contents of previously saved selections to start fresh."""
    for file in ["selected_category.json", "selected_sub_category.json", "selected_style.json"]:
        if os.path.exists(file):
            with open(file, "w", encoding="utf-8") as f:
                f.write("{}")  # Clear the file content with an empty JSON object

def on_exit(root):
    """Handle application exit with confirmation and closing message."""
    confirm = messagebox.askyesno("Exit", "Hey, are you sure you want to leave?")
    if confirm:
        messagebox.showinfo("Goodbye", "Thank you for visiting My Outfit Advisor! We hope you found the perfect outfit and can’t wait to help you style your next look")
        root.destroy()

def main():
    reset_selections()  # Ensure fresh start
    filepath = "data.json"
    outfits_data = load_outfits_data(filepath)

    if not outfits_data:
        print("Error: No outfit data loaded.")
        return

    # Display welcome message
    messagebox.showinfo("Welcome aboard!", "Hi there! Welcome to My Outfit Advisor—your personal guide to finding the perfect outfit for any occasion")

    # Step 1: Select Category
    selected_category = load_selected_category()
    if not selected_category:
        root = tk.Tk()
        root.title("Category")
        root.geometry("1920x1080")
        root.config(bg="#CCC0A9")
        
        # Set custom exit handler
        root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
        
        create_category_frame(outfits_data, root)
        root.mainloop()  # Wait for user interaction
        selected_category = load_selected_category()  # Reload the selected category after window is closed

    if not selected_category:
        print("Error: No category selected. Exiting.")
        return

    # Step 2: Select Sub-Category
    filtered_by_category = filter_data_by_category(outfits_data, selected_category)
    selected_sub_category = load_selected_sub_category()
    if not selected_sub_category:
        root = tk.Tk()
        root.title("Select Sub-Category")
        root.geometry("1920x1080")
        root.config(bg="#CCC0A9")
        
        # Set custom exit handler
        root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
        
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
        root.geometry("1920x1080")
        root.config(bg="#CCC0A9")
        
        # Set custom exit handler
        root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
        
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
    root.title("Selected Style")
    root.geometry("1920x1080")
    root.config(bg="#CCC0A9")
    
    # Set custom exit handler
    root.protocol("WM_DELETE_WINDOW", lambda: on_exit(root))
    
    create_sub_style_frame(filtered_by_style, root, selected_category, selected_sub_category, selected_style)
    root.mainloop()


if __name__ == "__main__":
    main()

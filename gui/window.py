import json
import tkinter as tk
from tkinter import messagebox
from gui.widgets import create_button, create_label, create_radio_button, create_category_radio_buttons
from gui.image import show_image
import os
print("Current working directory:", os.getcwd())



def load_outfits_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print("Data loaded successfully:", data)  # Debug print
        return data["outfits"]  # Return the list under "outfits" key
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return []

# Cek hasilnya
filepath = "data.json"
outfits_data = load_outfits_data(filepath)
print(outfits_data)


# Function to get outfit suggestion based on selections
def get_outfit_suggestion(category, sub_category, sub_style, outfits_data):
    for outfit in outfits_data:
        if (outfit["category"] == category and
            outfit["sub_category"] == sub_category and
            outfit["style"] == sub_style):
            return outfit
    return None


# Function to create category selection frame
def create_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_categories, frame):
    create_label(frame, text="Select Category:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    create_category_radio_buttons(frame, list(outfits_data.keys()), update_sub_categories, category_variable)


# Function to create sub-category selection frame
def create_sub_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_styles, frame):
    create_label(frame, text="Select Subcategory:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    create_radio_button(frame, [], update_sub_styles, sub_category_variable)


# Function to create style selection frame
def create_style_selection_frame(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, frame):
    def update_styles(*args):
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        styles = list(outfits_data[category][sub_category].keys()) if category and sub_category else []

        for widget in frame.winfo_children():
            if hasattr(widget, "radio_style"):
                widget.destroy()

        create_radio_button(frame, styles, lambda: None, sub_style_variable)

    # Add label and initialize styles
    create_label(frame, text="Select Style:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    sub_category_variable.trace_add("write", update_styles)  # Trigger update when sub_category changes


# Function to create sub-style selection frame
def create_sub_style_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_outfit, frame):
    create_label(frame, text="Select Sub-Style:", font=("Arial", 14), fg="#33b5b5", bg="#f2f2f2", pady=10)
    create_radio_button(frame, [], update_outfit, sub_style_variable)


# Function to create outfit suggestion frame
def create_outfit_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, frame, update_outfit):
    def update_outfit_inner():
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        sub_style = sub_style_variable.get()

        if category and sub_category and sub_style:
            outfit = get_outfit_suggestion(category, sub_category, sub_style, outfits_data)
            if outfit:
                create_label(frame, text=f"Recommended Outfit: {outfit['sub_style']}", font=("Arial", 12), fg="#333333", bg="#f2f2f2", pady=20)
                show_image(frame, outfit['image'])  # Ensure 'image' field exists
            else:
                messagebox.showwarning("Warning", "No outfit found for the selected options.")
        else:
            messagebox.showwarning("Warning", "Please select all options.")

    create_button(frame, text="Get Outfit", font=("Arial", 14), bg="#ff6f61", fg="white", command=update_outfit_inner, pady=10)


# Function to create the main window
def create_window(outfits_data):
    window = tk.Tk()
    window.title("My Outfit Advisor")
    window.geometry("800x600")
    window.config(bg="#f2f2f2")

    create_label(window, text="My Outfit Advisor", font=("Arial", 24, "bold"), fg="#33b5b5", bg="#f2f2f2", pady=20)

    # Variables to store user selections
    category_variable = tk.StringVar()
    sub_category_variable = tk.StringVar()
    style_variable = tk.StringVar()
    sub_style_variable = tk.StringVar()

    # Create frames for each stage
    frame_category = tk.Frame(window, bg="#f2f2f2")
    frame_sub_category = tk.Frame(window, bg="#f2f2f2")
    frame_style = tk.Frame(window, bg="#f2f2f2")
    frame_sub_style = tk.Frame(window, bg="#f2f2f2")
    frame_outfit = tk.Frame(window, bg="#f2f2f2")

    # Pack frames
    frame_category.pack(fill="both", expand=True)
    frame_sub_category.pack(fill="both", expand=True)
    frame_style.pack(fill="both", expand=True)
    frame_sub_style.pack(fill="both", expand=True)
    frame_outfit.pack(fill="both", expand=True)

    def raise_frame(frame):
        frame.tkraise()

    # Sub-category update function
    def update_sub_categories(*args):
        category = category_variable.get()
        sub_categories = list(outfits_data[category].keys()) if category else []
        print("Sub categories:", sub_categories)  # Debug print

        for widget in frame_category.winfo_children():
            if hasattr(widget, "radio_sub_category"):
                widget.destroy()

        create_radio_button(frame_category, sub_categories, lambda: raise_frame(frame_sub_category), sub_category_variable)

    # Sub-style update function
    def update_sub_styles(*args):
        category = category_variable.get()
        sub_category = sub_category_variable.get()
        sub_styles = list(outfits_data[category][sub_category].keys()) if category and sub_category else []

        for widget in frame_sub_category.winfo_children():
            if hasattr(widget, "radio_sub_style"):
                widget.destroy()

        create_radio_button(frame_sub_category, sub_styles, lambda: raise_frame(frame_sub_style), sub_style_variable)

    # Initialize the frames
    create_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_categories, frame_category)
    create_sub_category_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, update_sub_styles, frame_sub_category)
    create_style_selection_frame(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, frame_style)
    create_sub_style_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, lambda: raise_frame(frame_outfit), frame_sub_style)
    create_outfit_face(window, outfits_data, category_variable, sub_category_variable, sub_style_variable, frame_outfit, lambda: None)

    raise_frame(frame_category)
    window.mainloop()


# Main execution
if __name__ == "__main__":
    filepath = "data.json"  # Path to JSON data
    outfits_data = load_outfits_data(filepath)
    create_window(outfits_data)

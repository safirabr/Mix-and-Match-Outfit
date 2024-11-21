import os
import json
from gui.window import create_window
from data.data_loader import load_data

def load_outfits_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found in {os.getcwd()}.")
        return None

def main():
    # Load data from JSON
    outfits_data = load_outfits_data(filepath)
    if outfits_data is None:
        return  # Exit if data cannot be loaded

    # Create application window
    create_window(outfits_data)

if __name__ == "__main__":
    # Path to JSON file
    filepath = r"data.json"

    # Run GUI
    main()

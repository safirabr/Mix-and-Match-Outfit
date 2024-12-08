import tkinter as tk

def create_button(parent, text, font, bg, fg, command, pady=0):
    """
    Fungsi untuk membuat tombol pada UI.
    """
    button = tk.Button(parent, text=text, font=font, bg=bg, fg=fg, command=command)
    button.pack(pady=pady)

def create_label(parent, text, font, fg, bg, pady=0):
    """
    Fungsi untuk membuat label pada UI.
    """
    label = tk.Label(parent, text=text, font=font, fg=fg, bg=bg)
    label.pack(pady=pady)

def create_radio_button(parent, options, command, variable, widget_tag=None):
    """
    Fungsi untuk membuat grup radio button pada UI dengan kemampuan pembaruan dinamis.
    """
    # Hapus widget lama jika ada
    for widget in parent.winfo_children():
        if widget_tag and hasattr(widget, widget_tag):
            widget.destroy()

    for option in options:
        radio_button = tk.Radiobutton(parent, text=option, variable=variable, value=option, command=command)
        if widget_tag:
            setattr(radio_button, widget_tag, True)  # Tandai widget dengan tag tertentu
        radio_button.pack()

def create_category_radio_buttons(parent, categories, command, variable):
    """
    Fungsi untuk membuat grup radio button untuk kategori.
    """
    for widget in parent.winfo_children():
        if hasattr(widget, "radio_category"):
            widget.destroy()

    for category in categories:
        radio_button = tk.Radiobutton(parent, text=category, variable=variable, value=category, command=command)
        setattr(radio_button, "radio_category", True)  # Tandai widget
        radio_button.pack()

def create_dynamic_buttons(parent, items, command, columns=3):
    """
    Create buttons dynamically for each item in a grid layout.
    :param parent: The parent widget to attach buttons.
    :param items: A list of items for which buttons will be created.
    :param command: The command to execute when a button is clicked. The item will be passed as an argument.
    :param columns: The number of columns in the grid layout.
    """
    for widget in parent.winfo_children():
        widget.destroy()  # Clear existing widgets
    
    row = 0
    col = 0
    for item in items:
        button = tk.Button(
            parent,
            text=item,
            font=("Arial", 12),
            bg="#33b5b5",
            fg="white",
            command=lambda value=item: command(value),
            width=15,  # Set width for uniform button size
            height=2   # Set height for uniform button size
        )
        button.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
        col += 1
        if col >= columns:  # Move to the next row after `columns` buttons
            col = 0
            row += 1


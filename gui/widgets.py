import tkinter as tk

def create_button(parent, text, font, bg, fg, command, pady=0):
    button = tk.Button(parent, text=text, font=font, bg=bg, fg=fg, command=command)
    button.pack(pady=pady)

def create_label(parent, text, font, fg, bg, pady=0):
    label = tk.Label(parent, text=text, font=font, fg=fg, bg=bg)
    label.pack(pady=pady)

def create_radio_button(parent, options, command, variable):
    for option in options:
        radio_button = tk.Radiobutton(parent, text=option, variable=variable, value=option, command=command)
        radio_button.pack()

def create_category_radio_buttons(parent, categories, command, variable):
    for category in categories:
        create_radio_button(parent, [category], command, variable)

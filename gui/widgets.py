import tkinter as tk

def create_button(parent, text, font, bg, fg, command, pady=0):
    """
    Fungsi untuk membuat tombol pada UI.

    Args:
        parent (tk.Widget): Widget parent tempat tombol akan ditambahkan.
        text (str): Teks yang ditampilkan pada tombol.
        font (tuple): Font yang digunakan untuk teks tombol.
        bg (str): Warna latar belakang tombol.
        fg (str): Warna teks tombol.
        command (function): Fungsi yang dipanggil ketika tombol diklik.
        pady (int, optional): Padding vertikal pada tombol. Default 0.
    """
    button = tk.Button(parent, text=text, font=font, bg=bg, fg=fg, command=command)
    button.pack(pady=pady)

def create_label(parent, text, font, fg, bg, pady=0):
    """
    Fungsi untuk membuat label pada UI.

    Args:
        parent (tk.Widget): Widget parent tempat label akan ditambahkan.
        text (str): Teks yang ditampilkan pada label.
        font (tuple): Font yang digunakan untuk teks label.
        fg (str): Warna teks label.
        bg (str): Warna latar belakang label.
        pady (int, optional): Padding vertikal pada label. Default 0.
    """
    label = tk.Label(parent, text=text, font=font, fg=fg, bg=bg)
    label.pack(pady=pady)

def create_radio_button(parent, options, command, variable):
    """
    Fungsi untuk membuat grup radio button pada UI.

    Args:
        parent (tk.Widget): Widget parent tempat radio button akan ditambahkan.
        options (list): Daftar pilihan yang akan menjadi nilai pada radio button.
        command (function): Fungsi yang dipanggil ketika pilihan radio button berubah.
        variable (tk.StringVar): Variabel yang menyimpan nilai yang dipilih.
    """
    for option in options:
        radio_button = tk.Radiobutton(parent, text=option, variable=variable, value=option, command=command)
        radio_button.pack()

def create_category_radio_buttons(parent, categories, command, variable):
    """
    Fungsi untuk membuat grup radio button untuk kategori (tren, preferensi, warna).

    Args:
        parent (tk.Widget): Widget parent tempat radio button akan ditambahkan.
        categories (list): Daftar kategori yang akan menjadi pilihan radio button.
        command (function): Fungsi yang dipanggil ketika kategori berubah.
        variable (tk.StringVar): Variabel yang menyimpan kategori yang dipilih.
    """
    for category in categories:
        create_radio_button(parent, [category], command, variable)

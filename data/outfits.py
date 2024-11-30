def get_outfit_suggestion(style, sub_style, data):
    # Cek apakah style ada di data
    if style in data:
        style_data = data[style]
        if sub_style in style_data:
            return style_data[sub_style]
        else:
            return "Sub style tidak ditemukan"
    else:
        return "style tidak ditemukan"


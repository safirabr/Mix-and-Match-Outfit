def get_outfit_suggestion(category, sub_category, data):
    # Cek apakah kategori ada di data
    if category in data:
        category_data = data[category]
        if sub_category in category_data:
            return category_data[sub_category]
        else:
            return "Subkategori tidak ditemukan"
    else:
        return "Kategori tidak ditemukan"

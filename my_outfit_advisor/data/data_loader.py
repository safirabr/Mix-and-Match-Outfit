import json

def load_data(file_path="data.json"):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

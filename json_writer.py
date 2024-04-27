import json


def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_json(file_path, new_data):
    existing_data = read_json(file_path)

    existing_data.append(new_data)

    write_json(existing_data, file_path)
import json


class DataSaver:
    __file_name = "data.json"

    @staticmethod
    def save_data(data):
        try:
            with open(DataSaver.__file_name, "r") as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = []

        existing_data.extend(data)

        with open(DataSaver.__file_name, "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

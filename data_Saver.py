import json


class DataSaver:
    __file_name = "data.json"

    @staticmethod
    def save_data(data):
        with open(DataSaver.__file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)

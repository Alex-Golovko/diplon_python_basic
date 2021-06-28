import json

class JsonFileProcess:

    def __init__(self):
        pass

    def create_result_file(self, filename):
        result_file = open(filename, 'w', encoding='utf-8')
        return result_file

    def write_into_file(self, file_descriptor, data):
        json.dumps(data, file_descriptor, ensure_ascii=False)

    def close_file(self, file_description):
        file_description.close()

    def read_file(self, filename):
        with open(filename) as data_file:
            data = json.load(data_file)
        return data
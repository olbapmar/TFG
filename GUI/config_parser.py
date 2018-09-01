import json

class ConfigParser:
    @staticmethod
    def parse(file):
        content = json.load(open(file))
        return content
import dirtyjson
import yaml


class Person(object):
    def __init__(self, name, age, phones: list):
        self.name = name
        self.age = age
        self.phones = phones


class PersonFactory:
    def create_from_json(self, file_name) -> Person:
        with open(file_name) as f:
            obj = dirtyjson.load(f)
        phones = [item['number'] for item in obj['contactnumbers']]
        person = Person(obj['name'], obj['age'], phones)
        return person

    def create_from_yaml(self, file_name) -> Person:
        with open(file_name) as f:
            obj0 = yaml.load(f, Loader=yaml.FullLoader)
        obj = obj0[0]
        person = Person(obj['name'], obj['age'], [obj['number']])
        return person


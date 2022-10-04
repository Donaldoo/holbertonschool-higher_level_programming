#!/usr/bin/python3
"""Task 1"""
import json


class Base:
    """New class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string repr of objs to a file"""
        filename = cls.__name__ + ".json"
        dictList = []
        with open(filename, "w") as my_file:
            if list_objs is not None:
                for obj in list_objs:
                    dictList.append(obj.to_dictionary())
            my_file.write(Base.to_json_string(dictList))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attrs set"""
        newInstance = cls(1, 1)
        return newInstance.update(**dictionary)

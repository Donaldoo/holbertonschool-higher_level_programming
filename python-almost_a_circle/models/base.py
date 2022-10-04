#!/usr/bin/python3
"""Task 1"""
import json
from os import path


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
        """returns the list of json string repr"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attrs set"""
        if cls.__name__ == "Rectangle":
            newInstance = cls(1, 1)
        else:
            newInstance = cls(1)
        newInstance.update(**dictionary)
        return newInstance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if path.exists(filename):
            with open(filename, "r") as my_file:
                objList = []
                jsonList = Base.from_json_string(my_file.read())
                for obj in jsonList:
                    objList.append(cls.create(**obj))
                return objList
        else:
            return []

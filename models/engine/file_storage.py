#!/usr/bin/env python
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}  # <class name>.id

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        my_dict = {}
        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    self.__objects[key] = globals()[class_name](**value)

        except FileNotFoundError:
            pass

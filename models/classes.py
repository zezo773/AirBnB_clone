#!/usr/bin/env python3


from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
}

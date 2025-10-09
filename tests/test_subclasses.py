#!/usr/bin/env python3
import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class TestInheritance(unittest.TestCase):
    """Test that all subclasses properly inherit from BaseModel"""

    def test_inheritance(self):
        for cls in [State, City, Amenity, Place, Review]:
            obj = cls()
            self.assertIsInstance(obj, BaseModel)
            self.assertTrue(issubclass(cls, BaseModel))


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_attributes_exist(self):
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")


class TestCity(unittest.TestCase):
    """Tests for the City class"""

    def test_attributes_exist(self):
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_attributes_exist(self):
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def test_attributes_exist(self):
        p = Place()
        attrs = {
            "city_id": "",
            "user_id": "",
            "name": "",
            "description": "",
            "number_rooms": 0,
            "number_bathrooms": 0,
            "max_guest": 0,
            "price_by_night": 0,
            "latitude": 0.0,
            "longitude": 0.0,
            "amenity_ids": [],
        }
        for key, value in attrs.items():
            self.assertTrue(hasattr(p, key))
            self.assertEqual(getattr(p, key), value)


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    def test_attributes_exist(self):
        r = Review()
        attrs = {
            "place_id": "",
            "user_id": "",
            "text": "",
        }
        for key, value in attrs.items():
            self.assertTrue(hasattr(r, key))
            self.assertEqual(getattr(r, key), value)



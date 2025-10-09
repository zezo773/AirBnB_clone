#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Runs before each test"""
        self.model = BaseModel()

    # ---------- TEST INIT ----------
    def test_has_unique_id(self):
        """Each BaseModel should have a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)
        self.assertIsInstance(self.model.id, str)
        # UUID check
        uuid.UUID(self.model.id)

    def test_created_and_updated_are_datetime(self):
        """created_at and updated_at should be datetime objects"""
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test reloading an instance from a dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertNotIn("__class__", new_model.__dict__)

    # ---------- TEST SAVE ----------
    def test_save_updates_updated_at(self):
        """save() should update the 'updated_at' attribute"""
        old_updated_at = self.model.updated_at
        time.sleep(0.001)  # tiny delay to ensure timestamp changes
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    # ---------- TEST TO_DICT ----------
    def test_to_dict_returns_dict(self):
        """to_dict() should return a dictionary"""
        my_dict = self.model.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_to_dict_has_class_name(self):
        """to_dict() should contain __class__ key"""
        my_dict = self.model.to_dict()
        self.assertIn("__class__", my_dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_format(self):
        """created_at and updated_at should be strings in ISO format"""
        my_dict = self.model.to_dict()
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        # Convert back to datetime to verify format
        datetime.fromisoformat(my_dict["created_at"])
        datetime.fromisoformat(my_dict["updated_at"])

    # ---------- TEST STR ----------
    def test_str_representation(self):
        """__str__ should return correct format"""
        output = str(self.model)
        self.assertIn("[BaseModel]", output)
        self.assertIn(self.model.id, output)
        self.assertIn("created_at", output)
        self.assertIn("updated_at", output)

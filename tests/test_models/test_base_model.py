#!/usr/bin/python3
""" Module iwth unittests for BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        """Test that the BaseModel has a unique id"""
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)
        self.assertGreater(len(self.model.id), 0)

    def test_created_at(self):
        """Test that the created_at attribute is set"""
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test that the updated_at attribute is set"""
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test that the __str__ method returns a string"""
        self.assertIsInstance(str(self.model), str)

    def test_save(self):
        """Test that the save method updates the updated_at attribute"""
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary"""
        my_dict = self.model.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIn("__class__", my_dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIn("id", my_dict)
        self.assertEqual(my_dict["id"], self.model.id)
        self.assertIn("created_at", my_dict)
        self.assertEqual(my_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertIn("updated_at", my_dict)
        self.assertEqual(my_dict["updated_at"],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

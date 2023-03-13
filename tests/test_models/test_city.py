#!/usr/bin/python3
""" Module containing unittests for models/city.py."""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_inherits_from_BaseModel(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes_are_strings(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_str_method(self):
        self.assertIsInstance(str(self.city), str)

    def test_to_dict_method(self):
        dict_obj = self.city.to_dict()
        self.assertIsInstance(dict_obj, dict)
        self.assertTrue(hasattr(dict_obj, "__class__"))
        self.assertTrue(hasattr(dict_obj, "created_at"))
        self.assertTrue(hasattr(dict_obj, "updated_at"))
        self.assertTrue(hasattr(dict_obj, "id"))
        self.assertTrue(hasattr(dict_obj, "state_id"))
        self.assertTrue(hasattr(dict_obj, "name"))
        self.assertEqual(dict_obj['__class__'], 'City')

    def tearDown(self):
        del self.city


if __name__ == '__main__':
    unittest.main()

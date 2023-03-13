#!/usr/bin/python3
""" Module containing unittests for models/amenity.py file"""

import unittest
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_is_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_str_representation(self):
        am = Amenity()
        am.id = "123456"
        amstr = str(am)
        self.assertIn("[Amenity] (123456)", amstr)

    def test_instantiation_with_kwargs(self):
        am = Amenity(id="345")
        self.assertEqual(am.id, "345")

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None)


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    def test_one_save(self):
        am = Amenity()
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        am = Amenity()
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)


class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())


if __name__ == '__main__':
    unittest.main()

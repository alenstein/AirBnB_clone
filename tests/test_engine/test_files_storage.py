#!/usr/bin/python3
"""
    Module containing unit tests for the Filestorage class.
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Setup function for testing """
        try:
            self.storage = FileStorage()
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_all(self):
        """ Test the all method """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ Test the new method """
        bm = BaseModel()
        bm.id = 123
        self.storage.new(bm)
        self.assertIn("BaseModel.123", self.storage.all().keys())

    def test_save(self):
        """ Test the save method """
        bm = BaseModel()
        bm.id = 456
        self.storage.new(bm)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertIn("BaseModel.456", data.keys())

    def test_classes(self):
        """ Test the classes method """
        classes = self.storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertIn("BaseModel", classes.keys())
        self.assertIs(classes["BaseModel"], BaseModel)

    def test_reload(self):
        """ Test the reload method """
        bm = BaseModel()
        bm.id = 789
        self.storage.new(bm)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel.789", self.storage.all().keys())

    def test_attributes(self):
        """ Test the attributes method """
        attributes = self.storage.attributes()
        self.assertIsInstance(attributes, dict)
        self.assertIn("BaseModel", attributes.keys())
        self.assertIn("id", attributes["BaseModel"].keys())
        self.assertIs(attributes["BaseModel"]["id"], str)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" Module containing definition for FileStorage class."""

import datetime
import json
import os


class FileStorage:
    """ Definition for class that stores and retrieves data."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects
        :return: (dict) the dictionary __objects
        """
        return FileStorage.__objects

    @staticmethod
    def new(obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    @staticmethod
    def save():
        """ serializes __objects to the JSON file (Path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    @staticmethod
    def classes():
        """ returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    @staticmethod
    def reload():
        """ reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: FileStorage.classes()[v["__class__"]](**v) \
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    @staticmethod
    def attributes():
        """ returns the valid attributes and their types for classname"""
        attributes = {"BaseModel": \
                          {"id": str, "created_at": datetime.datetime, \
                           "updated_at": datetime.datetime}, \
                      "User": \
                          {"email": str, \
                           "password": str, \
                           "first_name": str, \
                           "last_name": str}, \
                      "State": \
                          {"name": str}, \
                      "City": \
                          {"state_id": str, \
                           "name": str}, \
                      "Amenity": \
                          {"name": str}, \
                      "Place": \
                          {"city_id": str, \
                           "user_id": str, \
                           "name": str, \
                           "description": str, \
                           "number_rooms": int, "number_bathrooms": int, \
                           "max_guest": int, \
                           "price_by_night": int, \
                           "latitude": float, \
                           "longitude": float, \
                           "amenity_ids": list}, \
                      "Review": \
                          {"place_id": str, \
                           "user_id": str, \
                           "text": str}
                      }
        return attributes

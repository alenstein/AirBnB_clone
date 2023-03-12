#!/usr/bin/python3
""" Module contains definition for the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Definition for class that manages the  review objects"""

    place_id = ""
    user_id = ""
    text = ""


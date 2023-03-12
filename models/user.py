#!/usr/bin/python3
"""Module contains definition for the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Definition for class that  manages user objects."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

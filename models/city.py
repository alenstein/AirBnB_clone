#!/usr/bin/python3
"""This module contains definition for the City."""

from models.base_model import BaseModel


class City(BaseModel):
    """Definition for class that manages city objects"""

    state_id = ""
    name = ""

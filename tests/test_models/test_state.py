#!/usr/bin/python3
""" Module containing unittests for models/state.py file"""

import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_id(self):
        self.assertIsInstance(self.state.id, str)

    def test_name(self):
        self.assertIsInstance(self.state.name, str)

    def test_created_at(self):
        self.assertIsInstance(self.state.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_str(self):
        expected_str = "[State] ({}) {}".format(self.state.id,
                                                self.state.__dict__)
        self.assertEqual(expected_str, str(self.state))

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()

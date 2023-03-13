#!/usr/bin/python3
"""Module containing unittests for the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Create a new User object before each test."""
        self.user = User()

    def tearDown(self):
        """Clean up after each test."""
        del self.user

    def test_email_attribute_exists(self):
        """Test that a new User instance has an email attribute."""
        self.assertTrue(hasattr(self.user, "email"))

    def test_password_attribute_exists(self):
        """Test that a new User instance has a password attribute."""
        self.assertTrue(hasattr(self.user, "password"))

    def test_first_name_attribute_exists(self):
        """Test that a new User instance has a first_name attribute."""
        self.assertTrue(hasattr(self.user, "first_name"))

    def test_last_name_attribute_exists(self):
        """Test that a new User instance has a last_name attribute."""
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_email_attribute_is_empty_string(self):
        """Test that a new User instance has an empty email attribute."""
        self.assertEqual(self.user.email, "")

    def test_password_attribute_is_empty_string(self):
        """Test that a new User instance has an empty password attribute."""
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute_is_empty_string(self):
        """Test that a new User instance has an empty first_name attribute."""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute_is_empty_string(self):
        """Test that a new User instance has an empty last_name attribute."""
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()

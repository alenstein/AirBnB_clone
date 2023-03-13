#!/usr/bin/python3
""" Module containing unittests for models/review.py file"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, "")
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_str_method(self):
        expected = "[{}] ({}) {}".format(type(self.review).__name__,
                                         self.review.id,
                                         self.review.__dict__)
        self.assertEqual(expected, str(self.review))

    def test_save_method(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertEqual(type(review_dict), dict)
        self.assertTrue('id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)
        self.assertTrue('__class__' in review_dict)
        self.assertTrue('place_id' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('text' in review_dict)

    def test_to_dict_method_values(self):
        iso_format = '%Y-%m-%dT%H:%M:%S.%f'
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")
        self.assertEqual(review_dict['created_at'],
                         self.review.created_at.strftime(iso_format))
        self.assertEqual(review_dict['updated_at'],
                         self.review.updated_at.strftime(iso_format))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
    Module contatining unit tests for the console.py file

    tests cases are for the HBNB class.
"""
import unittest
import io
import sys
from unittest import mock
from unittest.mock import patch

import models
from models import storage
from models.base_model import BaseModel
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('create')
            self.assertEqual('** class name missing **\n', f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('create MyClass')
            self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

        with patch('models.storage') as m:
            m.all.return_value = {'MyClass.1234': BaseModel(id='1234')}
            with patch('sys.stdout', new=io.StringIO()) as f:
                self.console.onecmd('create BaseModel')
                self.assertEqual('\n', f.getvalue())
                self.assertEqual(2, len(storage.all()))

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('show')
            self.assertEqual('** class name missing **\n', f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('show MyClass')
            self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('show BaseModel')
            self.assertEqual('** instance id missing **\n', f.getvalue())

        with patch('models.storage') as m:
            m.all.return_value = {'MyClass.1234': BaseModel(id='1234')}
            with patch('sys.stdout', new=io.StringIO()) as f:
                self.console.onecmd('show BaseModel 1234')
                self.assertEqual(str(BaseModel(id='1234')) +
                                 '\n', f.getvalue())

            with patch('sys.stdout', new=io.StringIO()) as f:
                self.console.onecmd('show BaseModel 4321')
                self.assertEqual('** no instance found **\n', f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('destroy')
            self.assertEqual('** classname missing **\n', f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('destroy MyClass')
            self.assertEqual('** class doesn\'t exist**\n', f.getvalue())

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd('destroy BaseModel')
            self.assertEqual('** instance id is missing **\n', f.getvalue())

        with patch('models.storage') as m:
            m.all.return_value = {'MyClass.1234': BaseModel(id='1234')}
            with patch('sys.stdout', new=io.StringIO()) as f:
                self.console.onecmd('destroy BaseModel 1234')
                self.assertEqual('', f.getvalue())
                self.assertEqual(0, len(storage.all()))

            with patch('sys.stdout', new=io.StringIO()) as f:
                self.console.onecmd('destroy BaseModel 4321')
                self.assertEqual('** no instance found **\n', f.getvalue())

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)


if __name__ == "__main__":
    unittest.main()

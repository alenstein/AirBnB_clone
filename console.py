#!/usr/bin/python3
""" Module with code for the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage, FileStorage
import re
import json


class HBNBCommand(cmd.Cmd):
    """ Definition for command interpreter class"""

    prompt = "(hbnb) "

    def default(self, line):
        """ catch commands if nothing else matches"""
        self._precmd(line)

    def _precmd(self, line):
        """ interprets commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(([^)]*)\))$", line)

        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""

            match_attr_and_value = re.search('^(?:"([^"]*)?(?:, (.*))?$)',
                                             attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(1) or "") + \
                        " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """ helper method for update() with a dictionary. """

        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class  name missing **")
        elif classname not in storage.classes():
            print("** instance id missing **")
        elif uid is None:
            print("** instance is missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items(self):
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all(self)[key].save()

    def do_EOF(self, line):
        """ handles end of file character """
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """ no instruction function."""
        pass

    def do_create(self, line):
        """ creates an instance."""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            try:
                instance = storage.classes()[line]()
                instance.save()
                print(instance.id)
            except Exception as e:
                print("** error creating instance: {} **".format(str(e)))

    def do_show(self, line):
        """prints the string representation of an instance."""

        if not line:
            # Check if the line argument is empty
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                # Check if the first word is a valid class name
                print("** class doesn't exist **")
            elif len(words) < 2:
                # Check if an instance id is missing
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    # Check if the instance with the given key exists
                    print("** no instance found **")
                else:
                    """ Use __str__ method to get the string representation
                     of the instance
                    """
                    print(storage.all()[key].__str__())

    def do_destroy(self, line):
        """ deletes an instance based on the classname and id."""
        if line == "" or line is None:
            print("** classname missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist**")
            elif len(words) < 2:
                print("** instance id is missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """ prints all string representation of all instances"""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """ counts the instances of a class"""

        words = line.split(' ')
        if not words[0]:
            print("**class name missing **")
        elif words[0] not in storage.classes():
            print("** class does not exist **")
        else:
            matches = []
            for k in storage.all():
                if k.startswith(words[0] + '.'):
                    matches.append(k)
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute"""
        match = re.search(
            r'^(\S+)(?:\s(\S+)(?:\s((?:\s((?:"[^"]*")|(?:(\S)+))))?)?)', line)
        if not match:
            print("** class name is missing **")
            return

        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if classname not in storage.classes():
            print("** class does not exist **")
            return
        if uid is None:
            print("** instance id missing **")
            return

        key = "{}.{}".format(classname, uid)
        if key not in storage.all():
            print("** no instance found **")
            return
        if not attribute:
            print("** attribute name missing **")
            return
        if not value:
            print("** value missing **")
            return

        value = value.replace('"', '')
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass

        attributes = storage.classes()[classname].__dict__
        if attribute in attributes:
            value = attributes[attribute](value)

        setattr(storage.all()[key], attribute, value)
        storage.all()[key].save()


if __name__ == '__main__':
    storage = FileStorage()
    HBNBCommand().cmdloop()

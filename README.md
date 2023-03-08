**Airbnb Clone Command Interpreter**
This project is a command interpreter built in Python to manage Airbnb objects. It is the first step towards building a full web application, the Airbnb clone. The command interpreter allows users to perform operations on objects, create new objects, retrieve objects, update object attributes, and destroy objects.

![Alt](/airbnb_project_outline.png "Project Outline")
***How to Start the Command Interpreter***
To start the command interpreter, navigate to the project directory in the terminal and run the following command:
*$ ./console.py*

***How to Use the Command Interpreter***
Once the command interpreter is running, you can use the following commands:

**help**: displays the list of available commands and their description
**quit**: exits the command interpreter
**create**: creates a new object and saves it to a JSON file
**show**: prints the string representation of an object based on the class name and id
**destroy**: deletes an object based on the class name and id
**all**: prints all string representation of all objects or all instances of a specific class
**update**: updates an attribute of an object based on the class name and id
To use a command, type the command followed by the necessary arguments. For example:

*(hbnb) create BaseModel*
This will print the string representation of the *BaseModel* instance with the id 1234-1234-1234.

**Examples**
Here are some examples of how to use the command interpreter:
(hbnb) create User
7dd780b9-1595-41b5-8a8d-788b6f0e579e
(hbnb) show User 7dd780b9-1595-41b5-8a8d-788b6f0e579e
[User] (7dd780b9-1595-41b5-8a8d-788b6f0e579e) {'id': '7dd780b9-1595-41b5-8a8d-788b6f0e579e', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}
(hbnb) all
["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}", "[User] (7dd780b9-1595-41b5-8a8d-788b6f0e579e) {'id': '7dd780b9-1595-41b5-8a8d-788b6f0e579e', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}"]
(hbnb) update User 7dd780b9-1595-41b5-


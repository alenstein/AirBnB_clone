**Airbnb Clone Command Interpreter**
<br>
This project is a command interpreter built in Python to manage Airbnb objects. It is the first step towards building a full web application, the Airbnb clone. The command interpreter allows users to perform operations on objects, create new objects, retrieve objects, update object attributes, and destroy objects.

![Alt](airbnb_project_outliine.png "Project Outline")<br>
<br>## How to Start the Command Interpreter***<br>
To start the command interpreter, navigate to the project directory in the terminal and run the following command:
<br>
*$ ./console.py*
<br>
<br>***How to Use the Command Interpreter***
<br>
Once the command interpreter is running, you can use the following commands:
<br>
**help**: displays the list of available commands and their description<br>
**quit**: exits the command interpreter<br>
**create**: creates a new object and saves it to a JSON file<br>
**show**: prints the string representation of an object based on the class name and id<br>
**destroy**: deletes an object based on the class name and id<br>
**all**: prints all string representation of all objects or all instances of a specific class<br>
**update**: updates an attribute of an object based on the class name and id<br>
To use a command, type the command followed by the necessary arguments. For example:<br>
<br>
*(hbnb) create BaseModel*
<br>This will print the string representation of the *BaseModel* instance with the id 1234-1234-1234.
<br>
<br>**Examples**<br>
Here are some examples of how to use the command interpreter:<br>
*(hbnb) create User<br>*
7dd780b9-1595-41b5-8a8d-788b6f0e579<br>
*(hbnb) show User 7dd780b9-1595-41b5-8a8d-788b6f0e579*<br>
[User] (7dd780b9-1595-41b5-8a8d-788b6f0e579e) {'id': '7dd780b9-1595-41b5-8a8d-788b6f0e579e', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}
<br>(hbnb) all<br>
["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}", "[User] (7dd780b9-1595-41b5-8a8d-788b6f0e579e) {'id': '7dd780b9-1595-41b5-8a8d-788b6f0e579e', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}"]<br>
(hbnb) update User 7dd780b9-1595-41b5-8a8d-788b6f0e579<br>
<br>

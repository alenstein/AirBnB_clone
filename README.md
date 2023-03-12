# Airbnb Clone Command Interpreter
<br>
This project is a command interpreter built in Python to manage Airbnb objects. It is the first step towards building a full web application, the Airbnb clone. The command interpreter allows users to perform operations on objects, create new objects, retrieve objects, update object attributes, and destroy objects.

![Alt](airbnb_project_outliine.png "Project Outline")<br>
<br>
## The Command Interpreter 
<br>
The application interface closely resembles the Bash shell, however, it is designed with a specific set of commands tailored to meet the needs of the AirBnB clone website. These commands are limited in number and serve the sole purpose of managing and utilizing the website's functionalities.
To start the command interpreter, navigate to the project directory in the terminal and run the following command:<br>

*$./console.py*

### How to Use the Command Interpreter
<br>
Once the command interpreter is running, you can use the following commands:

**help**: displays the list of available commands and their description<br>
**quit**: exits the command interpreter<br>
**create**: creates a new object and saves it to a JSON file<br>
**show**: prints the string representation of an object based on the class name and id<br>
**destroy**: deletes an object based on the class name and id<br>
**all**: prints all string representation of all objects or all instances of a specific class<br>
**update**: updates an attribute of an object based on the class name and id<br>

The command line interpreter provides a user-friendly interface for users to interact with the backend of the web application.
To use a command, type the command followed by the necessary arguments. For example:<br>
<br>
**(hbnb) create BaseModel**
<br>This will print the string representation of the *BaseModel* instance id.
<br>

### Examples
Here are some examples of how to use the command interpreter:<br>
**(hbnb) create User<br>**
7dd780b9-1595-41b5-8a8d-788b6f0e579<br>
**(hbnb) show User 7dd780b9-1595-41b5-8a8d-788b6f0e579**<br>
[User] (7dd780b9-1595-41b5-8a8d-788b6f0e579e) {'id': '7dd780b9-1595-41b5-8a8d-788b6f0e579e', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}
<br>(hbnb) all<br>
["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}", "[User] (7dd780b9-1595-41b5-8a8d-788b6f0e579e) {'id': '7dd780b9-1595-41b5-8a8d-788b6f0e579e', 'created_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0), 'updated_at': datetime.datetime(2023, 3, 8, 15, 30, 0, 0)}"]<br>
**(hbnb) update User 7dd780b9-1595-41b5-8a8d-788b6f0e579**<br>
<br>
The command line interpreter integrated with the backend and file storage system allows for several actions to be executed, including creating new objects such as a User or Place, retrieving objects from a file or database, performing operations on objects such as counting or computing statistics, updating attributes of an existing object, and deleting an object.

## Installing (Linux Enviroment)
Clone the repository for this project from GitHub with the following command:
* git clone https://github.com/alenstein/AirBnB_clone.git *

then after executing the command above all the required files to run the clone will be availble.

change directory to /AirBnB_clone/ by executing:
**cd AirBnB_clone**

then to start the program type:
** ./console.py **

### Critical files required by the clone:
* models/engine/file_storage.py:  This class is responsible for serializing instances to a JSON file and deserializing JSON file to instances. <br>
* models/init.py: This file contains a unique FileStorage instance for the application. <br>
* models/base_model.py: This class defines all common attributes and methods for other classes. <br>
* models/user.py: This class represents the User model and inherits from the BaseModel class. <br>
* models/state.py: This class represents the State model and inherits from the BaseModel class. <br>
* models/city.py: This class represents the City model and inherits from the BaseModel class. <br>
* models/amenity.py: This class represents the Amenity model and inherits from the BaseModel class. <br>
* models/place.py: This class represents the Place model and inherits from the BaseModel class. <br>
* models/review.py: This class represents the Review model and inherits from the BaseModel class <br>

## Using the program
The program can be used in two different modes, namely Interactive mode and Non-interactive mode.

In * Interactive mode *, the console will display a prompt with the prefix (hbnb) indicating that the user can input and execute a command. Once a command is executed, the program will wait for another command until the user exits the program. <br>
<br>
#### $ ./console.py <br> 
#### (hbnb) help **<br>
#### Documented commands (type help <topic>):<br>
#### ========================================<br>
#### EOF  help  quit<br>
#### (hbnb) <br> 
#### (hbnb) <br>
#### (hbnb) quit <br>
#### $

In * Non-interactive mode *, the program must be run with a command input piped into its execution so that the command is immediately executed without displaying any prompt. In this mode, no further input will be expected from the user.
<br>
#### echo "help" | ./console.py
#### (hbnb)
#### Documented commands (type help <topic>):
#### ========================================
#### EOF  all  count  create  destroy  help  quit  show  update
#### (hbnb) 
<br>



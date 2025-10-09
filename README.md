# AirBnB clone - The console

![AirBnB Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20251009%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251009T084801Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ea6eb2a1a33f7d8fdc10558652baad49d57f9dd2ea0356ea56e80e541deeb09b)

This project is part of the AirBnB clone series and focuses on implementing the BaseModel class and its functionalities. In this task, we are working on creating instances of the BaseModel class from dictionary representations.

## Tasks:
```
Ⓜ️ 0. README, AUTHORS:				COMPLETED ✅	
Ⓜ️ 1. Be pycodestyle compliant: 		COMPLETED ✅	
Ⓜ️ 2. Unittests: 				COMPLETED ✅
Ⓜ️ 3. BaseModel: 				COMPLETED ✅	
Ⓜ️ 4. Create BaseModel from dictionary:		COMPLETED ✅	
Ⓜ️ 5. Store first object: 			COMPLETED ✅
Ⓜ️ 6. Console 0.0.1:				COMPLETED ✅
Ⓜ️ 7. Console 0.1:				COMPLETED ✅
Ⓜ️ 8. First User:				COMPLETED ✅
Ⓜ️ 9. More classes:				COMPLETED ✅
Ⓜ️ 10. Console 1.0:				COMPLETED ✅

# AirBnB Clone - Console 0.0.1 & Console 0.1

This project is part of the AirBnB clone series and focuses on implementing a command-line interface (CLI) for managing AirBnB objects.

## Description :page_facing_up:
This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Environment :computer:
The console was developed in Ubuntu 14.04LTS using python3 (version 3.4.3).

### Further information :bookmark_tabs:
For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements :memo:
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 14.04, python3 and pep8 style corrector.

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

###### Example No.1

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name Betty
['User', 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name', 'Betty']
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)

```

## Built with :gear:
python3 (3.4.3)

### Version :pushpin:
HBnB - version 9.6

### Authors :fountain_pen:
* Ziad Ammar
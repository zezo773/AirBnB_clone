# 🏠 AirBnB Clone - The Console

![AirBnB Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png)

This project is part of the **AirBnB Clone** series.  
It focuses on implementing the **BaseModel class**, object serialization/deserialization, and a **command-line interface (CLI)** to manage AirBnB objects.

---

## ✅ Progress Overview

| Task | Description | Status |
|------|--------------|--------|
| 0 | README, AUTHORS | ✅ Completed |
| 1 | Be pycodestyle compliant | ✅ Completed |
| 2 | Unittests | ✅ Completed |
| 3 | BaseModel | ✅ Completed |
| 4 | Create BaseModel from dictionary | ✅ Completed |
| 5 | Store first object | ✅ Completed |
| 6 | Console 0.0.1 | ✅ Completed |
| 7 | Console 0.1 | ✅ Completed |
| 8 | First User | ✅ Completed |
| 9 | More classes | ✅ Completed |
| 10 | Console 1.0 | ✅ Completed |

---

## 🧠 Description

This is the **first phase** of a four-part AirBnB clone project.  
In this phase, a basic **command-line interpreter** was created using Python’s `cmd` module.  
It allows users to **create, show, update, destroy, and list** AirBnB objects.

---

## 💻 Environment

Developed and tested on:
- **Ubuntu 14.04 LTS**
- **Python 3.4.3**

📘 For more details on Python setup, visit [python.org](https://www.python.org/).

---

## 🧾 Requirements

- Knowledge of **Python 3**
- Understanding of **command-line interpreters**
- Environment setup: **Ubuntu 14.04**, **Python 3**
- Code compliant with **PEP8** style guide

---

## ⚙️ Command Summary

| **Command** | **Description** |
|--------------|-----------------|
| `create <class>` | Creates a new object of the specified class |
| `show <class> <id>` | Prints the string representation of an instance |
| `all [class]` | Prints all objects, optionally filtered by class name |
| `update <class> <id> <attribute> <value>` | Updates instance attributes and saves changes |
| `destroy <class> <id>` | Deletes an instance and updates the JSON file |
| `count <class>` | Displays the number of instances of a given class |
| `help` | Displays help information about available commands |
| `quit` / `EOF` | Exits the console |

---

## 💡 Example Usage

```bash
$ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106), 'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139)}
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name "Betty"
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'id': '...', 'name': 'Betty'}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) quit


## Built with :gear:
python3 (3.4.3)

### Version :pushpin:
HBnB - version 9.6

### Authors :fountain_pen:
* Ziad Ammar
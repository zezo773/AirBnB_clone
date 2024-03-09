ALX Full-Stack Software Engineer Program: AirBnB Clone (Step 1: Console)

This project is the first step towards building an AirBnB clone application. It implements a command-line interface (CLI) for data management in Python 3. This CLI allows you to perform CRUD operations (Create, Read, Update, Delete) on various AirBnB objects, forming the foundation for the application's data storage.

Project Structure:

This project serves as the initial part of a larger AirBnB clone application being developed as part of the ALX Full-Stack Software Engineer program.
The focus of this step is to create a console for data manipulation.
Console Functionality:

Written in Python 3.
Enables CRUD operations on AirBnB objects: User, City, Review, etc. (Further details on models in the "Models" section)
Provides a user-friendly interface for interacting with data.
Models:

Currently, the application utilizes seven models, each inheriting from a base model BaseModel:

BaseModel:

id: Unique identifier generated using the uuid package.
created_at: Datetime object indicating object creation time.
updated_at: Datetime object indicating last object update time.
class: String specifying the object's type (model).
Additional attributes specific to each model:

User:
first_name: String representing user's first name.
last_name: String representing user's last name.
password: String representing user's password (secure storage recommended).
email: String representing user's email address.
State:
name: String representing the state name.
City:
state_id: Foreign key referencing a State object.
name: String representing the city name.
Amenity:
name: String representing the amenity name.
Place:
city_id: Foreign key referencing a City object.
user_id: Foreign key referencing a User object (represents the owner).
name: String representing the place name.
description: String providing a description of the place.
number_rooms: Integer representing the number of rooms.
number_bathrooms: Integer representing the number of bathrooms.
max_guest: Integer representing the maximum guest capacity.
price_by_night: Integer representing the price per night.
latitude: Float representing the place's latitude.
longitude: Float representing the place's longitude.
amenity_ids: List of integers referencing associated Amenity objects.
Review:
place_id: Foreign key referencing a Place object.
user_id: Foreign key referencing a User object (represents the reviewer).
text: String containing the review text.
Usage:

Navigate to the project's root directory in your terminal.
Run the console using the following command:
./console
Console Commands:

create <type>: Create an object of type <type>. The newly created object's ID will be displayed.
update <id> <attribute_name> <attribute_value>: Update the specified attribute (<attribute_name>) of the object with ID <id> to the new value (<attribute_value>).
destroy <type> <id>: Delete the object of type <type> with ID <id>.
show <type> <id>: Display details of the object of type <type> with ID <id>.
all [<type>]: Display all objects of type <type>. If no type is specified, displays all objects.
help [command]: Show help information for a specific command (<command>) or display all documented commands if no command is specified.
Author:

Ziad Ammar

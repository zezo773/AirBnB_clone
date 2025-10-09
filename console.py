#!/usr/bin/env python3
import cmd
from models.classes import classes
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):

    def do_update(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objects = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        obj = all_objects[key]
        value = args[3].strip('"')
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass
        setattr(obj, attr_name, value)
        obj.save()

    def do_all(self, arg):
        """all string representation of all instances based or not"""
        args = arg.split()
        objects = storage.all()

        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print(
                [
                    str(obj)
                    for key, obj in objects.items()
                    if key.startswith(args[0] + ".")
                ]
            )

    def do_destroy(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        object_all = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in object_all:
            print("** no instance found **")
            return
        del object_all[key]
        storage.save()

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return

        new_inst = classes[arg]()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_object = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in all_object:
            print("** no instance found **")
            return
        print(all_object[key])

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when Ctrl+D (EOF) is pressed"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == "__main__":
    console = HBNBCommand()
    console.prompt = "(hbnb) "
    console.cmdloop()

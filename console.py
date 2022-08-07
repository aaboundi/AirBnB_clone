#!/usr/bin/python3
"""
Ths module is about console part of
AIrBnb project
"""


from cmd import Cmd
import inspect
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State



class HBNBCommand(Cmd):
    """HBNBCommand console class definition"""

    models = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        }

    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Empty line overwrite"""
        return False

    def do_create(self, arg):
        """command to create instance of BaseModel"""
        list_arguments_ofclass = arg.split()

        if HBNBCommand.validate_commandline(list_arguments_ofclass):
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_update(self, arg):
        """updates an object"""
        args = arg.split()
        list_arguments_ofcmd = arg.split()
        if HBNBCommand.validate_commandline(list_arguments_ofcmd):
            instance = storage.all()
            for key, value in instance.items():
                instance_id = key.split('.')[1]
                if instance_id == list_arguments_ofcmd[1]:
                    value = self.type_checker(list_arguments_ofcmd[3])
                    setattr(instance.get(key), list_arguments_ofcmd[2], value)
                    storage.save()

    def do_all(self, arg):
        """print string representation of all instances"""
        list_args_ofcmd = arg.split()
        # print(arg, list_args_ofcmd)
        # print("do_all", list(HBNBCommand.models))

        instance_list = []
        instance = storage.all()

        if len(list_args_ofcmd) < 1:
            for value, count in instance.items():
                instance_list.append(str(instance[value]))
            print("{}".format(instance_list))
        else:
            if list_args_ofcmd[0] not in self.models.keys():
                print("** class doesn't exist **")
                return
            for value, count in instance.items():
                if instance[value].__class__.__name__ == list_args_ofcmd[0]:
                    instance_list.append(str(instance[value]))
            print("{}".format(instance_list))

    def do_show(self, arg):
        """print string representation of instance of specified class"""
        list_args_ofcmd = arg.split()
        # print("do_show", list_args_ofcmd)
        if HBNBCommand.validate_commandline(list_args_ofcmd):
            key = "{}.{}".format(list_args_ofcmd[0], list_args_ofcmd[1])
            # print(key)
            if key in storage.all():
                print(storage.all()[key])
                return False
            else:
                print("** no instance found **")

        # print(list_args_ofcmd)
        return False

    def do_destroy(self, arg):
        """destroy instance of specified class"""

        list_args_ofcmd = arg.split()
        if HBNBCommand.validate_commandline(list_args_ofcmd):
            key = "{}.{}".format(list_args_ofcmd[0], list_args_ofcmd[1])
            # print(key)
            instance = storage.all()
            # print("do_destroy",instance)
            for key in list(instance):
                instance_id = key.split('.')[1]
                if instance_id == list_args_ofcmd[1]:
                    instance.pop(key, 0)
                    storage.save()

        return False

    @staticmethod
    def validate_commandline(args):
        """validate command line arguments"""
        # get command to call
        command = inspect.stack()[1][3]
        # print("validate_commandline", command, args)
        return HBNBCommand.check_command(command, args)

    @staticmethod
    def check_command(command, args_list):
        # print("ici", command, args_list)
        return {
            'do_create': HBNBCommand.validate_class,
            'do_show': HBNBCommand.validate_instance,
            'do_destroy': HBNBCommand.validate_instance,
            'do_update': HBNBCommand.validate_update,
        }.get(command)(args_list)

    @staticmethod
    def validate_class(args):
        """validate class args"""
        if len(args) < 1:
            print("** class name missing **")
            return False
        elif args[0] not in list(HBNBCommand.models):
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def validate_instance(args):
        """validate instance args"""
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in list(HBNBCommand.models):
            if len(args) > 1:
                return True
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False
        return HBNBCommand.validate_class(args)

    @staticmethod
    def validate_update(args):
        """validate class args"""

        if HBNBCommand.validate_instance(args):
            if len(args) < 3:
                print("** attribute name missing **")
                return (False)
            elif len(args) < 4:
                print("** value missing **")
                return False
            return True
        return False

    @staticmethod
    def type_checker(arg):
        """Check type of arg """
        check_list = list(arg)
        if check_list[0] == "'" or check_list[0] == '"':
            new_string = ''.join([c for c in arg if c != '"' and c != "'"])
            return (new_string)
        if ord(check_list[0]) >= 48 and ord(check_list[0]) <= 57:
            return (int(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()

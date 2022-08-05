#!/usr/bin/python3
"""
Ths module is about console part of
AIrBnb project
"""


from cmd import Cmd


class HBNBCommand(Cmd):
    """HBNBCommand console class definition"""

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

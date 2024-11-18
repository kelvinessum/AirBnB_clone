#!/usr/bin/python3
""" Defines the console class
which is the entry point of the Airbnb Project
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ does various AirBNB commands """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """End-of-file command to exit the program."""
        print()
        return True

    def do_help(self, arg):
        """Display help for commands."""
        return super().do_help(arg)

    def emptyline(self):
        """Do nothing on empty input."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

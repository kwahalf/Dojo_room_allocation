
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    dojo create_room (<room_type> <room_name>)...
    dojo add_person <first_name> <last_name>(Fellow | Staff)
                              [--wants_accomodation=(Y | N)]
    dojo (-i | --interactive)
    dojo (-h | --help | --version)

    Options:
    -i, --interactive  Interactive Mode
    -a, --wants_accomodation=<opt>  Person wants accomodation [default: N]
"""


import sys
import os
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
from Dojo import Dojo

dojo = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    cprint(figlet_format("DOJO VERSION 0", font='starwars'),
           'yellow', 'on_red', attrs=['bold'])
    print("Welcome to the DOJO! version 0")
    cprint(__doc__, 'blue')


class DojoSystem(cmd.Cmd):
    prompt = '(Dojo) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (<room_type> <room_name>)..."""

        purposes = args["<room_type>"]
        rooms = args["<room_name>"]
        for room in rooms:
            purpose = purposes[rooms.index(room)]
            dojo.create_room(room, purpose)

    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage:
    add_person <first_name> <second_name> (fellow | staff)
    [--wants_accomodation=<opt>]
        Options:
            -a, --wants_accomodation=<opt>  Wants accomodation [default: N]
        """
        first_name = args["<first_name>"]
        second_name = args["<second_name>"]
        if args["fellow"]:
            role = "FELLOW"
        else:
            role = "STAFF"
        wants_accomodation = args["--wants_accomodation"]
        if wants_accomodation == 'Y' or wants_accomodation == 'N':
            dojo.add_person(first_name, second_name, role, wants_accomodation)

    def do_clear(self, arg):
        """Clears screen"""
        os.system("clear")

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print("Don't be a stranger. Welcome back again!")
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    os.system("clear")
    intro()
    DojoSystem().cmdloop()

print(opt)

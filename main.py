#! /usr/bin/env python3

import sys
from mypackage import birthdays

if len(sys.argv)>1:
    birthdays.return_birthday(sys.argv[1])
else:
    print("Please type a valid name")

""" remember that every time you will type a name, if they are two different words " " are necessary """

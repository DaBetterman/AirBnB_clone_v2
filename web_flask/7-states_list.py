#!/usr/bin/python3
from sys import argv

argv = int(argv[1])

args = argv % 2

if args == 1:
    print("Number: {:d} is odd".format(argv))
elif args == 0:
    print("Number: {:d} is even".format(argv))
else:
    print("Not Found")

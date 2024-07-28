#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
if len(argv) == 1:
    print("{} argument:".format(len(argv)))
elif len(argv) >= 2:
    print("{} arguments:".format(len(argv)))
else:
    print("{} arguments.".format(len(argv)))

for i, arg in enumerate(argv, start=1):
    print("{}: {}".format(i, arg))

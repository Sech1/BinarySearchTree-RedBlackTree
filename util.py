import itertools
import sys
import time

# Using Spinner written for Project 1 (cs340).
class util:
    go = True

    def __init__(self):
        pass

    @classmethod
    def spinning_cursor(cls):
        spinner = itertools.cycle(['-Doing Algo Stuff. ', '/Doing Algo Stuff.. ',
                                   '|Doing Algo Stuff... ', '\\Doing Algo Stuff.... '])
        while util.go:
            sys.stdout.write(next(spinner))  # write the next character
            sys.stdout.flush()  # flush stdout buffer (actual character display)
            time.sleep(.25)
            sys.stdout.write('\r')  # erase the last written char


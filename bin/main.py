#!python


import sys
import os


# FIXME: WILL BREAK IN AN ACTUAL DISTRIBUTION!
sys.path = sys.path + [os.path.split(os.path.abspath(__file__))[0] + \
        os.sep + ".."]
import rogue

rogue.main()


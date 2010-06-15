# Property of Nikolai Ugelvik.
# Anyone else (especially Janis Kirsteins) claiming to own this
# software should be dismissed immediately.

# Code contained herein should only initialize the main module

import sys, os


# FIXME: WILL BREAK IN AN ACTUAL DISTRIBUTION!
sys.path = sys.path + [os.path.split(os.path.abspath(__file__))[0] + \
        os.sep + ".."]
import rogue

rogue.main()


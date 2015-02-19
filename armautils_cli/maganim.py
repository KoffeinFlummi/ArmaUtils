#!/usr/bin/env python3

import numpy as np
from PIL import Image

def maganim(pargs, oargs):
    if len(pargs) != 5:
        return -1

    animname, source, selection, magsize, indent = pargs
    try:
        magsize = int(magsize)
        if indent.lower() == "t":
            indent = "\t"
        else:
            indent = int(indent) * " "
    except:
        return -1

    magint = 1 / magsize

    for i in range(magsize):
        if i == 0:
            print(3 * indent + "class {}1 {}".format(animname, "{"))
        else:
            print(3 * indent + "class {}{}: {}1 {}".format(animname, (i+1), animname, "{"))

        if i == 0:
            print(4 * indent + "type = \"hide\";")
            print(4 * indent + "source = \"{}\";".format(source))

        print(4 * indent + "selection = \"{}{}\";".format(selection,(i+1)))

        if i == 0:
            print(4 * indent + "sourceAddress = \"mirror\";")
            print(4 * indent + "minValue = -1;")
            print(4 * indent + "maxValue = 0;")
            print(4 * indent + "minphase = -1;")
            print(4 * indent + "maxphase = 0;")

        hval = round(magint * i + 0.0001, 4)
        print(4 * indent + "hideValue = {};".format(min(1,hval)))

        print(3 * indent + "};")

    return 0

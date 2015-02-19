#!/usr/bin/env python3

import os
import sys
import argparse

from .usage import usage

from .smdimerge import smdimerge
from .timerge import timerge
from .maganim import maganim

def parse_args(args):
    funcs = {
        "smdimerge": smdimerge,
        "timerge": timerge,
        "maganim": maganim
    }

    if "--help" in args or len(args) == 0:
        return usage(args)

    if args[0] in funcs.keys():
        pargs = list(filter(lambda x: x[0] != "-", args[1:]))
        oargs = list(filter(lambda x: x[0] == "-", args[1:]))
        rcode = funcs[args[0]](pargs, oargs)
        if rcode < 0:
            return usage(args)
        else:
            sys.exit(rcode)

    return usage(args)

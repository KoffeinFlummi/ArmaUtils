#!/usr/bin/env python3

import os
import sys
import textwrap

def table(name, desc, length):
    try:
        # only available in 3.3+
        columns, lines = os.get_terminal_size()
    except:
        columns, lines = 80, 44

    output = "\n".join(textwrap.wrap(desc, columns - (length + 6)))
    output = textwrap.indent(output, (length + 4) * " ")
    output = "  " + name.ljust(length+2) + output[(length+4):]

    return output

def usage(args):
    funcs = {
        "smdimerge": {
            "description": "Merges specular and gloss maps (grayscale images) into one SMDI map",
            "args": [
                ["[specular map]", "Path to specular map"],
                ["[gloss map]", "Path to gloss map"],
                ["[target]", "Destination path"]
            ],
            "additional": ""
        },
        "timerge": {
            "description": "Merges the various components of a thermal map (grayscale images) into one map",
            "args": [
                ["[base map]", "Path to base texture of thermal map"],
                ["[moving map]", "Path to moving parts of thermal map"],
                ["[metabolism map]", "Path to metabolism map"],
                ["[target]", "Destination path"]
            ],
            "additional": "For more information regarding thermal imaging maps, check this link: https://community.bistudio.com/wiki/Thermal_Imaging_Maps."
        },
        "maganim": {
            "description": "Creates the model config structure for magazine animations (hiding of bullets)",
            "args": [
                ["[anim name]", "Prefix for the animation classnames (appended with number)"],
                ["[anim source]", "Name of animation source ('revolving' for weapons)"],
                ["[selection]", "Prefix for the selection names (appended with number)"],
                ["[mag size]", "Size of magazine"],
                ["[indent]", "Either an integer for number of spaces or t for a tab"]
            ],
            "additional": "Copy the output into the Animations class of your CfgModels entry."
        }
    }

    if len(args) > 0 and args[0] in funcs.keys():
        entry = funcs[args[0]]

        argstring = " ".join(list(map(lambda x: x[0], entry["args"])))
        print("\nUsage: armautils {} {}".format(args[0], argstring))

        print("\nArguments:")
        namelen = max(list(map(lambda x: len(x[0]), entry["args"])))
        for arg in entry["args"]:
            print(table(arg[0], arg[1], namelen))

        if entry["additional"] != "":
            print("\n\n{}".format(entry["additional"]))
        sys.exit(0)

    print("\nUsage: armautils [command] [parameters]")

    print("\nCommands:")
    namelen = max(list(map(lambda x: len(x), funcs.keys())))
    for command, entry in funcs.items():
        print(table(command, entry["description"], namelen))

    print("\n\nUse 'armautils [command] --help' to display help for an individual command.")
    print("\nProject Home: https://github.com/KoffeinFlummi/ArmaUtils")

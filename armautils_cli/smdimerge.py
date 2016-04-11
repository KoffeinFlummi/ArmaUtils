#!/usr/bin/env python3

import numpy as np
from PIL import Image

def smdimerge(pargs, oargs):
    if len(pargs) != 3:
        return -1

    path_spec, path_gloss, path_target = pargs

    try:
        spec = Image.open(path_spec).convert("RGBA")
        gloss = Image.open(path_gloss).convert("RGBA")
    except:
        print("Failed to read images. Please check your paths.")
        return 1

    if spec.size != gloss.size:
        print("Image sizes do not match, aborting.")
        return 1

    smdi = Image.new("RGBA", spec.size, "white")

    data = np.array(smdi)
    r,g,b,a = data.transpose()
    g = np.array(spec).transpose()[0]
    b = np.array(gloss).transpose()[0]
    data = np.array([r,g,b,a]).transpose()

    smdi = Image.fromarray(data)

    try:
        smdi.save(path_target)
    except:
        print("Failed to write final image to disk. Check permissions.")
        return 1
    else:
        print("SMDI map saved at: {}".format(path_target))

    return 0

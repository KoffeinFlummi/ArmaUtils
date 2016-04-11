#!/usr/bin/env python3

import numpy as np
from PIL import Image

def timerge(pargs, oargs):
    if len(pargs) != 4:
        return -1

    path_base, path_moving, path_meta, path_target = pargs

    try:
        base = Image.open(path_base).convert("RGBA")
        moving = Image.open(path_moving).convert("RGBA")
        meta = Image.open(path_meta).convert("RGBA")
    except:
        print("Failed to read images. Please check your paths.")
        return 1

    if base.size != moving.size or base.size != meta.size:
        print("Image sizes do not match, aborting.")
        return 1

    ti = Image.new("RGBA", meta.size, "white")

    data = np.array(ti)
    r,g,b,a = data.transpose()
    g = np.array(base).transpose()[0]
    b = np.array(moving).transpose()[0]
    a = np.array(meta).transpose()[0]
    data = np.array([r,g,b,a]).transpose()

    ti = Image.fromarray(data)

    try:
        ti.save(path_target)
    except:
        print("Failed to write final image to disk. Check permissions.")
        return 1
    else:
        print("TI map saved at: {}".format(path_target))

    return 0

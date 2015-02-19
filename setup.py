#!/usr/bin/env python3

import os
import sys
import platform
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ArmaUtils",
    version = "1.0",
    packages = ["armautils_cli"],
    scripts = ["scripts/armautils"],
    install_requires = ["numpy>=1.8.1", "Pillow>=2.7.0"],

    author = "Felix \"KoffeinFlummi\" Wiegand",
    author_email = "koffeinflummi@gmail.com",
    description = "Various tools for Arma content creation",
    long_description = read("README.md"),
    license = "MIT",
    keywords = "arma game development",
    url = "https://github.com/KoffeinFlummi/ArmaUtils",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Utilities"
    ]
)

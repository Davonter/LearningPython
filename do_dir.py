#!/usr/bin/python3

import os

path = os.path.abspath('.')

print(path)

path2 = os.path.split(path)

print(path2[0])
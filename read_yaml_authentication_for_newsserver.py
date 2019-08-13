#!/usr/bin/env python3

import sys

# pip install -U PyYAML
# pip3 install -U PyYAML

import yaml
print("yaml version is", yaml.__version__)



try:
	filename = sys.argv[1]
except:
	print("Specify filename")
	sys.exit(-1)

with open(filename) as f:
    #data = yaml.load(f, Loader=yaml.FullLoader)
    data = yaml.load(f, Loader=yaml.SafeLoader)

    print(data)


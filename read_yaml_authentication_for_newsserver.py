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


# now look at "servers"
try:
	# print(data["servers"])
	print("\nDetails of 'servers':")
	for i in data["servers"]:
		print(i)
		if isinstance(i,dict):
			# i is a dictionary, so print elements
			for x in i:
				print(x)
		else:
			# i is not a dictionary, so ... just print it:
			print(i)
except:
	print("No 'servers' defined")

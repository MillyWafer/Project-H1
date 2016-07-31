import random
import string

names = list()

def get_name():
	global names
	
	while True:

		name = random.choice(string.uppercase)
		name += random.choice(string.uppercase)
		name += random.choice(string.uppercase)

		name += random.choice (string.digits)
		name += random.choice (string.digits)
		name += random.choice (string.digits)

		if name not in names:
			names.append(name)
			return name



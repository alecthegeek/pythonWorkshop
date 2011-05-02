#!/usr/bin/env python

def greeter(name):
	"""Create a greeting."""
	greeting_base = "Hello "
	return  greeting_base + name


myName = raw_input("Please enter Name: ")

myGreeting = greeter(myName)

print(myGreeting)

print("\n")

#The same thing, but a little harder to read
print(greeter(raw_input("Please enter Name: ")))

# And finally some documenttion for (almost) free

print(greeter.__doc__)

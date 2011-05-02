#!/usr/bin/env python

def add(a, b):
	''' Add two numbers together'''
	return int(a)+int(b)

if __name__ == "__main__":
	fn = raw_input("First number: ")
	sn = raw_input("Second number: ")

	if fn.isdigit() and sn.isdigit():
		print (add(fn,sn))
	else:
		print("Numbers not entered")


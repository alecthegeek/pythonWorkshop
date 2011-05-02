#!/usr/bin/env python

from add3 import add
from subtract import sub
from div import div
from multiplication import mult


fn = raw_input("First number: ")
sn = raw_input("Second number: ")
op = raw_input("Operator : ")

if fn.isdigit() and sn.isdigit():
	if op == "/":
		print (div(fn,sn))
	elif op == "*":
		print (mult(fn,sn))
	elif op == "+":
		print (add(fn,sn))
	elif op == "-":
		print (sub(fn,sn))
	else:
		print("Operation not supported")
else:
	print("Numbers not entered")

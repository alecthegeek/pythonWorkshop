#!/usr/bin/env python

def add(a, y):
	''' Add two numbers together'''
	return a+y


fn = raw_input("First number: ")
sn = raw_input("Second number: ")

if fn.isdigit() and sn.isdigit():
	print (add(fn,sn))
else:
	print("Numbers not entered")


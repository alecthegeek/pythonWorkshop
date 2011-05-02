#!/usr/bin/env python

def div(a, y):
	''' Divide two numbers'''
	if y == 0:
		return 0
	else:
		return a/y

if __name__ == '__main__':
	print (div(2,4))
	print (div(2,0))

#!/usr/bin/env/python
#-*-coding:utf-8-*-

class Stack(object):
	'''
	Implement stack with Python.
	'''
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)		

	def pop(self):
		return self.items.pop()

	def empty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

	def top(self):
		return self.items[-1]


my_stack = Stack()
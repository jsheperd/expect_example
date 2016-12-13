#!/usr/bin/python
import sys

name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")
print("Happy %s.th birthday %s!" % (age, name))

while 1:
  r = raw_input("push q for quit: ")
  if r == "q":
    sys.exit()

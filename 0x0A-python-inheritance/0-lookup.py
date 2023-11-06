#!/usr/bin/python3
""" A module that contains a lookup func

- (for searching for and return the list of available attitributes and methods attached to the object in question)

"""

def lookup(obj):
  """ Used to search and return available attributes and method attached to obj """
  return dir(obj)

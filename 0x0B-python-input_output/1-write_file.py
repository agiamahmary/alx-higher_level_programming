#!/usr/bin/python3
""" A modlue containing  write_file func """


def write_file(filename="", text=''):
    ''' Writes to a file by overwriting to it'''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

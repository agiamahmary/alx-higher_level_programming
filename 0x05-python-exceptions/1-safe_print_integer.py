#!/usr/bin/python3
def safe_print_integer(value): 
    try: 
        print("{:d}".format(value))
	print() # Print as an integer 
        return True
    except: 
	return False

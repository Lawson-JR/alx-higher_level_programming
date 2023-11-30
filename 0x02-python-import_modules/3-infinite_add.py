#!/usr/bin/python3
if __name__ == "__main__":
    import sys

def infinite_add():
    arguments = sys.argv[1:]
    result = 0

    for arg in arguments:
        result += int(arg)
        
    print(result)

infinite_add()

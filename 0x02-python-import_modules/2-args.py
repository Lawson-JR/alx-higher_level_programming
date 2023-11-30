#!/usr/bin/python3
if __name__ == "__main__":
    import sys

def print_arguments():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print(f"Number of argument(s): {num_arguments}")

    if num_arguments == 0:
        print(".")
    else:
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")

print_arguments()

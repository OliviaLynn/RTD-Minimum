"""
Provides some print functions; also lets you apply them to command line args
"""

import sys


def print_excited(string_to_print: str):
    """
    Adds exclamation points to a string and then prints the result
    :param string_to_print: a string to be modified and printed
    :returns: no return
    """
    print(f"{string_to_print}!!")


def print_ominous(string_to_print: str):
    """
    Adds an ellipsis to a string and then prints the result
    :param string_to_print: a string to be modified and printed
    :returns: no return
    """
    print(f"{string_to_print}...")


def process_cl_or_use_default(default_string: str):
    """
    Parses commandline args and passes them to printing function; or, if there
    are no CL args, passes given string to the printing function
    :param default_string: string to print if no CL args
    :returns: no return
    """
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print_excited(arg)
    else:
        print_excited(default_string)


if __name__ == "__main__":
    print("begin...")
    process_cl_or_use_default("ok")
    print("finished!")
"""
Utils for https://adventofcode.com/2018/day/1.
"""


def parse_line(line):
    """
    Parses a line of input in the form [+-]\d, returning the integer
    equivalent.

    Args:
        line (string): The line to parse

    Returns:
        int: An int representing the current frequency
    """
    line = line.strip()
    op, num = line[0], int(line[1:])
    if op == "+":
        return num
    return -1 * num

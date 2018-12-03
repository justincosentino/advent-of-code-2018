"""
Utils for https://adventofcode.com/2018/day/3.
"""


def parse_line(line):
    """
    Parses a line of input in the form.

    Args:
        line (string): The line to parse, of the form

            "#<claim> @ <left>,<top> : <width>x<height>"

    Returns:
        dict: A dict of each field keyed on claim, left, top, width, and height
    """
    claim, rest = line.split("@")
    left, rest = rest.split(",")
    top, rest = rest.split(":")
    width, height = rest.split("x")
    return {
        'claim': claim.strip(),
        'left': int(left.strip()),
        'top': int(top.strip()),
        'width': int(width.strip()),
        'height': int(height.strip()),
    }

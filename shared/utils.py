"""
Utils for https://adventofcode.com/2018/. Shared across daily challenges.
"""

import argparse


def arg_parse_input_path(day, part):
    """
    Adds an argument parser for the input file path.

    TODO: more details.
    """
    parser = argparse.ArgumentParser(
        description='Solves Day {0} Part {1} of Advent of Code'.format(
            day,
            part))
    parser.add_argument(
        'path',
        type=str,
        nargs=1,
        help='The path to the input file.')
    args = parser.parse_args()
    path = args.path[0]
    return path


def read_file(path, parse_line):
    """
    Reads each line from provided data file, building a list of parsed inputs.

    Runs in O(n) time using O(n) memory.

    Args:
        path (string): The path to the input file

    Returns:
        list: A list of parsed input lines
    """
    data = []
    with open(path, 'r') as input_file:
        for line in input_file:
            data.append(parse_line(line))
    input_file.close()
    return data

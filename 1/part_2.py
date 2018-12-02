"""
Solves part 2 of https://adventofcode.com/2018/day/1.
"""

import collections
import os
import sys
import utils

# TODO: learn more about paths and importing and fix this nonsense
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shared.utils  # pylint: ignore=E402


def find_duplicate_frequency(inputs):
    """
    Finds the first duplicate frequency given a list of frequencies.

    Runs in O(n) time using O(n) memory.

    Args:
        inputs (list): A list of integer frequencies

    Returns:
        int: The first duplicate running frequency
    """
    seen = collections.defaultdict(bool)
    running_total = 0
    seen[running_total] = True

    while True:
        for freq in inputs:
            running_total += freq
            if seen[running_total]:
                return running_total
            seen[running_total] = True


def main():
    file_path = shared.utils.arg_parse_input_path(1, 2)
    data = shared.utils.read_file(file_path, utils.parse_line)
    first_duplicate = find_duplicate_frequency(data)
    print("The first duplicate running frequency total is {0}".format(
        first_duplicate))


if __name__ == "__main__":
    main()

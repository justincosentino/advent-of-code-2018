"""
Solves part 2 of https://adventofcode.com/2018/day/1.
"""

import collections
import utils


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
    file_path = utils.arg_parse_input_path(1, 2)
    data = utils.read_file(file_path)
    first_duplicate = find_duplicate_frequency(data)
    print("The first duplicate running frequency total is {0}.".format(
        first_duplicate))


if __name__ == "__main__":
    main()

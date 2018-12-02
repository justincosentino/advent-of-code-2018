"""
Solves part 1 of https://adventofcode.com/2018/day/1.
"""

import os
import sys
import utils

# TODO: learn more about paths and importing and fix this nonsense
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shared.utils # pylint: ignore=E402


def process_frequency(inputs):
    """
    Sums the list of frequencies.

    Runs in O(n) time using O(1) memory.

    Args:
        inputs (list): A list of integer frequencies

    Returns:
        int: The sum of all frequencies
    """
    return sum(inputs)


def main():
    file_path = shared.utils.arg_parse_input_path(1, 1)
    data = shared.utils.read_file(file_path, utils.parse_line)
    final_frequency = process_frequency(data)
    print("The resulting frequency is {0}".format(final_frequency))


if __name__ == "__main__":
    main()

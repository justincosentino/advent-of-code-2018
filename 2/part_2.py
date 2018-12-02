"""
Solves part 2 of https://adventofcode.com/2018/day/2.
"""

import collections
import os
import sys
import utils

# TODO: learn more about paths and importing and fix this nonsense
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shared.utils  # pylint: ignore=E402


def process_ids(box_ids):
    """
    Finds the two box_ids with a character difference of 1 and returns the
    common characters between the two box ids.

    Runs in O(n^2) time using O(1) memory where n is the number of box ids.

    TODO: this alg is gross and makes me sad. Improve it.

    Args:
        box_ids (list): A list of box id strings

    Returns:
        str: The common characters
    """
    for box1 in box_ids:
        for box2 in box_ids:
            diff = 0
            last_diff_index = 0
            for i, char in enumerate(box1):
                if box2[i] != char:
                    diff += 1
                    last_diff_index = i
            if diff == 1:
                box1_list = list(box1)
                del box1_list[last_diff_index]
                return "".join(box1_list)


def main():
    file_path = shared.utils.arg_parse_input_path(2, 2)
    data = shared.utils.read_file(file_path, utils.parse_line)
    common_letters = process_ids(data)
    print("The common letters between the two correct box ids: {0}.".format(
        common_letters))


if __name__ == "__main__":
    main()

"""
Solves part 1 of https://adventofcode.com/2018/day/2.
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
    Generates a checksum for the given list of box ids. The checksum is
    equal to:

        #_ids_with_2_repeated * #_ids_with_3_repeated

    Runs in O(kn) time using O(k) memory where n is the number of box ids
    and k is the length of each box id.

    Args:
        box_ids (list): A list of box id strings

    Returns:
        int: The checksum
    """
    twos = 0
    threes = 0
    for box in box_ids:
        counts = collections.Counter(box)
        seen_two = False
        seen_three = False
        for item in counts:
            if counts[item] == 3 and not seen_three:
                threes += 1
                seen_three = True
            if counts[item] == 2 and not seen_two:
                twos += 1
                seen_two = True
    return twos * threes


def main():
    file_path = shared.utils.arg_parse_input_path(2, 1)
    data = shared.utils.read_file(file_path, utils.parse_line)
    checksum = process_ids(data)
    print("The checksum for the list of box ids is {0}.".format(checksum))


if __name__ == "__main__":
    main()

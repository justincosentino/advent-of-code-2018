"""
Solves part 1 of https://adventofcode.com/2018/day/3.
"""

import collections
import os
import sys
import utils

# TODO: learn more about paths and importing and fix this nonsense
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shared.utils  # pylint: ignore=E402


def process_claims(claims):
    """
    Counts the number of square cloth inches that have multiple claims.

    Runs in O(nxy) time using O(xy) memory where n is the number of claims and
    x,y are the size of the cloth.

    Args:
        claims (list): A list of claim dicts. See utils#parse_line for details

    Returns:
        int: The number of square inches with multiple claims
    """
    cloth = collections.defaultdict(lambda: collections.defaultdict(int))
    for claim in claims:
        # Grab claim info
        left, top = claim["left"], claim["top"]
        width, height = claim["width"], claim["height"]

        # Increment all squares associated with the current claim. We could
        # also count all those with >= 2 claims here, but need to store more
        # information to avoid double counting.
        xs = range(left, left + width)
        ys = range(top, top + height)
        for x in xs:
            for y in ys:
                cloth[x][y] += 1

    # Count the number of squares that have more than 1 claim.
    count = 0
    for x in sorted(cloth.keys()):
        for y in sorted(cloth[x].keys()):
            if cloth[x][y] >= 2:
                count += 1

    return count


def main():
    file_path = shared.utils.arg_parse_input_path(3, 1)
    data = shared.utils.read_file(file_path, utils.parse_line)
    num_squares = process_claims(data)
    print("The number of square inches of fabric are within two or " +
          "more claims: {0}.".format(num_squares))


if __name__ == "__main__":
    main()

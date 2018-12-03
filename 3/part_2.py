"""
Solves part 2 of https://adventofcode.com/2018/day/3.
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
    Finds the first nonoverlapping claim.

    Runs in O(nxy) time using O(n + xy) memory where n is the number of claims
    and x,y are the size of the cloth.

    Args:
        claims (list): A list of claim dicts. See utils#parse_line for details

    Returns:
        str: The first nonoverlapping claim, None if none exist
    """
    cloth = collections.defaultdict(lambda: collections.defaultdict(str))
    valid = collections.defaultdict(bool)

    for claim in claims:
        # Grab claim info
        claim_id = claim["claim"]
        left, top = claim["left"], claim["top"]
        width, height = claim["width"], claim["height"]

        # By default, the claim is valid
        valid[claim_id] = True

        # Check all squares, claiming a square if no other claim has been made
        # and marking both the current and the claimer invalid if there is
        # overlap
        xs = range(left, left + width)
        ys = range(top, top + height)
        for x in xs:
            for y in ys:
                current_id = cloth[x][y]
                if current_id:
                    valid[current_id] = False
                    valid[claim_id] = False
                else:
                    cloth[x][y] = claim_id

    # Find the valid claim
    for claim_id, is_valid in valid.items():
        if is_valid:
            return claim_id

    # No valid claim found, return None
    return None


def main():
    file_path = shared.utils.arg_parse_input_path(3, 2)
    data = shared.utils.read_file(file_path, utils.parse_line)
    claim = process_claims(data)
    print("The id of the only nonoverlapping claim: {0}.".format(claim))


if __name__ == "__main__":
    main()

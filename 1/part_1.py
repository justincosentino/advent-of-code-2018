"""
Solves part 1 of https://adventofcode.com/2018/day/1.
"""

import utils


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
    file_path = utils.arg_parse_input_path(1, 1)
    data = utils.read_file(file_path)
    final_frequency = process_frequency(data)
    print("The resulting frequency is {0}.".format(final_frequency))


if __name__ == "__main__":
    main()

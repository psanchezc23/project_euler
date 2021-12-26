import time

import numpy as np


A_ASCII_VALUE = ord("A")


def exercise_022():
    """
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text
    file containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?

    :return: Total of all the names scores in the file
    :rtype: int
    """

    with open("files/exercise_022.txt", "r") as f:
        names = f.readlines()[0].split(",")

    names = sorted(names)

    total_score = np.int64(0)
    for position, raw_name in enumerate(names):
        name = raw_name.replace('"', "")
        name_score = sum([ord(c) - A_ASCII_VALUE + 1 for c in name])
        name_score *= (position + 1)
        total_score += name_score

    return total_score


if __name__ == '__main__':

    start_time = time.time()
    print(exercise_022())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

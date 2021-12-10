import time

from itertools import permutations


def exercise_024(number_str, position):
    """
    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?

    :param number_str: numbers to permute
    :type number_str: str
    :param position: position to return
    :type position: int

    :return: lexicographic permutation of <number_str> with position
    <position>.
    :rtype: str
    """

    perms = ["".join(p) for p in permutations(number_str)]
    sorted_perms = sorted(perms)
    return sorted_perms[position]


if __name__ == '__main__':

    start_time = time.time()
    number_str = "0123456789"
    print(exercise_024(number_str, 999999))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

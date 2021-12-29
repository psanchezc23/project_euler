import time

from exercises.utils import factorial


def _get_combinations_number(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def exercise_053():
    """
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.

    :return: Valid number
    :rtype: int
    """

    n_greater = 0
    for n in range(23, 101):
        for r in range(1, n+1):
            if _get_combinations_number(n, r) > 1000000:
                n_greater += n - 2 * r + 1
                break
    return n_greater


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_053())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

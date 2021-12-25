import time


def exercise_028(spiral_size):
    """
    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?

    :param spiral_size: Size of the spiral
    :type spiral_size: int

    :return: Sum of the diagonals
    :rtype: int
    """

    diagonals = {
        "upper-left": 0,
        "upper-right": 0,
        "lower-left": 0,
        "lower-right": 0
    }

    for size in range(3, spiral_size + 1, 2):
        diagonals["upper-right"] += size ** 2
        diagonals["upper-left"] += size ** 2 - (size - 1)
        diagonals["lower-left"] += size ** 2 - 2 * (size - 1)
        diagonals["lower-right"] += size ** 2 - 3 * (size - 1)

    sum_diagonals = sum(diagonals.values()) + 1
    return sum_diagonals


if __name__ == '__main__':
    start_time = time.time()
    n_digits = 1001
    print(exercise_027(n_digits))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

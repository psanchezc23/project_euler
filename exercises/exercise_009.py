import time
import numpy as np


def exercise_009(triplet_sum):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    :param int triplet_sum: Sum of Pythagorean triplet
    :return: product of abc that sums <triplet_sum>.
    :rtype: int

    """

    for b in range(1, triplet_sum):
        for a in range(1, b):
            c = np.sqrt(a ** 2 + b ** 2)

            if a + b + c == triplet_sum:
                print('a < b < c')
                print('{a} < {b} < {c}'.format(a=a, b=b, c=c))
                return a * b * c

    return 0


if __name__ == '__main__':
    start_time = time.time()
    triplet_sum = 1000
    print(exercise_009(triplet_sum))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

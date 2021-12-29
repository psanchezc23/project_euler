import time

from exercises.utils import long_division


def exercise_026(maximum_divisor):
    """
    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.

    :param maximum_divisor: Maximum divisor
    :type maximum_divisor: int

    :return: Divisor with the longest recurring cycle.
    :rtype: int
    """

    cycle_divisor = {}
    for d in range(1, maximum_divisor):
        div = long_division(1, d)
        cycle = div.split("(")
        cycle_divisor[d] = len(cycle[-1]) - 1 if len(cycle) == 2 else 0
    return max(cycle_divisor, key=cycle_divisor.get)


if __name__ == '__main__':

    start_time = time.time()
    maximum_divisor = 1000
    print(exercise_026(maximum_divisor))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

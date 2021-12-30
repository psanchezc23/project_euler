import time


def exercise_063():
    """
    The 5-digit number, 16807=75, is also a fifth power. Similarly, the
    9-digit number, 134217728=89, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?

    :return: Size of the square
    :rtype: int
    """

    n = 0
    found = True
    n_nth_power = 0
    while found:
        found = False
        n += 1
        for number in range(1, 10):
            if len(list(str(number ** n))) == n:
                n_nth_power += 1
                found = True
    return n_nth_power


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_063())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

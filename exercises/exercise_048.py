import time


def exercise_048(maximum_number):
    """
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

    :return: Last ten digits of the series.
    :rtype: int
    """

    result = 0
    for i in range(1, maximum_number+1):
        i_10_digits = int(str(i ** i)[-10:])
        result = int(str(result + i_10_digits)[-10:])
    return result


if __name__ == '__main__':
    start_time = time.time()
    maximum_number = 1000
    print(exercise_048(maximum_number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

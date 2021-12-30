import time


PANDIGITAL_1_9 = set(map(str, range(1, 9)))


def _is_pandigital(number_str):
    number_digits = set(number_str)
    return len(PANDIGITAL_1_9 - number_digits) == 0


def exercise_038():
    """
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?

    :return: Largest pandigital 9-digit number
    :rtype: int
    """

    maximum_number = 918273645
    for base in range(9234, 10000):
        number_str = str(base) + str(base * 2)
        number = int(number_str)
        if _is_pandigital(number_str):
            maximum_number = max(maximum_number, number)
    return maximum_number


if __name__ == "__main__":
    start_time = time.time()
    print(exercise_038())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

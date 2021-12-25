import time


def exercise_030(n_digits):
    """
    Surprisingly there are only three numbers that can be written as the sum
    of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.

    :param n_digits: Maximum number of digits for each number
    :type n_digits: int

    :return: Sum of all the numbers written as the sum of fifth powers
    :rtype: int
    """

    valid_numbers = set()

    stop = False
    number = 1
    maximum_number = 0
    while not stop:
        maximum_number = number * 9 ** n_digits
        if len(str(maximum_number)) <= number:
            stop = True
        number += 1

    powers = {str(k): pow(k, n_digits) for k in range(0, 10)}
    for number in range(10, maximum_number + 1):
        number_digits = list(str(number))
        sum_number_digits_exp = sum([powers[d] for d in number_digits])
        if number == sum_number_digits_exp:
            valid_numbers.add(number)

    return sum(valid_numbers)


if __name__ == '__main__':
    start_time = time.time()
    n_digits = 5
    print(exercise_030(n_digits))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

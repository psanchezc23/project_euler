import time


def exercise_036(maximum_number):
    """
    The decimal number, 585 = 10010010012 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)

    :return: Sum of palindromic number in both bases.
    :rtype: int
    """

    def is_palindromic(number):
        return str(number) == str(number)[::-1]

    double_palindromic = []
    for number in range(maximum_number):
        if is_palindromic(number):
            number_bin = bin(number)[2:]
            if is_palindromic(number_bin):
                double_palindromic.append(number)

    return sum(double_palindromic)


if __name__ == '__main__':
    start_time = time.time()
    maximum_number = 1000000
    print(exercise_036(maximum_number))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

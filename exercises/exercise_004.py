import time


def exercise_004(n_digits):
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    :param n_digits: Digits of numbers to multiply.
    :type n_digits: int

    :return: largest palindrome made from the product of two <digits>-digit
    numbers.
    :rtype: int
    """

    digits_nums_range = range(10 ** (n_digits-1) - 1, 10 ** n_digits, 1)

    max_mult = 0
    for num_1 in digits_nums_range:
        for num_2 in digits_nums_range:
            mult = num_1*num_2
            mult_str = str(mult)
            if mult_str == mult_str[::-1]:
                max_mult = max(max_mult, mult)

    return max_mult


if __name__ == '__main__':
    start_time = time.time()
    digits = 2  # 2
    print(exercise_004(digits))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

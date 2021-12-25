import time

from exercises.utils import range_product


def exercise_034():
    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are not included.

    :return: Number of ways to reach the coins sum
    :rtype: int
    """

    digits_factorial = {str(k): range_product(1, k) for k in range(1, 10)}
    digits_factorial["0"] = 1

    maximum_number = digits_factorial["9"] * 7
    numbers = []
    for i in range(3, maximum_number):
        digits = list(str(i))
        sum_fact_digts = sum([digits_factorial[d] for d in digits])
        if i == sum_fact_digts:
            numbers.append(i)

    return sum(numbers)


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_034())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

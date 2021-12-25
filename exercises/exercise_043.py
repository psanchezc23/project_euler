import time

from itertools import permutations


def exercise_043():
    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
    note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.

    :return: sum of all numbers
    :rtype: int
    """

    # divisible by 5 and not repeated numbers
    d6 = "5"

    # divisible by 11
    d7d8 = set()
    for number in range(501, 599):
        number_str = str(number)
        if (number % 11 == 0) and len(set(number_str)) == 3:
            d7d8.add(number_str[1:])

    # divisible by 13
    d6d7d8d9 = set()
    for number in range(100, 1000):
        number_str = str(number)
        if number_str[:-1] in d7d8 and number_str[-1] != d6 and \
                len(set(number_str)) == 3 and (number % 13 == 0):
            d6d7d8d9.add(d6 + number_str)

    # divisible by 17
    d6d7d8d9d10 = set()
    for d10 in range(10):
        for number in d6d7d8d9:
            d6d7d8d9d10_i = str(number) + str(d10)
            if len(set(d6d7d8d9d10_i)) == 5 and \
                    (int(d6d7d8d9d10_i[-3:]) % 17 == 0):
                d6d7d8d9d10.add(d6d7d8d9d10_i)

    # divisible by 7
    d5d6d7d8d9d10 = set()
    for d5 in range(10):
        for number in d6d7d8d9d10:
            d5d6d7d8d9d10_i = str(d5) + str(number)
            if len(set(d5d6d7d8d9d10_i)) == 6 and \
                    (int(d5d6d7d8d9d10_i[:3]) % 7 == 0):
                d5d6d7d8d9d10.add(d5d6d7d8d9d10_i)

    valid_numbers = []
    for number in d5d6d7d8d9d10:
        for d4 in {"0", "2", "4", "6", "8"}:  # divisible by 2
            d4d5d6d7d8d9d10 = d4 + number
            if len(set(d4d5d6d7d8d9d10)) == 7:
                digits = set(range(10)) - set(map(int, set(d4d5d6d7d8d9d10)))
                for d1d2d3_i in permutations(digits):
                    d1d2d3 = "".join(map(str, d1d2d3_i))
                    final_number = d1d2d3 + d4d5d6d7d8d9d10
                    if int(final_number[2:5]) % 3 == 0:
                        valid_numbers.append(int(final_number))

    return sum(valid_numbers)


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_043())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

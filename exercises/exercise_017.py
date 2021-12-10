import time
import numpy as np


def get_number_str(number):
    """
    Given a number, this function retrieves it written in english words.
    :param number: Number to write in english words.
    :type number: int

    :return: Number in english words.
    :rtype: str
    """

    en_dictionary = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if number in en_dictionary:
        return en_dictionary[number]
    elif 20 < number < 100:
        dec = np.int64(np.floor(number / 10) * 10)
        return "{}-{}".format(
            en_dictionary[dec],
            en_dictionary[np.int(number - dec)]
        )
    else:
        number_digits = list(map(int, list(str(number))))
        hundred_thousand = "{} {}".format(
            en_dictionary[number_digits[0]],
            "hundred" if len(number_digits) < 4 else "thousand"
        )

        units = 10 ** (len(number_digits) - 1)
        number -= np.int64(np.floor(number / units) * units)
        if number > 0:
            return "{} and {}".format(hundred_thousand, get_number_str(number))
        else:
            return hundred_thousand


def exercise_017(number_limit):
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.

    :param number_limit: Maximum number to take into account
    :type number_limit: int

    :return: Sum of the letters of each number below number_limit.
    :rtype: int
    """

    n_letters = 0
    for number in range(1, number_limit + 1):
        en_number_str = get_number_str(number)
        clean_en_number_str = en_number_str.replace(" ", "").replace("-", "")
        n_letters += len(clean_en_number_str)

    return n_letters


if __name__ == '__main__':
    start_time = time.time()
    number_limit = 1000
    print(exercise_017(number_limit))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

import time


def _is_valid_number(number):
    if set(str(2 * number)) == \
            set(str(3 * number)) == \
            set(str(4 * number)) == \
            set(str(5 * number)) == \
            set(str(6 * number)):
        return True
    return False


def exercise_052():
    """
    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.

    :return: Valid number
    :rtype: int
    """

    number = 123456
    while number <= 165432:
        if _is_valid_number(number):
            return number
        number += 1


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_052())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

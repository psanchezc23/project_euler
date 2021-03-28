import numpy as np


def exercise_001(numbers, maximum_value):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

    :param array-like numbers: The values should be multiples of these numbers.
    :param int maximum_value: Maximum number to look for multiples.
    :return: It returns the sum of the multiples of the numbers.
    :rtype: int

    """

    vector = np.arange(maximum_value)
    idx = np.zeros(maximum_value, dtype=bool)
    for num in numbers:
        idx |= (vector % num) == 0
    return np.sum(vector[idx])


if __name__ == "__main__":
    numbers = np.array([3, 5])
    maximum_value = 1000
    print(exercise_001(numbers, maximum_value))


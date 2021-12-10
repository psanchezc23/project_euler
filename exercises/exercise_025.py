import time


def exercise_025(n_digits):
    """
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?

    :param n_digits: Number of digits
    :type n_digits: int

    :return: First number with <n_digits> digits.
    :rtype: int
    """

    fibonacci_number_1 = 1
    fibonacci_number_2 = 1
    fibonacci_number_2_index = 2
    while len(str(fibonacci_number_1 + fibonacci_number_2)) < n_digits:
        next_fibonacci_number = fibonacci_number_1 + fibonacci_number_2
        fibonacci_number_1 = fibonacci_number_2
        fibonacci_number_2 = next_fibonacci_number
        fibonacci_number_2_index += 1

    return fibonacci_number_2_index + 1


if __name__ == '__main__':

    start_time = time.time()
    n_digits = 1000
    print(exercise_025(n_digits))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

import time

from exercises.utils import is_prime


def exercise_007(n_prime):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?

    :param n_prime: Number of prime numbers.
    :type n_prime: int

    :return: <n_prime>-th prime number.
    :rtype: int
    """

    count = 1
    candidate = 1
    while count < n_prime:
        candidate += 2
        if is_prime(candidate):
            count += 1

    return candidate


if __name__ == '__main__':
    start_time = time.time()
    n_prime = 10001  # 10
    print(exercise_007(n_prime))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

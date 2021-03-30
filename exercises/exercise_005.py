import time


def exercise_005(n_divisors):
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    :param int n_divisors: Number of divisors
    :return: smallest positive number that is evenly divisible by all of the numbers from 1 to <n_divisors>.
    :rtype: int

    """

    divisors = range(1, n_divisors+1)

    # Extract all the cumprod of prime numbers (it will be the step)
    cumprod_primes = 1
    for num in range(1, n_divisors+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                cumprod_primes *= num

    number = cumprod_primes
    while True:

        is_valid = True
        for divisor in divisors:
            if (number % divisor) != 0:
                is_valid = False
                break

        if is_valid:
            break

        number += cumprod_primes

    return number


if __name__ == '__main__':
    start_time = time.time()
    n_divisors = 20  # 10
    print(exercise_005(n_divisors))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

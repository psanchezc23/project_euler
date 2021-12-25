import time

from exercises.utils import is_prime


def exercise_037():
    """
    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain
    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
    right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

    :return: Sum of truncatable numbers.
    :rtype: int
    """

    primes = dict()

    number = 10
    truncatable_numbers_to_find = 11
    truncatable_numbers = []
    while truncatable_numbers_to_find:
        if is_prime(number):
            primes[number] = True
            number_str = str(number)
            i = 1
            prime = True
            while prime and i < len(number_str):

                number_i = int(number_str[i:])
                prime_i = primes.get(number_i)
                if prime_i is None:
                    primes[number_i] = is_prime(number_i)
                    prime_i = primes[number_i]

                number_minus_i = int(number_str[:-i])
                prime_minus_i = primes.get(number_minus_i)
                if prime_minus_i is None:
                    primes[number_minus_i] = is_prime(number_minus_i)
                    prime_minus_i = primes[number_minus_i]

                prime = prime & prime_i & prime_minus_i
                i += 1

            if prime:
                truncatable_numbers_to_find -= 1
                truncatable_numbers.append(number)

        number += 1

    return sum(truncatable_numbers)


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_037())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

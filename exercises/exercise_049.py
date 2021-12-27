import time

from itertools import permutations

from exercises.utils import is_prime


def exercise_049():
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?

    :return: Valid sequences
    :rtype: list[list]
    """

    solutions = []
    watched = {}
    for number in range(1001, 10000, 2):
        if number not in watched:
            number_digits = list(str(number))
            primes_perms = set()
            for perm_digits in permutations(number_digits):
                perm = int("".join(perm_digits))
                if perm > 1000:
                    watched[perm] = True
                    if is_prime(perm):
                        primes_perms.add(perm)

            valid_primes = set()
            for pp1 in primes_perms:
                for pp2 in primes_perms:
                    if abs(pp1 - pp2) in [3330, 6660]:
                        valid_primes.add(pp1)
                        valid_primes.add(pp2)

            if len(valid_primes) >= 3:
                solutions.append(sorted(valid_primes))

    return solutions


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_049())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

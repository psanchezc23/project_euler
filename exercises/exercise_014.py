import time


def exercise_014(number_limit):
    """
    The following iterative sequence is defined for the set of positive
    integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

    :param number_limit: Maximum number to test
    :type number_limit: int

    :return: greatest product of <n-digits> consecutive digits.
    :rtype: int
    """

    def collatz_next_number(num):
        return  num / 2 if num % 2 == 0 else 3 * num + 1

    maximum_number = 0
    maximum_number_len_chain = 0

    chain_dict = {}

    for num in range(number_limit):

        next_number = num
        len_chain = 1
        while next_number > 1:
            next_number = collatz_next_number(next_number)

            if next_number in chain_dict:
                len_chain += chain_dict[next_number]
                break
            else:
                len_chain += 1

        if len_chain > maximum_number_len_chain:
            maximum_number = num
            maximum_number_len_chain = len_chain

        chain_dict[num] = len_chain

    return maximum_number, maximum_number_len_chain


if __name__ == '__main__':
    start_time = time.time()
    number_limit = 1000000
    print(exercise_014(number_limit))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

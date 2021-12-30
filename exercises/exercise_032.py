import time


PANDIGITAL_1_9 = set(map(str, range(1, 10)))


def _is_pandigital(number_str):
    number_digits = set(number_str)
    return len(PANDIGITAL_1_9 - number_digits) == 0 and len(number_str) == 9


def exercise_032():
    """
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to
    only include it once in your sum.

    :return: Number of pandigital products
    :rtype: int
    """

    pandigital_products = set()
    pandigital_sum = 0
    for number_1 in range(2, 100):
        for number_2 in range(2, 10000 // number_1):
            product = number_1 * number_2
            number_str = str(number_1) + str(number_2) + str(product)
            if _is_pandigital(number_str) and \
                    product not in pandigital_products:
                pandigital_sum += product
                pandigital_products.add(product)
    return pandigital_sum


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_032())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

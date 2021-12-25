import time


def exercise_039():
    """
    If p is the perimeter of a right angle triangle with integral length
    sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?

    :return: Perimeter for which the number of solutions is maximised.
    :rtype: int
    """

    n_solutions = {}
    max_p = 0
    for p in range(2, 1000, 2):
        n_solutions_p = 0
        for a in range(2, p // 3):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                n_solutions_p += 1
        n_solutions[p] = n_solutions_p
        if n_solutions_p > n_solutions.get(max_p, 0):
            max_p = p
    return max_p


if __name__ == '__main__':
    start_time = time.time()
    print(exercise_039())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

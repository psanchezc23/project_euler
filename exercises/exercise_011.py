import time

import numpy as np


def exercise_011():
    """
    In the 20×20 grid below, four numbers along a diagonal line have been marked
    in red.

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?

    :return: Greatest product
    :rtype: int
    """

    with open("../files/exercise_011.txt", "r") as f:
        matrix = [list(map(int, line.split(" "))) for line in f.readlines()]
    matrix = np.matrix(matrix)

    n_row = matrix.shape[0]
    n_col = matrix.shape[1]

    max_product = 0
    for row in range(n_row):
        for col in range(n_col):
            row_col = {
                "N": matrix[row-3:row+1, col],
                "S": matrix[row:row+4, col],
                "W": matrix[row, col-3:col+1],
                "E": matrix[row, col:col+4],
                "NE": np.diag(np.fliplr(matrix[row-3:row+1, col:col+4])),
                "NW": np.diag(matrix[row-3:row+1, col-3:col+1]),
                "SE": np.diag(matrix[row:row+4, col:col+4]),
                "SW": np.diag(np.fliplr(matrix[row:row+4, col-3:col+1]))
            }
            max_product_row_col = max([np.prod(v) for v in row_col.values()])
            max_product = max(max_product, max_product_row_col)

    return max_product


if __name__ == '__main__':

    start_time = time.time()
    print(exercise_011())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

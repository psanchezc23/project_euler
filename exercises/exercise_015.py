import time
import numpy as np


def exercise_015(grid_size):
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.

    How many such routes are there through a 20×20 grid?

    :param grid_size: Size of the grid
    :type grid_size: int

    :return: Number of routes
    :rtype: int
    """

    # Using central binomial coefficient: (2n)! / (n!)^2
    if grid_size <= 10:
        num = np.prod(np.arange(1, 2 * grid_size + 1, dtype=np.int64))
        den = np.prod(np.arange(1, grid_size + 1, dtype=np.int64)) ** 2
        n_routes = num / den
    else:
        n_routes = np.prod([
            (grid_size + k) / k for k in range(1, grid_size + 1)
        ])

    return np.int64(np.round(n_routes))


def exercise_015_recursive(grid_size):
    def _get_n_routes(n_rows_left, n_columns_left):
        n_routes = 0
        if not n_rows_left and not n_columns_left:
            n_routes = 1
        elif not n_rows_left and n_columns_left:
            n_routes += _get_n_routes(n_rows_left, n_columns_left - 1)
        elif n_rows_left and not n_columns_left:
            n_routes += _get_n_routes(n_rows_left - 1, n_columns_left)
        else:
            n_routes += _get_n_routes(n_rows_left - 1, n_columns_left)
            n_routes += _get_n_routes(n_rows_left, n_columns_left - 1)
        return n_routes

    return _get_n_routes(grid_size, grid_size)


if __name__ == '__main__':
    start_time = time.time()
    grid_size = 20
    print(exercise_015(grid_size))
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

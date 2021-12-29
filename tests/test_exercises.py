import time
import exercises
import numpy as np


MAXIMUM_EXECUTION_TIME = 10  # seconds


def check_time_exercises(exercise_function, *args):
    start_time = time.time()
    _ = exercise_function(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    assert execution_time < MAXIMUM_EXECUTION_TIME


def test_exercise_001():
    exercise_function = exercises.exercise_001
    numbers = np.array([3, 5])
    maximum_value = 10
    solution = exercise_function(numbers, maximum_value)
    assert solution == 23

    numbers = np.array([3, 5])
    maximum_value = 1000
    solution = exercise_function(numbers, maximum_value)
    assert solution == 233168

    check_time_exercises(exercise_function, numbers, maximum_value)


def test_exercise_002():
    exercise_function = exercises.exercise_002

    maximum_value = 4000000
    solution = exercise_function(maximum_value)
    assert solution == 4613732

    check_time_exercises(exercise_function, maximum_value)


def test_exercise_003():
    exercise_function = exercises.exercise_003

    number = 13195
    solution = exercise_function(number)
    assert solution == 29

    number = 600851475143
    solution = exercise_function(number)
    assert solution == 6857

    check_time_exercises(exercise_function, number)


def test_exercise_004():
    exercise_function = exercises.exercise_004

    digits = 2
    solution = exercise_function(digits)
    assert solution == 9009

    digits = 3
    solution = exercise_function(digits)
    assert solution == 906609

    check_time_exercises(exercise_function, digits)


def test_exercise_005():
    exercise_function = exercises.exercise_005

    n_divisors = 10
    solution = exercise_function(n_divisors)
    assert solution == 2520

    n_divisors = 20
    solution = exercise_function(n_divisors)
    assert solution == 232792560

    check_time_exercises(exercise_function, n_divisors)


def test_exercise_006():
    exercise_function = exercises.exercise_006

    n_natural = 10
    solution = exercise_function(n_natural)
    assert solution == 2640

    n_natural = 100
    solution = exercise_function(n_natural)
    assert solution == 25164150

    check_time_exercises(exercise_function, n_natural)


def test_exercise_007():
    exercise_function = exercises.exercise_007

    n_prime = 6
    solution = exercise_function(n_prime)
    assert solution == 13

    n_prime = 10001
    solution = exercise_function(n_prime)
    assert solution == 104743

    check_time_exercises(exercise_function, n_prime)


def test_exercise_008():
    exercise_function = exercises.exercise_008

    n_digits = 4
    solution = exercise_function(n_digits)
    assert solution == 5832

    n_digits = 13
    solution = exercise_function(n_digits)
    assert solution == 23514624000

    check_time_exercises(exercise_function, n_digits)


def test_exercise_009():
    exercise_function = exercises.exercise_009

    triplet_sum = 12
    solution = exercise_function(triplet_sum)
    assert solution == 60

    triplet_sum = 1000
    solution = exercise_function(triplet_sum)
    assert solution == 31875000

    check_time_exercises(exercise_function, triplet_sum)


def test_exercise_010():
    exercise_function = exercises.exercise_010

    number = 10
    solution = exercise_function(number)
    assert solution == 17

    number = 2000000
    solution = exercise_function(number)
    assert solution == 142913828922

    check_time_exercises(exercise_function, number)


def test_exercise_011():
    exercise_function = exercises.exercise_011

    solution = exercise_function()
    assert solution == 70600674

    check_time_exercises(exercise_function)


def test_exercise_012():
    exercise_function = exercises.exercise_012

    n_divisors = 5
    solution = exercise_function(n_divisors)
    assert solution == 28

    n_divisors = 500
    solution = exercise_function(n_divisors)
    assert solution == 76576500

    check_time_exercises(exercise_function, n_divisors)


def test_exercise_013():
    exercise_function = exercises.exercise_013

    number = 10
    solution = exercise_function(number)
    assert solution == '5537376230'

    check_time_exercises(exercise_function, number)


def test_exercise_014():
    exercise_function = exercises.exercise_014

    initial_number = 1000000
    solution = exercise_function(initial_number)
    assert solution == (837799, 525)

    check_time_exercises(exercise_function, initial_number)


def test_exercise_015():
    exercise_function = exercises.exercise_015

    solutions = [
        1, 2, 6, 20, 70, 252, 924, 3432, 12870, 48620, 184756, 705432, 2704156,
        10400600, 40116600, 155117520, 601080390, 2333606220, 9075135300,
        35345263800, 137846528820, 538257874440, 2104098963720, 8233430727600,
        32247603683100, 126410606437752, 495918532948104, 1946939425648112
    ]

    grid_sizes = np.arange(len(solutions) + 1)

    for grid_size, solution in zip(grid_sizes, solutions):
        exercise_solution = exercise_function(grid_size)
        assert exercise_solution == solution

        check_time_exercises(exercise_function, grid_size)


def test_exercise_016():
    exercise_function = exercises.exercise_016

    exponent = 15
    solution = exercise_function(exponent)
    assert solution == 26
    exponent = 1000
    solution = exercise_function(exponent)
    assert solution == 1366

    check_time_exercises(exercise_function, exponent)


def test_exercise_017():
    exercise_function = exercises.exercise_017

    number_limit = 5
    solution = exercise_function(number_limit)
    assert solution == 19
    number_limit = 1000
    solution = exercise_function(number_limit)
    assert solution == 21124

    check_time_exercises(exercise_function, number_limit)


def test_exercise_018():
    exercise_function = exercises.exercise_018

    solution = exercise_function()
    assert solution == 1074

    check_time_exercises(exercise_function)


def test_exercise_019():
    exercise_function = exercises.exercise_019

    solution = exercise_function()
    assert solution == 171

    check_time_exercises(exercise_function)


def test_exercise_020():
    exercise_function = exercises.exercise_020

    solution = exercise_function(10)
    assert solution == 27

    solution = exercise_function(100)
    assert solution == 648

    check_time_exercises(exercise_function, 100)


def test_exercise_021():
    exercise_function = exercises.exercise_021

    number_limit = 10000
    solution = exercise_function(number_limit)
    assert solution == 31626

    check_time_exercises(exercise_function, number_limit)


def test_exercise_022():
    exercise_function = exercises.exercise_022

    solution = exercise_function()
    assert solution == 871198282

    check_time_exercises(exercise_function)


def test_exercise_023():
    exercise_function = exercises.exercise_023

    solution = exercise_function()
    assert solution == 4179871

    check_time_exercises(exercise_function)


def test_exercise_024():
    exercise_function = exercises.exercise_024

    number_str = "0123456789"
    position = 999999
    solution = exercise_function(number_str, position)
    assert solution == "2783915460"

    check_time_exercises(exercise_function, number_str, position)


def test_exercise_025():
    exercise_function = exercises.exercise_025

    n_digits = 1000
    solution = exercise_function(n_digits)
    assert solution == 4782

    check_time_exercises(exercise_function, n_digits)


def test_exercise_026():
    exercise_function = exercises.exercise_026

    n_digits = 1000
    solution = exercise_function(n_digits)
    assert solution == 983

    check_time_exercises(exercise_function, n_digits)


def test_exercise_027():
    exercise_function = exercises.exercise_027

    solution = exercise_function()
    assert solution == -59231

    check_time_exercises(exercise_function)


def test_exercise_028():
    exercise_function = exercises.exercise_028

    spiral_size = 5
    solution = exercise_function(spiral_size)
    assert solution == 101

    spiral_size = 1001
    solution = exercise_function(spiral_size)
    assert solution == 669171001

    check_time_exercises(exercise_function, spiral_size)


def test_exercise_029():
    exercise_function = exercises.exercise_029

    solution = exercise_function(2, 5, 2, 5)
    assert solution == 15

    solution = exercise_function(2, 100, 2, 100)
    assert solution == 9183

    check_time_exercises(exercise_function, 2, 100, 2, 100)


def test_exercise_030():
    exercise_function = exercises.exercise_030

    n_digits = 4
    solution = exercise_function(n_digits)
    assert solution == 19316

    n_digits = 5
    solution = exercise_function(n_digits)
    assert solution == 443839

    check_time_exercises(exercise_function, n_digits)


def test_exercise_031():
    exercise_function = exercises.exercise_031

    coins_sum = 5
    solution = exercise_function(coins_sum)
    assert solution == 4

    coins_sum = 200
    solution = exercise_function(coins_sum)
    assert solution == 73682

    check_time_exercises(exercise_function, coins_sum)


def test_exercise_034():
    exercise_function = exercises.exercise_034

    solution = exercise_function()
    assert solution == 40730

    check_time_exercises(exercise_function)


def test_exercise_035():
    exercise_function = exercises.exercise_035

    maximum_number = 1000000
    solution = exercise_function(maximum_number)
    assert solution == 55

    check_time_exercises(exercise_function, maximum_number)


def test_exercise_036():
    exercise_function = exercises.exercise_036

    maximum_number = 1000000
    solution = exercise_function(maximum_number)
    assert solution == 872187

    check_time_exercises(exercise_function, maximum_number)


def test_exercise_037():
    exercise_function = exercises.exercise_037

    solution = exercise_function()
    assert solution == 748317

    check_time_exercises(exercise_function)


def test_exercise_039():
    exercise_function = exercises.exercise_039

    solution = exercise_function()
    assert solution == 840

    check_time_exercises(exercise_function)


def test_exercise_040():
    exercise_function = exercises.exercise_040

    decimal_positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    solution = exercise_function(decimal_positions)
    assert solution == 210

    check_time_exercises(exercise_function, decimal_positions)


def test_exercise_041():
    exercise_function = exercises.exercise_041

    solution = exercise_function()
    assert solution == 7652413

    check_time_exercises(exercise_function)


def test_exercise_042():
    exercise_function = exercises.exercise_042

    solution = exercise_function()
    assert solution == 162

    check_time_exercises(exercise_function)


def test_exercise_043():
    exercise_function = exercises.exercise_043

    solution = exercise_function()
    assert solution == 16695334890

    check_time_exercises(exercise_function)


def test_exercise_044():
    exercise_function = exercises.exercise_044

    solution = exercise_function()
    assert solution == 5482660

    check_time_exercises(exercise_function)


def test_exercise_045():
    exercise_function = exercises.exercise_045

    solution = exercise_function()
    assert solution == 1533776805

    check_time_exercises(exercise_function)


def test_exercise_048():
    exercise_function = exercises.exercise_048

    maximum_number = 1000
    solution = exercise_function(maximum_number)
    assert solution == 9110846700

    check_time_exercises(exercise_function, maximum_number)


def test_exercise_049():
    exercise_function = exercises.exercise_049

    solution = exercise_function()
    assert "".join(map(str, solution[0])) == "148748178147"
    assert "".join(map(str, solution[1])) == "296962999629"

    check_time_exercises(exercise_function)


def test_exercise_052():
    exercise_function = exercises.exercise_052

    solution = exercise_function()
    assert solution == 142857

    check_time_exercises(exercise_function)


def test_exercise_053():
    exercise_function = exercises.exercise_053

    solution = exercise_function()
    assert solution == 4075

    check_time_exercises(exercise_function)


def test_exercise_054():
    exercise_function = exercises.exercise_054

    solution = exercise_function()
    assert solution == 376

    check_time_exercises(exercise_function)


def test_exercise_056():
    exercise_function = exercises.exercise_056

    solution = exercise_function()
    assert solution == 972

    check_time_exercises(exercise_function)


def test_exercise_057():
    exercise_function = exercises.exercise_057

    solution = exercise_function()
    assert solution == 153

    check_time_exercises(exercise_function)


def test_exercise_058():
    exercise_function = exercises.exercise_058

    solution = exercise_function()
    assert solution == 26241

    check_time_exercises(exercise_function)

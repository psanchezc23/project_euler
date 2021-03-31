import exercises
import numpy as np


def test_exercise_001():
    numbers = np.array([3, 5])
    maximum_value = 10
    solution = exercises.exercise_001.exercise_001(numbers, maximum_value)
    assert solution == 23

    numbers = np.array([3, 5])
    maximum_value = 1000
    solution = exercises.exercise_001.exercise_001(numbers, maximum_value)
    assert solution == 233168


def test_exercise_002():
    maximum_value = 4000000
    solution = exercises.exercise_002.exercise_002(maximum_value)
    assert solution == 4613732


def test_exercise_003():
    number = 13195
    solution = exercises.exercise_003.exercise_003(number)
    assert solution == 29

    number = 600851475143
    solution = exercises.exercise_003.exercise_003(number)
    assert solution == 6857


def test_exercise_004():
    digits = 2
    solution = exercises.exercise_004.exercise_004(digits)
    assert solution == 9009

    digits = 3
    solution = exercises.exercise_004.exercise_004(digits)
    assert solution == 906609


def test_exercise_005():
    n_divisors = 10
    solution = exercises.exercise_005.exercise_005(n_divisors)
    assert solution == 2520

    n_divisors = 20
    solution = exercises.exercise_005.exercise_005(n_divisors)
    assert solution == 232792560


def test_exercise_006():
    n_natural = 10
    solution = exercises.exercise_006.exercise_006(n_natural)
    assert solution == 2640

    n_natural = 100
    solution = exercises.exercise_006.exercise_006(n_natural)
    assert solution == 25164150


def test_exercise_007():
    n_prime = 6
    solution = exercises.exercise_007.exercise_007(n_prime)
    assert solution == 13

    n_prime = 10001
    solution = exercises.exercise_007.exercise_007_best(n_prime)
    assert solution == 104743


def test_exercise_008():
    n_digits = 4
    solution = exercises.exercise_008.exercise_008(n_digits)
    assert solution == 5832

    n_digits = 13
    solution = exercises.exercise_008.exercise_008(n_digits)
    assert solution == 23514624000


def test_exercise_009():
    triplet_sum = 12
    solution = exercises.exercise_009.exercise_009(triplet_sum)
    assert solution == 60

    triplet_sum = 1000
    solution = exercises.exercise_009.exercise_009(triplet_sum)
    assert solution == 31875000


def test_exercise_010():
    number = 10
    solution = exercises.exercise_010.exercise_010(number)
    assert solution == 17

    number = 2000000
    solution = exercises.exercise_010.exercise_010(number)
    assert solution == 142913828922

import time

import pandas as pd


def exercise_019():
    """
    You are given the following information, but you may prefer to do some
    research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

    :return: Maximum total of adjacent numbers.
    :rtype: int
    """

    dates = pd.date_range("19010101", "20001231", freq="MS")
    return sum([date.weekday() == 6 for date in dates])


if __name__ == '__main__':

    start_time = time.time()
    print(exercise_019())
    end_time = time.time()
    print('{} s'.format(end_time - start_time))

#!/usr/bin/env python3
"""
Utils functions and classes, used by all other files.

In particular, contains
* pd: parse a string into a date
* Run: run objects (RunGoal, RunLong, RunRace, RunShort)
"""
# pylint: disable=invalid-name

from datetime import datetime


def pd(s):
    """
    Parse a string of the form "year-month-day" to a Python date.
    """
    return datetime.strptime(s, '%Y-%m-%d').date()


def date2timestamp(d):
    """
    Convert a Python date to a timestamp.
    """
    return datetime.fromordinal(d.toordinal()).timestamp()


def date_y_eq(a, b):
    """
    Test for equality by year between two dates.
    """
    return a.year == b.year


def date_ym_eq(a, b):
    """
    Test for equality by year and month between two dates.
    """
    return (a.year == b.year) and (a.month == b.month)


def date_yw_eq(a, b):
    """
    Test for equality by year and week number between two dates.
    """
    a_y, a_weekn, _ = a.isocalendar()
    b_y, b_weekn, _ = b.isocalendar()
    return (a_y == b_y) and (a_weekn == b_weekn)


def estimate_time(d1, t1, d2):
    """
    Estimate the time for running distance d2, based on the performance
    (distance, time) (d1, t1). Scaling is not fully linear.

    Based on Peter Riegel's 1981's formula: T2 = T1 * (D2/D1)**1.06
    """
    b = 1.06
    t2 = t1 * (d2 / d1)**b
    return t2


def estimate_distance_at_14_1(d1, t1):
    """
    Estimate the distance that can be achieved by running at 14.1 km/h, based on
    the performance (distance, time) (d1, t1), using Peter Riegel's 1981's
    formula.

    Can not solve it mathematically, wolframalpha says:
        d2 = 10**-19 * d1**(53/3) / t1**(50/3)
        d2 = 10**-19 * d1**(1.06*50/3) / t1**(50/3)
    Big coeff are imprecise, using an iterative solution instead.
    """

    if d1 == 0:
        return 0

    for d in range(1, 42200+1, 100):
        d2 = d/1000
        t2 = estimate_time(d1, t1, d2)

        if d2/t2 < 14.1:
            return d2

    return 42.2


class Run:
    """
    Represent a run, with, among other attributes, distance and time.

    Several attributes are automatically computed, such as marathon-related
    statistics.
    """
    def __init__(self, date, distance, time_mn, temp):
        self.date = date
        self.distance = distance
        self.time_h = time_mn/60
        self.temp = temp

        self.speed = self.distance / self.time_h
        self.hm_time = estimate_time(self.distance, self.time_h, 21.1)
        self.hm_speed = 21.1 / self.hm_time
        self.m_time = estimate_time(self.distance, self.time_h, 42.2)
        self.m_speed = 42.2 / self.m_time
        self.dist_at_14_1_kmph = estimate_distance_at_14_1(self.distance, self.time_h)


class RunGoal(Run):
    # pylint: disable=too-few-public-methods
    pass


class RunLong(Run):
    # pylint: disable=too-few-public-methods
    pass


class RunRace(Run):
    # pylint: disable=too-few-public-methods
    pass


class RunRelax(Run):
    # pylint: disable=too-few-public-methods
    pass


class RunShort(Run):
    # pylint: disable=too-few-public-methods
    pass

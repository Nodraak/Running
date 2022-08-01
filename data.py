#!/usr/bin/env python3

from collections import namedtuple
from datetime import datetime


def date2datetime(d):
    return datetime.fromordinal(d.toordinal())


def pd(s):
    return datetime.strptime(s, '%Y-%m-%d').date()


RunShort = namedtuple("RunShort", ("date", "distance", "speed", "temp"))
RunLong = namedtuple("RunLong", ("date", "distance", "speed", "temp"))
RunRace = namedtuple("RunRace", ("date", "distance", "speed", "temp"))


RUNS = (
    RunShort(pd('2021-03-27'), 4.14, 10.6, None),

    # 8 runs - 55 km
    RunShort(pd('2021-04-02'), 6.42, 11.2, None),
    RunShort(pd('2021-04-08'), 6.45, 11.4, None),
    RunLong(pd('2021-04-11'), 7.24, 11.0, None),
    RunShort(pd('2021-04-14'), 3.9, 7.5, None),
    RunLong(pd('2021-04-18'), 3.3, 10.0, None),
    RunShort(pd('2021-04-22'), 7.8, 11.9, None),
    RunLong(pd('2021-04-24'), 11.3, 11.8, None),  # 8
    RunShort(pd('2021-04-27'), 6.6, 11.6, None),  # 9

    # 12 runs - 110 km
    RunLong(pd('2021-05-01'), 13.5, 12.0, None),  # 10
    RunShort(pd('2021-05-06'), 6.0, 12.4, None),  # 11
    RunLong(pd('2021-05-08'), 14.4, 11.9, None),  # 12
    RunShort(pd('2021-05-12'), 5.8, 12.3, None),  # 13
    RunShort(pd('2021-05-14'), 6.4, 12.6, None),  # 14
    RunLong(pd('2021-05-15'), 15.0, 11.4, None),  # 15
    RunShort(pd('2021-05-18'), 5.8, 12.0, None),  # 16
    RunShort(pd('2021-05-20'), 4.0, 12.0, None),  # 17 - Strides
    RunLong(pd('2021-05-23'), 17.0, 10.7, None),  # 18
    RunShort(pd('2021-05-25'), 6.2, 12.4, None),  # 19
    RunShort(pd('2021-05-27'), 6.2, 12.8, None),  # 20
    RunLong(pd('2021-05-28'), 13.6, 12.4, None),  # 21

    # 09 - 17 km
    RunLong(pd('2021-09-18'), 7, 12.2, None),
    RunLong(pd('2021-09-25'), 9.6, 10.7, None),

    # 10 - 30 km
    RunLong(pd('2021-10-02'), 10.6, 11.8, 15),
    RunLong(pd('2021-10-09'), 11.7, 11.5, 12),
    RunLong(pd('2021-10-17'), 7.9, 12.2, 11),

    # 2 runs - 15 km
    RunShort(pd('2022-01-02'), 7.8, 11.2, 13),
    RunShort(pd('2022-01-09'), 7.8, 11.2, None),

    # 3 runs - 25 km
    RunShort(pd('2022-02-12'), 6, 12, 6),
    RunShort(pd('2022-02-19'), 5.8, 12.5, 6),
    RunLong(pd('2022-02-26'), 11.2, 12.0, 7),

    # 5 runs - 50 km
    RunLong(pd('2022-03-08'), 12, 12, 6),
    RunLong(pd('2022-03-12'), 12, 12, 10),
    RunLong(pd('2022-03-19'), 12, 12, 10),
    RunLong(pd('2022-03-27'), 12, 12, 10),
    RunShort(pd('2022-03-29'), 5.7, 12.6, None),

    # 9 runs - 120 km
    RunLong(pd('2022-04-06'), 14.9, 11.9, 10),
    RunLong(pd('2022-04-09'), 15.3, 12.2, 8),
    RunShort(pd('2022-04-13'), 7.5, 12.1, None),
    RunLong(pd('2022-04-15'), 18, 12, 10),
    RunShort(pd('2022-04-18'), 11.9, 12.3, 15),
    RunRace(pd('2022-04-24'), 21.1, 11.99, 14),  # Race - half marathon
    RunShort(pd('2022-04-26'), 6, 12.4, 14),
    RunShort(pd('2022-04-28'), 6, 13.1, 14),
    RunLong(pd('2022-04-30'), 18.55, 12.3, 16),

    # 8 runs - 100 km
    RunShort(pd('2022-05-03'), 9, 13.1, 10),
    RunLong(pd('2022-05-07'), 22.3, 12.2, 16),
    RunShort(pd('2022-05-12'), 9, 13.3, 16),
    RunLong(pd('2022-05-15'), 10.3, 11.7, 17),
    RunShort(pd('2022-05-18'), 11.7, 12.7, 20),
    RunLong(pd('2022-05-21'), 15.6, 12.5, 18),
    RunLong(pd('2022-05-28'), 18.0, 11.9, 12),
    RunShort(pd('2022-05-31'), 6, 13.7, 10),

    # 9 runs - 110 km
    RunShort(pd('2022-06-02'), 9, 13.0, 18),
    RunLong(pd('2022-06-04'), 18.0, 12.0, 19),
    RunShort(pd('2022-06-09'), 11.7, 13.5, 18),
    RunShort(pd('2022-06-14'), 9, 13.6, 18),
    RunShort(pd('2022-06-16'), 9, 14.0, 22),
    RunLong(pd('2022-06-18'), 15, 12.8, 26),
    RunShort(pd('2022-06-24'), 12, 13.50, 20),
    RunLong(pd('2022-06-25'), 18, 12.5, 21),
    RunShort(pd('2022-06-28'), 12, 14.03, 24),

    # 11 runs - 150 km (TBC)
    RunShort(pd('2022-07-01'), 12, 13.70, 23),
    RunLong(pd('2022-07-02'), 18, 13.31, 21),
    RunShort(pd('2022-07-05'), 12, 13.90, 19),
    RunShort(pd('2022-07-08'), 12, 14.45, 15), # PB - 12k
    RunShort(pd('2022-07-09'), 15, 13.50, 18),
    RunLong(pd('2022-07-12'), 18, 13.42, 16), # PB - 18k
    RunShort(pd('2022-07-16'), 9, 12.85, 22),  # Note - mauvaise respiration
    RunShort(pd('2022-07-18'), 12, 13.60, 18),  # Note - mauvaise respiration
    RunShort(pd('2022-07-22'), 6, 13.90, 20),  # Note - 2x 25 m de denivele
    RunRace(pd('2022-07-24'), 20, 13.45, 22), # Race - 20 km CDGR



    # 08: 12 runs - 200-220 km (TBC)
    # 09: 12 runs - 240 km (TBC)
    # 10: 12 runs - 240 km (TBC)
    # 11: 12 runs - 160 km (TBC)

    # 2022-11-27 half marathon Boulogne
    # 2023-04-02 Marathon Paris
)

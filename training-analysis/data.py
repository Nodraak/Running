#!/usr/bin/env python3
"""
Run data.
"""

from utils import pd, RunGoal, RunLong, RunRace, RunRelax, RunShort


RUNS = (
    #
    # 2020
    # Carrera de las empresas
    #

    RunShort(pd('2020-11-29'), 4.7, 25, None),
    RunShort(pd('2020-12-02'), 3.0, 20, None),
    RunShort(pd('2020-12-04'), 6.6, 34, None),
    RunShort(pd('2020-12-09'), 6.7, 40, None),
    RunShort(pd('2020-12-11'), 5.2, 27, None),
    RunRace(pd('2020-12-15'), 6.5, 33, None),

    #
    # 2021
    # Marathon try 1 - Too much, too quickly
    #

    RunShort(pd('2021-03-27'), 4.14, 23.00, None),

    # 8 runs - 55 km
    RunShort(pd('2021-04-02'), 6.42, 35.00, None),
    RunShort(pd('2021-04-08'), 6.45, 34.00, None),
    RunLong(pd('2021-04-11'), 7.24, 42.00, None),
    RunShort(pd('2021-04-14'), 3.9, 33.00, None),
    RunLong(pd('2021-04-18'), 3.3, 20.00, None),
    RunShort(pd('2021-04-22'), 7.8, 39.00, None),
    RunLong(pd('2021-04-24'), 11.3, 58.00, None),  # 8
    RunShort(pd('2021-04-27'), 6.6, 34.14, None),  # 9

    # 12 runs - 110 km
    RunLong(pd('2021-05-01'), 13.5, 68.00, None),  # 10
    RunShort(pd('2021-05-06'), 6.0, 28.00, None),  # 11
    RunLong(pd('2021-05-08'), 14.4, 72.00, None),  # 12
    RunShort(pd('2021-05-12'), 5.8, 28.00, None),  # 13
    RunShort(pd('2021-05-14'), 6.4, 30.00, None),  # 14
    RunLong(pd('2021-05-15'), 15.0, 79.00, None),  # 15
    RunShort(pd('2021-05-18'), 5.8, 29.00, None),  # 16
    RunShort(pd('2021-05-20'), 4.0, 20.00, None),  # 17 - Strides
    RunLong(pd('2021-05-23'), 17.0, 95.00, None),  # 18
    RunShort(pd('2021-05-25'), 6.2, 30.00, None),  # 19
    RunShort(pd('2021-05-27'), 6.2, 29.00, None),  # 20
    RunLong(pd('2021-05-28'), 13.6, 66.00, None),  # 21

    RunLong(pd('2021-06-23'), 5.8, 30.00, 15),

    # 09 - 17 km
    RunLong(pd('2021-09-18'), 7, 34.00, None),
    RunLong(pd('2021-09-25'), 9.6, 54.00, None),

    # 10 - 30 km
    RunLong(pd('2021-10-02'), 10.6, 54.00, 15),
    RunLong(pd('2021-10-09'), 11.7, 61.00, 12),
    RunLong(pd('2021-10-17'), 7.9, 38.00, 11),

    #
    # 2022
    # Several half-marathon. Ready for Marathon, but too late for Berlin, waiting Paris 2023-04.
    #

    # 2 runs - 15 km
    RunShort(pd('2022-01-02'), 7.8, 42.00, 13),
    RunShort(pd('2022-01-09'), 7.8, 42.00, None),

    # 3 runs - 25 km
    RunShort(pd('2022-02-12'), 6, 30.00, 6),
    RunShort(pd('2022-02-19'), 5.8, 27.00, 6),
    RunLong(pd('2022-02-26'), 11.2, 55.00, 7),

    # 5 runs - 50 km
    RunLong(pd('2022-03-08'), 12, 60.00, 6),
    RunLong(pd('2022-03-12'), 12, 60.00, 10),
    RunLong(pd('2022-03-19'), 12, 60.00, 10),
    RunLong(pd('2022-03-27'), 12, 60.00, 10),
    RunShort(pd('2022-03-29'), 5.7, 27.00, None),

    # 9 runs - 120 km
    RunLong(pd('2022-04-06'), 14.9, 75.00, 10),
    RunLong(pd('2022-04-09'), 15.3, 75.00, 8),
    RunShort(pd('2022-04-13'), 7.5, 37.00, None),
    RunLong(pd('2022-04-15'), 18.0, 90.00, 10),
    RunShort(pd('2022-04-18'), 11.9, 58.00, 15),
    RunRace(pd('2022-04-24'), 21.1, 105.50, 14),  # Race Spreewald - 21.1k: 12 km/h
    RunShort(pd('2022-04-26'), 6.0, 29.00, 14),
    RunShort(pd('2022-04-28'), 6.0, 27.00, 14),
    RunLong(pd('2022-04-30'), 18.55, 90.00, 16),

    # 8 runs - 100 km
    RunShort(pd('2022-05-03'), 9, 41.00, 10),
    RunLong(pd('2022-05-07'), 22.3, 109.00, 16),
    RunShort(pd('2022-05-12'), 9, 40.00, 16),
    RunLong(pd('2022-05-15'), 10.3, 53.00, 17),
    RunShort(pd('2022-05-18'), 11.7, 55.00, 20),
    RunLong(pd('2022-05-21'), 15.6, 75.00, 18),
    RunLong(pd('2022-05-28'), 18.0, 91.00, 12),
    RunShort(pd('2022-05-31'), 6, 26.00, 10),

    # 9 runs - 110 km
    RunShort(pd('2022-06-02'), 9, 41.30, 18),
    RunLong(pd('2022-06-04'), 18.0, 90.00, 19),
    RunShort(pd('2022-06-09'), 11.7, 52.00, 18),
    RunShort(pd('2022-06-14'), 9, 39.70, 18),
    RunShort(pd('2022-06-16'), 9, 38.50, 22),
    RunLong(pd('2022-06-18'), 15, 71.00, 26),
    RunShort(pd('2022-06-24'), 12, 53.30, 20),
    RunLong(pd('2022-06-25'), 18, 89.00, 21),
    RunShort(pd('2022-06-28'), 12, 51.30, 24),

    # 12 runs - 150 km
    RunShort(pd('2022-07-01'), 12, 52.50, 23),
    RunLong(pd('2022-07-02'), 18, 81.10, 21),
    RunShort(pd('2022-07-05'), 12, 51.90, 19),
    RunShort(pd('2022-07-08'), 12, 49.83, 15),
    RunShort(pd('2022-07-09'), 15, 66.60, 18),
    RunLong(pd('2022-07-12'), 18, 80.50, 16),
    RunRelax(pd('2022-07-16'), 9, 42.00, 22),  # Note - mauvaise respiration
    RunRelax(pd('2022-07-18'), 12, 53.00, 18),  # Note - mauvaise respiration
    RunRelax(pd('2022-07-22'), 6, 25.90, 20),  # Note - 2x 25 m de denivele
    RunRace(pd('2022-07-24'), 20, 89.33, 22), # Race CDGR - 20k: 13.43 km/h
    RunShort(pd('2022-07-26'), 6, 25.30, 19),
    RunShort(pd('2022-07-28'), 9, 37.66, 20),

    # 12 runs - 160 km
    RunShort(pd('2022-08-01'), 12, 50.67, 21),
    RunShort(pd('2022-08-05'), 13.50, 59.50, 20),
    RunShort(pd('2022-08-08'), 12, 52.80, 17),
    RunShort(pd('2022-08-12'), 12, 52.80, 19),
    RunLong(pd('2022-08-13'), 15, 67.00, 24),
    RunShort(pd('2022-08-16'), 12, 51.00, 20),
    RunLong(pd('2022-08-20'), 15, 65.50, 21),
    RunShort(pd('2022-08-21'),  6, 24.80, 19),
    RunShort(pd('2022-08-23'), 15, 65.00, 18),
    RunShort(pd('2022-08-26'), 15, 65.50, 21),
    RunLong(pd('2022-08-28'), 21, 95.00, 20),
    RunShort(pd('2022-08-30'), 15, 64.90, 16),

    # 10 runs - 160 km
    RunShort(pd('2022-09-03'), 15, 67.90, 21),
    RunShort(pd('2022-09-05'), 15, 63.50, 15),
    RunShort(pd('2022-09-08'), 15, 66.00, 15),
    RunLong(pd('2022-09-10'), 25, 116.5, 19),
    RunShort(pd('2022-09-13'), 12, 50.85, 16),
    RunShort(pd('2022-09-16'), 15, 63.30, 10),
    RunLong(pd('2022-09-17'), 27, 122.83, 15),
    RunShort(pd('2022-09-20'), 15, 64.30, 9),
    RunShort(pd('2022-09-23'), 9, 36.63, 7),
    RunLong(pd('2022-09-25'), 15, 64.58, 17),

    # 9 runs - 140 km
    RunShort(pd('2022-10-04'), 15, 62.00, 11), # PB - 15k: 14.50 km/h (21.1k: 14.22)
    RunRelax(pd('2022-10-07'), 15, 65.75, 9),
    RunLong(pd('2022-10-09'), 21, 90.50, 15),
    RunShort(pd('2022-10-12'), 15, 63.13, 15),
    RunRelax(pd('2022-10-14'), 15, 68.00, 15),
    RunRelax(pd('2022-10-19'), 15, 65.28, 13),
    RunRace(pd('2022-10-23'), 21.1, 89.88, 15),  # Race Mueggelsee - 21.1k: 14.1 km/h
    RunRelax(pd('2022-10-28'), 6, 26.75, 13),
    RunRelax(pd('2022-10-30'), 12, 52.20, 20),

    # 12 runs - 160-180 km (TBC)



    # Goals
    RunGoal(pd('2022-11-27'), 21.1, 88, None), # Boulogne (ready for 3h marathon)
    RunGoal(pd('2023-04-02'), 42.2, 180, None), # Paris (3h marathon)
)

#!/usr/bin/env python3
"""
Run data.
"""

from utils import pd, RunGoal, RunLong, RunRace, RunRelax, RunShort, RunCross


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
    RunShort(pd('2022-10-04'), 15, 62.00, 11),
    RunRelax(pd('2022-10-07'), 15, 65.75, 9),
    RunLong(pd('2022-10-09'), 21, 90.50, 15),
    RunShort(pd('2022-10-12'), 15, 63.13, 15),
    RunRelax(pd('2022-10-14'), 15, 68.00, 15),
    RunRelax(pd('2022-10-19'), 15, 65.28, 13),
    RunRace(pd('2022-10-23'), 21.1, 89.88, 15),  # Race Mueggelsee - 21.1k: 14.10 km/h
    RunRelax(pd('2022-10-28'), 6, 26.75, 13),
    RunRelax(pd('2022-10-30'), 12, 52.20, 20),

    # 10 runs - 120 km
    RunShort(pd('2022-11-01'), 15, 63.97, 18),
    RunRelax(pd('2022-11-05'), 15, 63.78, 8),
    RunShort(pd('2022-11-08'), 6, 24.6, 10),
    RunShort(pd('2022-11-10'), 9.4, 39.33, 11),
    RunRelax(pd('2022-11-12'), 15, 64.07, 13),
    RunShort(pd('2022-11-14'), 15, 63.00, 7),
    RunCross(pd('2022-11-21'), 40),  # ice skating
    RunShort(pd('2022-11-24'), 12, 51.50, 6),
    RunRelax(pd('2022-11-26'), 5.9, 26.50, 8),
    RunRace(pd('2022-11-27'), 21.1, 89.47, 7), # Race Boulogne - 21.1k: 14.15 km/h

    # 6 runs - 55 km
    RunCross(pd('2022-12-01'), 40),  # ice skating
    RunRelax(pd('2022-12-10'), 9.6, 48.00, -1),  # track
    RunShort(pd('2022-12-14'), 5.9, 24.50, -3),  # KMN
    RunRelax(pd('2022-12-21'), 8.8, 40.00, 10),
    RunShort(pd('2022-12-27'), 11.9, 51.80, 8),
    RunShort(pd('2022-12-29'), 12, 50.3, 12),

    #
    # 2023-S1
    # Several half-marathon (sub 1h30). Preparing for Paris 2023-04 and Berlin 2023-09 (sub 3h).
    #

    # 12 runs - 180 km
    RunRelax(pd('2023-01-03'), 12.0, 60, 7),
    RunRelax(pd('2023-01-05'), 7.0, 35, 7),
    RunLong(pd('2023-01-07'), 18.6, 78.50, 7),
    RunShort(pd('2023-01-10'), 9.7, 40.8, 8),
    RunCross(pd('2023-01-10'), 30),  # ice skating - with new ice skates, very nice
    RunShort(pd('2023-01-13'), 13.4, 60.0, 10),  # strides, best 1.1 / 4:10 = 15.8
    RunLong(pd('2023-01-14'), 15.0, 64.0, 8),
    RunRelax(pd('2023-01-18'), 12.0, 57, 1),
    RunRelax(pd('2023-01-19'), 7.0, 34, 3),
    RunLong(pd('2023-01-20'), 24.9, 115.0, 0),
    RunShort(pd('2023-01-24'), 12.0, 50.5, 1),
    RunRelax(pd('2023-01-26'), 14.8, 68.75, 1),
    RunLong(pd('2023-01-28'), 27.5, 123.0, 1),

    # 16 runs - 250 km
    RunShort(pd('2023-02-02'), 15.0, 67.25, 7),
    RunRelax(pd('2023-02-03'), 12.0, 52.0, 7),
    RunLong(pd('2023-02-04'), 25.3, 115.0, 3),
    RunRelax(pd('2023-02-06'), 12.0, 54.0, 0),
    RunShort(pd('2023-02-09'), 15.0, 63.5, 2),
    RunRelax(pd('2023-02-10'), 12.0, 53.0, 5),
    RunRelax(pd('2023-02-11'), 12.0, 54.5, 5),
    RunShort(pd('2023-02-13'), 15.0, 61.7, 8),  # PB - 15k: 14.60 (21.1k: 14.30 km/h)
    RunCross(pd('2023-02-13'), 45),  # ice skating - (inner) schnell bahn
    RunRelax(pd('2023-02-14'), 11.3, 49.0, 7),
    RunCross(pd('2023-02-15'), 60),  # 2h swing
    RunLong(pd('2023-02-16'), 34.0, 156.0, 11),
    RunRelax(pd('2023-02-19'), 6.3, 30.0, 5),
    RunRelax(pd('2023-02-21'), 15.0, 65.0, 11),
    RunLong(pd('2023-02-22'), 25.4, 119.0, 8),
    RunCross(pd('2023-02-22'), 30),  # 1h swing

    RunCross(pd('2023-02-26'), 30),  # ski 6h
    RunCross(pd('2023-02-27'), 30),  # ski 6h
    RunCross(pd('2023-02-28'), 30),  # ski 6h
    RunCross(pd('2023-02-28'), 40),  # piscine 40 mn

    # 8 runs - 70 km
    RunCross(pd('2023-03-02'), 30),  # ski 4h
    RunCross(pd('2023-03-03'), 30),  # ski 4h
    RunCross(pd('2023-03-03'), 60),  # rando 2h
    RunRelax(pd('2023-03-11'), 6.0, 26.0, 2),
    RunRelax(pd('2023-03-16'), 15.0, 67.25, 9),
    RunRelax(pd('2023-03-17'), 9.1, 39.0, 13),
    RunLong(pd('2023-03-19'), 26.2, 120.0, 14),
    RunRelax(pd('2023-03-31'), 6.0, 30.0, None),

    RunRace(pd('2023-04-02'), 42.2, 3*60 + 44 + 42/60, 8),

    #
    # 2023-S2
    # Preparing for Berlin 2023-09 (goal sub 3h)
    #

    RunRelax(pd('2023-04-24'), 12.0, 56, 15),

    RunRelax(pd('2023-05-11'), 6.0, 28, 18),
    RunRelax(pd('2023-05-13'), 6.0, 27, 18),
    RunRelax(pd('2023-05-17'), 12.0, 54.5, 15),
    RunLong(pd('2023-05-20'), 18.6, 91.5, 15),
    RunShort(pd('2023-05-24'), 12.0, 54.5, 15),

    # 9 runs - 60 km
    RunShort(pd('2023-06-02'), 6.0, 28, 14),
    RunShort(pd('2023-06-04'), 6.3, 29.5, 17),
    RunShort(pd('2023-06-07'), 6.0, 28, None),
    RunShort(pd('2023-06-10'), 6.0, 26.3, 19),
    RunShort(pd('2023-06-14'), 6.0, 26.5, 19),
    RunShort(pd('2023-06-22'), 6.0, 27.0, 25),
    RunShort(pd('2023-06-24'), 6.0, 25.9, 18),
    RunRelax(pd('2023-06-27'), 9.0, 40.0, 15),
    RunRelax(pd('2023-06-30'), 9.0, 41.5, 19),

    # (12-16 runs - 180-250 km)
    RunLong(pd('2023-07-01'), 9.0, 41, 22),


    # (16-20 runs - 250-300 km)
    # (8-12 runs - 70-150 km)



    # Goals
    RunGoal(pd('2023-09-24'), 42.2, 180, None), # Berlin (3h marathon)
    RunGoal(pd('2023-09-24'), 21.1, 86.33, None), # Berlin (3h marathon) = HM: 14.66
    RunGoal(pd('2023-09-24'), 15, 60.13, None), # Berlin (3h marathon) = 15 km: 14.97
)

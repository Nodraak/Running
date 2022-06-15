from collections import namedtuple
from datetime import datetime

def pd(s):
    return datetime.strptime(s, '%Y-%m-%d').date()


RunShort = namedtuple("RunShort", ("date", "distance", "speed"))
RunLong = namedtuple("RunLong", ("date", "distance", "speed"))


RUNS_2021 = (
    RunShort(pd('2021-03-27'), 4.14, 10.6),

    # 8 runs - 55 km
    RunShort(pd('2021-04-02'), 6.42, 11.2),
    RunShort(pd('2021-04-08'), 6.45, 11.4),
    RunLong(pd('2021-04-11'), 7.24, 11.0),
    RunShort(pd('2021-04-14'), 3.9, 7.5),
    RunLong(pd('2021-04-18'), 3.3, 10.0),
    RunShort(pd('2021-04-22'), 7.8, 11.9),
    RunLong(pd('2021-04-24'), 11.3, 11.8),  # 8
    RunShort(pd('2021-04-27'), 6.6, 11.6),  # 9

    # 12 runs - 110 km
    RunLong(pd('2021-05-01'), 13.5, 12.0),  # 10
    RunShort(pd('2021-05-06'), 6.0, 12.4),  # 11
    RunLong(pd('2021-05-08'), 14.4, 11.9),  # 12
    RunShort(pd('2021-05-12'), 5.8, 12.3),  # 13
    RunShort(pd('2021-05-14'), 6.4, 12.6),  # 14
    RunLong(pd('2021-05-15'), 15.0, 11.4),  # 15
    RunShort(pd('2021-05-18'), 5.8, 12.0),  # 16
    RunShort(pd('2021-05-20'), 4.0, 12.0),  # 17 - Strides
    RunLong(pd('2021-05-23'), 17.0, 10.7),  # 18
    RunShort(pd('2021-05-25'), 6.2, 12.4),  # 19
    RunShort(pd('2021-05-27'), 6.2, 12.8),  # 20
    RunLong(pd('2021-05-28'), 13.6, 12.4),  # 21
)

RUNS_2022 = (
    # 2 runs - 15 km
    RunShort(pd('2022-01-02'), 7.8, 11.2),
    RunShort(pd('2022-01-09'), 7.8, 11.2),

    # 3 runs - 25 km
    RunShort(pd('2022-02-12'), 6, 12),
    RunShort(pd('2022-02-19'), 5.8, 12.5),
    RunLong(pd('2022-02-26'), 11.2, 12.0),

    # 5 runs - 50 km
    RunLong(pd('2022-03-08'), 12, 12),
    RunLong(pd('2022-03-12'), 12, 12),
    RunLong(pd('2022-03-19'), 12, 12),
    RunLong(pd('2022-03-27'), 12, 12),
    RunShort(pd('2022-03-29'), 5.7, 12.6),

    # 9 runs - 120 km
    RunLong(pd('2022-04-06'), 14.9, 11.9),
    RunLong(pd('2022-04-09'), 15.3, 12.2),
    RunShort(pd('2022-04-13'), 7.5, 12.1),
    RunLong(pd('2022-04-15'), 18, 12),
    RunShort(pd('2022-04-18'), 11.9, 12.3),
    RunLong(pd('2022-04-24'), 21.1, 11.99),  # half marathon
    RunShort(pd('2022-04-26'), 6, 12.4),
    RunShort(pd('2022-04-28'), 6, 13.1),
    RunLong(pd('2022-04-30'), 18.55, 12.3),

    # 8 runs - 100 km
    RunShort(pd('2022-05-03'), 9, 13.1),
    RunLong(pd('2022-05-07'), 22.3, 12.2),
    RunShort(pd('2022-05-12'), 9, 13.3),
    RunLong(pd('2022-05-15'), 10.3, 11.7),
    RunShort(pd('2022-05-18'), 11.7, 12.7),
    RunLong(pd('2022-05-21'), 15.6, 12.5),
    RunLong(pd('2022-05-28'), 18.0, 11.9),
    RunShort(pd('2022-05-31'), 6, 13.7),

    # 11 runs - 150 km (TBC)
    RunShort(pd('2022-06-02'), 9, 13.0),
    RunLong(pd('2022-06-04'), 18.0, 12.0),
    RunShort(pd('2022-06-09'), 11.7, 13.5),
    RunShort(pd('2022-06-14'), 9, 13.6),

    # 12 runs - 170 km (TBC)

)


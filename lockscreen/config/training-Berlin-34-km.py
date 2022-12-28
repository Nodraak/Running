#!/usr/bin/env python3
"""
Theory: long run pace is marathon pace +40 sec/km / +20%
For a 13.0-14.0 (4:15-4:30) marathon, that's 11.0-12.0 (5:00-5:30).

Note: over 5 km, +/- 1 min = +/- 0.5 km/h

# Stdout

checkpoint_calc_and_format_time: cp= 5.8 dd= 5.8 dt=1604 v=12.90
checkpoint_calc_and_format_time: cp=10.2 dd= 4.4 dt=1187 v=13.34
checkpoint_calc_and_format_time: cp=15.0 dd= 4.8 dt=1319 v=13.24
checkpoint_calc_and_format_time: cp=19.8 dd= 4.8 dt=1310 v=13.05
checkpoint_calc_and_format_time: cp=25.1 dd= 5.4 dt=1491 v=12.91
checkpoint_calc_and_format_time: cp=30.3 dd= 5.2 dt=1467 v=12.76
checkpoint_calc_and_format_time: cp=34.0 dd= 3.7 dt=1045 v=12.75
"""

CONF = {
    "RACE_DIST_KM": 34.0,
    "RACE_GOAL_TIME_S": 157*60,  # 157 = 13.0 km/h ; 151 = 13.5 km/h
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "{time:5s}  {dist:4.1f} Usual",         "kwargs": {"dist":  5.75}, "plt_kwargs": {"color": "gray"}},  #  26.8
        {"fmt": "{time:5s}  {dist:4.1f} Bridge",        "kwargs": {"dist": 10.15}, "plt_kwargs": {"color": "gray"}},  #  46.5
        {"fmt": "{time:5s}  {dist:4.1f} Corner Kirche", "kwargs": {"dist": 15.00}, "plt_kwargs": {"color": "blue"}},  #  68.5
        {"fmt": "{time:5s}  {dist:4.1f} Corner Ampel",  "kwargs": {"dist": 19.75}, "plt_kwargs": {"color": "blue"}},  #  90.3
        {"fmt": "{time:5s}  {dist:4.1f} A-HSH",         "kwargs": {"dist": 25.10}, "plt_kwargs": {"color": "blue"}},  # 115.2
        {"fmt": "{time:5s}  {dist:4.1f} Tram",          "kwargs": {"dist": 30.30}, "plt_kwargs": {"color": "blue"}},  # 139.7
        {"fmt": "{time:5s}  {dist:4.1f} End",           "kwargs": {"dist": 34.00}, "plt_kwargs": {"color": "gray"}},  # 157.0
    ),
    "TEXT_BOTTOM_LEFT": (
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
    ),
}

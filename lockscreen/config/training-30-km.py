#!/usr/bin/env python3
"""
# Stdout

checkpoint_calc_and_format_time: cp= 5.8 dd= 5.8 dt=1624 v=12.75
checkpoint_calc_and_format_time: cp=10.2 dd= 4.4 dt=1204 v=13.15
checkpoint_calc_and_format_time: cp=15.0 dd= 4.8 dt=1333 v=13.09
checkpoint_calc_and_format_time: cp=19.8 dd= 4.8 dt=1335 v=12.81
checkpoint_calc_and_format_time: cp=24.3 dd= 4.6 dt=1285 v=12.75
checkpoint_calc_and_format_time: cp=30.0 dd= 5.7 dt=1621 v=12.66
"""

CONF = {
    "RACE_DIST_KM": 30.0,
    "RACE_GOAL_TIME_S": 140*60,  # 12.8 km/h
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "{time:5s}  {dist:4.1f} usual",         "kwargs": {"dist":  5.75},  "plt_kwargs": {"color": "gray"}},  # 26.5
        {"fmt": "{time:5s}  {dist:4.1f} bridge",        "kwargs": {"dist": 10.15},  "plt_kwargs": {"color": "gray"}},  # 46.8
        {"fmt": "{time:5s}  {dist:4.1f} corner Kirche", "kwargs": {"dist": 15.00},  "plt_kwargs": {"color": "blue"}},  # 69.2
        {"fmt": "{time:5s}  {dist:4.1f} corner Ampel",  "kwargs": {"dist": 19.75},  "plt_kwargs": {"color": "blue"}},  # 91.1
        {"fmt": "{time:5s}  {dist:4.1f} usual",         "kwargs": {"dist": 24.30},  "plt_kwargs": {"color": "blue"}},  # 112.1
        {"fmt": "{time:5s}  {dist:4.1f} end",           "kwargs": {"dist": 30.00},  "plt_kwargs": {"color": "gray"}},  # 138.4
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
    ),
    "TEXT_BOTTOM_LEFT": (
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                    "kwargs": {},               "plt_kwargs": {"color": "gray"}},
    ),
}

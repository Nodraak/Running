#!/usr/bin/env python3
"""
# Stdout

RACE_GOAL_TIME_S=87:
checkpoint_calc_and_format_time: cp= 5.0 dd= 5.0 dt=1266 v=14.22
checkpoint_calc_and_format_time: cp=10.0 dd= 5.0 dt=1214 v=14.83
checkpoint_calc_and_format_time: cp=15.0 dd= 5.0 dt=1229 v=14.64
checkpoint_calc_and_format_time: cp=21.1 dd= 6.1 dt=1511 v=14.53

RACE_GOAL_TIME_S=88:
checkpoint_calc_and_format_time: cp= 5.0 dd= 5.0 dt=1280 v=14.06
checkpoint_calc_and_format_time: cp=10.0 dd= 5.0 dt=1228 v=14.66
checkpoint_calc_and_format_time: cp=15.0 dd= 5.0 dt=1244 v=14.47
checkpoint_calc_and_format_time: cp=21.1 dd= 6.1 dt=1529 v=14.36
"""

CONF = {
    "RACE_DIST_KM": 21.1,
    "RACE_GOAL_TIME_S": 87*60,
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        # 2
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",    "kwargs": {"dist":  5.0}, "plt_kwargs": {"color": "gray"}},
        # 7
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",    "kwargs": {"dist": 10.0}, "plt_kwargs": {"color": "gray"}},
        # 12
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",    "kwargs": {"dist": 15.0}, "plt_kwargs": {"color": "gray"}},
    ),
    "TEXT_BOTTOM_LEFT": (
        # 17
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        # 18
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        # 19
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        # 20
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Finish",   "kwargs": {"dist": 21.1}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
    ),
}

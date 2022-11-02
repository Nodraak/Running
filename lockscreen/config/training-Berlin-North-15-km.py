#!/usr/bin/env python3
"""
# Stdout

checkpoint_calc_and_format_time: cp= 1.0 dd= 1.0 dt= 294 v=12.26
checkpoint_calc_and_format_time: cp= 3.1 dd= 2.1 dt= 491 v=15.40
checkpoint_calc_and_format_time: cp= 5.8 dd= 2.7 dt= 633 v=15.35
checkpoint_calc_and_format_time: cp= 9.5 dd= 3.7 dt= 874 v=15.25
checkpoint_calc_and_format_time: cp=12.4 dd= 2.9 dt= 689 v=15.15
checkpoint_calc_and_format_time: cp=15.0 dd= 2.6 dt= 620 v=15.11
"""

CONF = {
    "RACE_DIST_KM": 15.0,
    "RACE_GOAL_TIME_S": 60*60,
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",        "kwargs": {"dist":  1.0}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",        "kwargs": {"dist":  3.1}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",        "kwargs": {"dist":  5.8}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",        "kwargs": {"dist":  9.5}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",        "kwargs": {"dist": 12.4}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",        "kwargs": {"dist": 15.0}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                "kwargs": {},             "plt_kwargs": {"color": "gray"}},
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

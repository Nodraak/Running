#!/usr/bin/env python3
"""
# Stdout

RACE_GOAL_TIME_S=84:
checkpoint_calc_and_format_time: cp= 5.0 dd= 5.0 dt=1224 v=14.70
checkpoint_calc_and_format_time: cp=10.0 dd= 5.0 dt=1172 v=15.36
checkpoint_calc_and_format_time: cp=15.0 dd= 5.0 dt=1186 v=15.17
checkpoint_calc_and_format_time: cp=21.1 dd= 6.1 dt=1458 v=15.06

RACE_GOAL_TIME_S=87:
checkpoint_calc_and_format_time: cp= 5.0 dd= 5.0 dt=1266 v=14.22
checkpoint_calc_and_format_time: cp=10.0 dd= 5.0 dt=1214 v=14.83
checkpoint_calc_and_format_time: cp=15.0 dd= 5.0 dt=1229 v=14.64
checkpoint_calc_and_format_time: cp=21.1 dd= 6.1 dt=1511 v=14.53

RACE_GOAL_TIME_S=90:
checkpoint_calc_and_format_time: cp= 5.0 dd= 5.0 dt=1307 v=13.77
checkpoint_calc_and_format_time: cp=10.0 dd= 5.0 dt=1256 v=14.33
checkpoint_calc_and_format_time: cp=15.0 dd= 5.0 dt=1273 v=14.14
checkpoint_calc_and_format_time: cp=21.1 dd= 6.1 dt=1565 v=14.03
"""

CONF = {
    "RACE_DIST_KM": 21.1,
    "RACE_GOAL_TIME_S": 87*60,
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                        "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Turn / Drink",     "kwargs": {"dist":  5.1}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Turn",             "kwargs": {"dist":  9.7}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",            "kwargs": {"dist": 10.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Crossing",         "kwargs": {"dist": 14.8}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink + Eat",      "kwargs": {"dist": 15.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Crossing",         "kwargs": {"dist": 15.2}, "plt_kwargs": {"color": "gray"}},
    ),
    "TEXT_BOTTOM_LEFT": (
        {"fmt": "{time:5s}  {dist:4.1f}  Turn (Seine)",     "kwargs": {"dist": 17.2}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Tennis",           "kwargs": {"dist": 19.2}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Turn (RA)",        "kwargs": {"dist": 20.1}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Finish",           "kwargs": {"dist": 21.1}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                        "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "-",                                        "kwargs": {},             "plt_kwargs": {"color": "gray"}},
    ),
}

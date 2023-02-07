#!/usr/bin/env python3
"""
# Stdout

checkpoint_calc_and_format_time: cp= 5.8 dd= 5.8 dt=1585 v=13.06
checkpoint_calc_and_format_time: cp=10.2 dd= 4.4 dt=1172 v=13.51
checkpoint_calc_and_format_time: cp=15.0 dd= 4.8 dt=1302 v=13.41
checkpoint_calc_and_format_time: cp=19.8 dd= 4.8 dt=1294 v=13.22
checkpoint_calc_and_format_time: cp=25.1 dd= 5.4 dt=1472 v=13.08
checkpoint_calc_and_format_time: cp=30.3 dd= 5.2 dt=1447 v=12.93
checkpoint_calc_and_format_time: cp=34.0 dd= 3.7 dt=1031 v=12.92
"""

CONF = {
    "RACE_DIST_KM": 34.0,
    "RACE_GOAL_TIME_S": 155*60,  # 13.2 km/h ; 157 = 13.0 km/h ; 151 = 13.5 km/h
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "{time:5s}  {dist:4.1f} usual",         "kwargs": {"dist":  5.75}, "plt_kwargs": {"color": "gray"}},  #  26.5
        {"fmt": "{time:5s}  {dist:4.1f} bridge",        "kwargs": {"dist": 10.15}, "plt_kwargs": {"color": "gray"}},  #  46.0
        {"fmt": "{time:5s}  {dist:4.1f} corner Kirche", "kwargs": {"dist": 15.00}, "plt_kwargs": {"color": "blue"}},  #  67.75
        {"fmt": "{time:5s}  {dist:4.1f} corner Ampel",  "kwargs": {"dist": 19.75}, "plt_kwargs": {"color": "blue"}},  #  89.0
        {"fmt": "{time:5s}  {dist:4.1f} A-HSH",         "kwargs": {"dist": 25.10}, "plt_kwargs": {"color": "blue"}},  # 113.75
        {"fmt": "{time:5s}  {dist:4.1f} tram",          "kwargs": {"dist": 30.30}, "plt_kwargs": {"color": "blue"}},  # 137.75
        {"fmt": "{time:5s}  {dist:4.1f} end",           "kwargs": {"dist": 34.00}, "plt_kwargs": {"color": "gray"}},  # 155.0
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

#!/usr/bin/env python3

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

#!/usr/bin/env python3

CONF = {
    "RACE_DIST_KM": 21.1,
    "RACE_GOAL_TIME_S": 89*60,
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                        "kwargs": {},             "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",            "kwargs": {"dist":  4.5}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Tunnel exit",      "kwargs": {"dist":  5.0}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Town/Tram/Cros",   "kwargs": {"dist":  9.5}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",            "kwargs": {"dist": 11.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Post bridge, R",   "kwargs": {"dist": 14.0}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",            "kwargs": {"dist": 15.5}, "plt_kwargs": {"color": "blue"}},
    ),
    "TEXT_BOTTOM_LEFT": (
        {"fmt": "{time:5s}  {dist:4.1f}  Dune",             "kwargs": {"dist": 17.4}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink",            "kwargs": {"dist": 18.5}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  1-2e cross",       "kwargs": {"dist": 18.7}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  2-3e cross B",     "kwargs": {"dist": 19.9}, "plt_kwargs": {"color": "green"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Finish",           "kwargs": {"dist": 21.1}, "plt_kwargs": {"color": "red"}},
        {"fmt": "-",                                        "kwargs": {},             "plt_kwargs": {"color": "gray"}},
    ),
}

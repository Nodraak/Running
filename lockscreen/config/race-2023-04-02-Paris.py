#!/usr/bin/env python3
"""
# Stdout

RACE_GOAL_TIME_S=3h40 (pacer 3h45, adjusted for final hills and easy for me):

checkpoint_format_time: cp= 4.5 dd= 4.5 dt=1461 v=11.09
checkpoint_format_time: cp=10.0 dd= 5.5 dt=1713 v=11.56
checkpoint_format_time: cp=15.0 dd= 5.0 dt=1557 v=11.56
checkpoint_format_time: cp=20.0 dd= 5.0 dt=1557 v=11.56
checkpoint_format_time: cp=25.0 dd= 5.0 dt=1557 v=11.56
checkpoint_format_time: cp=30.3 dd= 5.3 dt=1650 v=11.56
checkpoint_format_time: cp=35.0 dd= 4.7 dt=1463 v=11.56
checkpoint_format_time: cp=38.0 dd= 3.0 dt= 934 v=11.56
checkpoint_format_time: cp=40.5 dd= 2.5 dt= 772 v=11.56
checkpoint_format_time: cp=40.6 dd= 0.1 dt=  37 v=11.56
checkpoint_format_time: cp=41.3 dd= 0.7 dt= 218 v=11.56
checkpoint_format_time: cp=42.2 dd= 0.9 dt= 280 v=11.56

"""

CONF = {
    "RACE_DIST_KM": 42.2,
    "RACE_GOAL_TIME_S": (3*60 + 40)*60,
    "SPLIT_42_DV": 0.0,
    "TEXT_TOP_LEFT": (
        {"fmt": "{race_goal_time:3.0f}  {race_goal_speed:.2f} km/h  {km_time:5s} /km", "kwargs": {}, "plt_kwargs": {"color": "red"}},
        {"fmt": "{time:5s}  {dist:4.1f}  -",                "kwargs": {"dist": 0}, "plt_kwargs": {"color": "gray"}},

        {"fmt": "{time:5s}  {dist:4.1f}  Drink L (Chat)",   "kwargs": {"dist":  4.5}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink (PDorée)",   "kwargs": {"dist": 10.0}, "plt_kwargs": {"color": "gray"}},

        {"fmt": "{time:5s}  {dist:4.1f}  Drink   (Vinc)",   "kwargs": {"dist": 15.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink   (Vinc)",   "kwargs": {"dist": 20.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink L  (Bas)",   "kwargs": {"dist": 25.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink   (Alma)",   "kwargs": {"dist": 30.3}, "plt_kwargs": {"color": "blue"}},
    ),
    "TEXT_BOTTOM_LEFT": (
        {"fmt": "{time:5s}  {dist:4.1f}  Drink (P Aute)",   "kwargs": {"dist": 35.0}, "plt_kwargs": {"color": "blue"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Drink L (Casc)",   "kwargs": {"dist": 38.0}, "plt_kwargs": {"color": "blue"}},

        {"fmt": "{time:5s}  {dist:4.1f}  Trocadero (in)",   "kwargs": {"dist": 42.2-1.720}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  Trocadero (ou)",   "kwargs": {"dist": 42.2-1.600}, "plt_kwargs": {"color": "gray"}},
        {"fmt": "{time:5s}  {dist:4.1f}  V Hugo",           "kwargs": {"dist": 42.2-0.900}, "plt_kwargs": {"color": "gray"}},

        {"fmt": "{time:5s}  {dist:4.1f}  Finish",           "kwargs": {"dist": 42.2}, "plt_kwargs": {"color": "red"}},
    ),
}

#!/usr/bin/env python3
"""
Functions to process the data into a data structure that is easy to manipulate
and plot.
"""
# pylint: disable=invalid-name

from calendar import monthrange
import datetime
import statistics

from dateutil import rrule
from sklearn.linear_model import LinearRegression

from utils import date2timestamp, pd, date_y_eq, date_ym_eq, date_yw_eq, estimate_distance, RunGoal, RunRelax


def process_all(all_runs, start, end):
    """
    Return an object looking like the following:
    {
        "runs": [Run, Run, ...],
        "weekly": {
            "dates": [date, date, ...],
            "stats": [
                {
                    "duration_days": int,
                    "dist": {
                        "all": [float, float, ...],
                        "sum": float,
                        "mean": float,
                        "std": float,
                        "min": float,
                        "max": float,
                    },
                    "time_h": {
                        # same as "dist"
                    },
                    "speed": {
                        # same as "dist"
                    },
                    "predicted": {
                        "hm_time": # same as "dist"
                        "hm_speed": # same as "dist"
                        "m_time": # same as "dist"
                        "m_speed": # same as "dist"
                        "dist_at_14_1_kmph"
                    },
                },
                ...
            ],
        ],
        "monthly": {
            # same as "weekly"
        }
        "yearly": {
            # same as "weekly"
        },
        "regression": {
            # ...
        },
    }
    """

    ret = {}

    dates_weekly, dates_monthly = process_dates(start, end)
    dates_yearly = [pd("2020-01-01"), pd("2021-01-01"), pd("2022-01-01"), pd("2023-01-01")]

    # all
    ret["runs"] = all_runs

    # weekly
    ret["weekly"] = {
        "dates": dates_weekly,
        "stats": [],
    }
    for week in dates_weekly:
        runs = [r for r in all_runs if date_yw_eq(r.date, week) and not isinstance(r, RunGoal)]
        d = process_stats_complex(runs)
        d["duration_days"] = 7
        ret["weekly"]["stats"].append(d)

    # monthly
    ret["monthly"] = {
        "dates": dates_monthly,
        "stats": [],
    }
    for month in dates_monthly:
        runs = [r for r in all_runs if date_ym_eq(r.date, month) and not isinstance(r, RunGoal)]
        d = process_stats_complex(runs)
        d["duration_days"] = monthrange(month.year, month.month)[1]
        ret["monthly"]["stats"].append(d)

    # yearly
    ret["yearly"] = {
        "dates": dates_yearly,
        "stats": [],
    }
    for year in dates_yearly:
        runs = [r for r in all_runs if date_y_eq(r.date, year) and not isinstance(r, RunGoal)]
        d = process_stats_complex(runs)
        d["duration_days"] = 365
        ret["yearly"]["stats"].append(d)

    # regressions
    ret["regressions"] = process_speed_regression(all_runs)

    return ret


def process_dates(start, end):
    """
    Generate monthly and weekly dates lists.
    """
    assert start.weekday() == 0, "Date is not Monday: %s" % start
    start_weekly = start.replace(day=start.day-start.weekday())
    start_monthly = start.replace(day=1)

    dates_weekly = [d.date() for d in rrule.rrule(rrule.WEEKLY, dtstart=start_weekly, until=end)]
    dates_monthly = [d.date() for d in rrule.rrule(rrule.MONTHLY, dtstart=start_monthly, until=end)]

    return dates_weekly, dates_monthly


def process_stats_complex(runs):
    r = {
        "dist": process_stats_basic([r.distance for r in runs]),
        "time_h": process_stats_basic([r.time_h for r in runs]),
        "speed": process_stats_basic([r.speed for r in runs]),  # TODO weights by dist
        "predicted": {
            "hm_time": process_stats_basic(sorted([r.hm_time for r in runs])[-4:]),
            "hm_speed": process_stats_basic(sorted([21.1 / r.hm_time for r in runs])[-4:]),
            "m_time": process_stats_basic(sorted([r.m_time for r in runs])[-4:]),
            "m_speed": process_stats_basic(sorted([42.2 / r.m_time for r in runs])[-4:]),
        },
    }
    r["predicted"]["dist_at_14_1_kmph"] = estimate_distance(r["dist"]["f_median"], r["time_h"]["f_median"], 14.1)

    return r


def process_stats_basic(values_all):
    """
    Return an object looking like the following:
    {
        "all": [float, float, ...],
        "sum": float,
        "mean": float,
        "min": float,
        "q1": float,
        "q2": float,
        "q3": float,
        "max": float,
    }
    """

    if len(values_all) == 0:
        return {
            # for yearly/monthly/weekly stats
            "a_all": [],
            "a_sum": 0,
            "a_mean": 0,
            # for progression stats
            "f_median": 0,
            "f_mean": None,
            "f_std": None,
            "f_min": None,
            "f_max": None,
        }


    # remove outliners (lowest X% values)
    to_remove = len(values_all) * 0.34
    values_filtered = sorted(values_all)[int(to_remove):]

    return {
        # for yearly/monthly/weekly stats
        "a_all": values_all,
        "a_sum": sum(values_all),
        "a_mean": sum(values_all)/len(values_all),
        # for progression stats
        "f_median": statistics.median(values_filtered),
        "f_mean": sum(values_filtered)/len(values_filtered),
        "f_std": statistics.stdev(values_filtered) if (len(values_filtered) >= 2) else 0,
        "f_min": min(values_filtered),
        "f_max": max(values_filtered),
    }


def process_speed_regression(RUNS):
    """
        Aggregate and return:
        * runs, linear regression coefficients y(t) = t1*t+t0
        * by distance

    Return an object looking like the following:
    {
        "dist0": {
            "dt0": {
                "runs": [Run, Run, ...],
                "k0": float,
                "k1": float,
            },
            ...
        },
        ...
    }
    """
    DISTS_RANGES = {
        "9-": (5, 10),
        "12": (10, 14),
        "15": (14, 16),
        "18": (17, 19),
        "21+": (19, 42),
    }

    def is_in_range(dist_range, dist):
        return dist_range[0] < dist < dist_range[1]

    ret_regressions = {}
    for dist_ref, dist_range in DISTS_RANGES.items():
        ret_regressions[dist_ref] = {
            "all": [
                r for r in RUNS
                if is_in_range(dist_range, r.distance) and (r.temp is not None) and (not isinstance(r, RunRelax))
            ]
        }
        for dt in [12, 9, 6, 3, 2, 1]:
            runs = [
                r for r in ret_regressions[dist_ref]["all"]
                if (datetime.date.today() - r.date < datetime.timedelta(30*dt))
            ]

            if len(runs) == 0:
                k0 = 0
                k1 = 0
            else:
                model = LinearRegression().fit(
                    [[date2timestamp(r.date)] for r in runs],
                    [[r.speed] for r in runs],
                )

                k0 = model.intercept_[0]
                k1 = model.coef_[0][0]

            ret_regressions[dist_ref][dt] = {
                "runs": runs,
                "k0": k0,
                "k1": k1,
            }

    return ret_regressions

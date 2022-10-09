#!/usr/bin/env python3

from calendar import monthrange
import datetime
import statistics

from sklearn.linear_model import LinearRegression

from data import date2datetime, pd, RunGoal


def process_mileage(all_runs, dates_monthly, dates_weekly):
    """
        Aggregate and return:
        * distance and speed (velocity)
        * for all runs and averages
        * by months and by weeks
    """

    def date_ym_eq(a, b):
        return (a.year == b.year) and (a.month == b.month)

    def isocal_yw_eq(a, b):
        a_y, a_weekn, _ = a.isocalendar()
        b_y, b_weekn, _ = b.isocalendar()
        return (a_y == b_y) and (a_weekn == b_weekn)

    ret_monthly = {}
    for month in dates_monthly:
        runs = [r for r in all_runs if date_ym_eq(r.date, month) and not isinstance(r, RunGoal)]

        if len(runs) == 0:
            ret_monthly[month] = {
                "length": 0,
                "dists": [],
                "times": [],
                "speeds": [],
                "avg_dist": 0,
                "avg_speed": 0,
                "std_speed": 0,
            }
            continue

        ds = [r.distance for r in runs]
        ts = [r.time_h for r in runs]
        ss = [d/t for d, t in zip(ds, ts)]

        stdev = statistics.stdev(ss) if (len(runs) >= 2) else 0

        ret_monthly[month] = {
            "length": monthrange(month.year, month.month)[1],
            "dists": ds,
            "times": ts,
            "speeds": ss,
            "avg_dist": sum(ds)/len(ds),
            "avg_speed": sum(ds)/sum(ts),
            "std_speed": stdev,
        }

    ret_weekly = {}
    for week in dates_weekly:
        runs = [r for r in all_runs if isocal_yw_eq(r.date, week) and not isinstance(r, RunGoal)]

        if len(runs) == 0:
            ret_weekly[week] = {
                "length": 0,
                "dists": [],
                "times": [],
                "speeds": [],
                "avg_dist": 0,
                "avg_speed": 0,
                "std_speed": 0,
            }
            continue

        ds = [r.distance for r in runs]
        ts = [r.time_h for r in runs]
        ss = [d/t for d, t in zip(ds, ts)]

        stdev = statistics.stdev(ss) if (len(runs) >= 2) else 0

        ret_weekly[week] = {
            "length": 7,
            "dists": ds,
            "times": ts,
            "speeds": ss,
            "avg_dist": sum(ds)/len(ds),
            "avg_speed": sum(ds)/sum(ts),
            "std_speed": stdev,
        }

    return ret_monthly, ret_weekly


def process_speed(RUNS, t0, t1):
    """
        Aggregate and return:
        * runs, linear regression coefficients y(t) = t1*t+t0
        * by distance
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
                if (is_in_range(dist_range, r.distance) and r.temp is not None)
            ]
        }
        for dt in [3, 2, 1]:
            DATE_START = datetime.date.today() - datetime.timedelta(30*dt)

            runs = [
                r for r in ret_regressions[dist_ref]["all"]
                if (DATE_START < r.date)
            ]

            if len(runs) == 0:
                k0 = 0
                k1 = 0
            else:
                model = LinearRegression().fit(
                    [[date2datetime(r.date).timestamp()] for r in runs],
                    [[r.speed] for r in runs],
                )

                k0 = model.intercept_[0]
                k1 = model.coef_[0][0]

            ret_regressions[dist_ref][dt] = {
                "runs": runs,
                "t0": t0,
                "t1": t1,
                "k0": k0,
                "k1": k1,
                "y0": k1*t0.timestamp() + k0,
                "y1": k1*t1.timestamp() + k0,
            }

    return ret_regressions


def process_predict_times(runs):
    """
    Based on Peter Riegel's 1981's formula: T2 = T1 * (D2/D1)**1.06
    """

    def estimate_time(d1, t1, d2):
        b = 1.06
        t2 = t1 * (d2 / d1)**b
        return t2

    DATE_START = pd('2022-03-15')

    runs = [r for r in runs if DATE_START < r.date]

    return [
        {
            "run": r,
            "p42": estimate_time(r.distance, r.time_h, 42.2),
            "p21": estimate_time(r.distance, r.time_h, 21.1),
        }
        for r in runs
    ]

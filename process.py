#!/usr/bin/env python3

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from data import date2datetime, pd


def process_mileage(runs, dates_monthly, dates_weekly):
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
        ds = [r.distance for r in runs if date_ym_eq(r.date, month)]
        ts = [r.time_h for r in runs if date_ym_eq(r.date, month)]

        avg_d = sum(ds)/len(ds) if len(ds) else 0
        avg_v = sum(ds)/sum(ts) if len(ts) else 0

        ret_monthly[month] = {
            "dists": ds,
            "times": ts,
            "avg_dist": avg_d,
            "avg_speed": avg_v,
        }

    ret_weekly = {}
    for week in dates_weekly:
        ds = [r.distance for r in runs if isocal_yw_eq(r.date, week)]
        ts = [r.time_h for r in runs if isocal_yw_eq(r.date, week)]

        avg_d = sum(ds)/len(ds) if len(ds) else 0
        avg_v = sum(ds)/sum(ts) if len(ts) else 0

        ret_weekly[week] = {
            "dists": ds,
            "times": ts,
            "avg_dist": avg_d,
            "avg_speed": avg_v,
        }

    return ret_monthly, ret_weekly


def process_speed(RUNS, t0, t1):
    """
        Aggregate and return:
        * runs, linear regression coefficients y(t) = t1*t+t0
        * by distance
    """
    DISTS = [6, 9, 12, 15, 18, 21, 24]
    DATE_START = pd('2022-03-15')

    def is_plus_minus_10_percent(ref, dist):
        # TODO fix?
        return abs(ref/dist - 1) < 0.10

    ret_regressions = {}
    for ref_dist in DISTS:
        runs = [
            r for r in RUNS
            if (
                DATE_START < r.date
                and is_plus_minus_10_percent(ref_dist, r.distance)
                and r.temp is not None
            )
        ]

        model = LinearRegression().fit(
            [[date2datetime(r.date).timestamp()] for r in runs],
            [[r.speed] for r in runs],
        )

        k0 = model.intercept_[0]
        k1 = model.coef_[0][0]

        ret_regressions[ref_dist] = {
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
    def estimate_time(d1, t1, d2):
        b = 1.06
        t2 = t1 * (d2 / d1)**b
        return t2

    DATE_START = pd('2022-03-15')

    runs = [r for r in runs if DATE_START < r.date]

    return {
        'xs': [r.date for r in runs],
        'ys_42': [estimate_time(r.distance, r.time_h, 42.2) for r in runs],
        'ys_21': [estimate_time(r.distance, r.time_h, 21.1) for r in runs],
    }

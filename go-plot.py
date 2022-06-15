#!/usr/bin/env python3

from datetime import datetime, timedelta
from dateutil import rrule
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

from data import RUNS_2022 as RUNS, RunLong


def parse_date(s):
    return datetime.strptime(s, '%Y-%m-%d').date()

# for weekly milage stats
#START = parse_date('2021-03-22')  # Monday
#MID = parse_date("2021-08-15")
#END = parse_date("2021-10-15")
START = parse_date('2022-01-03')  # Monday
MID = parse_date("2022-08-15")
END = parse_date("2022-10-15")


def plot_grid(dates_weekly):
    plt.axhline(0, color="#E0E0E0", label='_nolegend_')

    for d in dates_weekly:
        plt.axvline(d, color="#E0E0E0", label='_nolegend_')


def plot_milage(subplot_args, dates_monthly, dates_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Distance (km)")

    plt.axhline(40, color="#E0E0E0")
    plt.axhline(50, color="#E0E0E0")

    plt.axhline(160, color="#E0E0E0")
    plt.axhline(200, color="#E0E0E0")

    xs = dates_monthly
    ys = [
        sum([r.distance for r in RUNS if r.date.month==d.month])
        for d in dates_monthly
    ]
    plt.plot(xs, ys, 'x-')

    xs = dates_weekly
    ys = [
        sum([r.distance for r in RUNS if r.date.isocalendar()[1]==d.isocalendar()[1]])
        for d in dates_weekly
    ]
    plt.plot(xs, ys, 'x-')

    plt.legend(["Monthly", "Weekly"])


def plot_distance(subplot_args, dates_monthly, dates_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Distance (km)")

    plt.axhline(6, color="#E0E0E0")
    plt.axhline(12, color="#E0E0E0")
    plt.axhline(18, color="#E0E0E0")
    plt.axhline(21, color="#E0E0E0")

    # plt.plot([START, MID], [5, 30], color="#E0E0E0")
    # plt.plot([MID, END], [30, 25], color="#E0E0E0")
    # plt.plot([START, MID], [3, 15], color="#E0E0E0")
    # plt.plot([MID, END], [15, 12], color="#E0E0E0")

    dates = [tup.date for tup in RUNS]
    distances = [tup.distance for tup in RUNS]
    speeds = [tup.speed for tup in RUNS]
    is_long_runs = [isinstance(tup, RunLong) for tup in RUNS]

    for dt, dist, is_long_run in zip(dates, distances, is_long_runs):
        color = {
            False: "blue",
            True: "green",
        }[is_long_run]
        plt.plot(dt, dist, 'x', color=color)


def plot_speed(subplot_args, dates_monthly, dates_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Speed (km/h)")
    plt.ylim((10, 15))

    plt.axhline(12, color="#E0E0E0")
    plt.axhline(13, color="#E0E0E0")
    plt.axhline(14, color="#E0E0E0")

    dates = [tup.date for tup in RUNS]
    distances = [tup.distance for tup in RUNS]
    speeds = [tup.speed for tup in RUNS]
    is_long_runs = [isinstance(tup, RunLong) for tup in RUNS]

    for d, s, is_long_run in zip(dates, speeds, is_long_runs):
        color = {
            False: "blue",
            True: "green",
        }[is_long_run]
        plt.plot(d, s, 'x', color=color)


def plot_4():
    def is_plus_minus_10_percent(ref, dist):
        return abs(ref/dist - 1) < 0.10

    ref_dists = [6, 9, 12, 15, 18, 21, 24]

    plt.axhline(12.0, color='#E0E0E0', label='_nolegend_')
    plt.axhline(12.5, color='#E0E0E0', label='_nolegend_')
    plt.axhline(13.0, color='#E0E0E0', label='_nolegend_')
    plt.axhline(13.5, color='#E0E0E0', label='_nolegend_')
    plt.axhline(14.0, color='#E0E0E0', label='_nolegend_')
    plt.axvline(parse_date('2022-03-01'), color='#E0E0E0', label='_nolegend_')
    plt.axvline(parse_date('2022-04-01'), color='#E0E0E0', label='_nolegend_')
    plt.axvline(parse_date('2022-05-01'), color='#E0E0E0', label='_nolegend_')
    plt.axvline(parse_date('2022-06-01'), color='#E0E0E0', label='_nolegend_')

    print("d (km)  progress (km/h) in 1 month")
    patches = []
    for ref_dist in ref_dists:
        runs = [r for r in RUNS if is_plus_minus_10_percent(ref_dist, r.distance)]

        xs, ys = [r.date for r in runs], [r.speed for r in runs]

        def date2datetime(d):
            return datetime.fromordinal(d.toordinal())

        model = LinearRegression().fit([[date2datetime(x).timestamp()] for x in xs], [[y] for y in ys])

        x0 = date2datetime(START) # date2datetime(parse_date('2022-03-01'))
        x1 = date2datetime(END) # date2datetime(parse_date('2022-11-01'))
        y0 = model.coef_[0][0]*x0.timestamp() + model.intercept_[0]
        y1 = model.coef_[0][0]*x1.timestamp() + model.intercept_[0]

        p, = plt.plot(xs, ys, 'x-')
        plt.plot([x0, x1], [y0, y1], '--', color=p.get_color())
        patches.append(p)

        print("%4.1f   %5.2f" % (ref_dist, model.coef_[0][0]*86400*365/12))

    plt.legend(patches, ref_dists)


def main():
    start_weekly = START.replace(day=START.day-START.weekday())
    start_monthly = START.replace(day=1)

    dates_weekly = [d.date() for d in rrule.rrule(rrule.WEEKLY, dtstart=start_weekly, until=END)]
    dates_monthly = [d.date() for d in rrule.rrule(rrule.MONTHLY, dtstart=start_monthly, until=END)]

    plt.figure()
    plt.xlim((START, MID))
    plot_milage((3, 1, 1), dates_monthly, dates_weekly)
    plot_distance((3, 1, 2), dates_monthly, dates_weekly)
    plot_speed((3, 1, 3), dates_monthly, dates_weekly)

    plt.figure()
    plt.xlim((START, END))
    plot_4()

    plt.show()


if __name__ == "__main__":
    main()

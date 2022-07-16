#!/usr/bin/env python3

from calendar import monthrange
from datetime import datetime, timedelta
from dateutil import rrule

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

from data import pd, RunLong, RUNS


def date2datetime(d):
    return datetime.fromordinal(d.toordinal())


# for weekly milage stats
#START = pd('2021-03-22')  # Monday
START = pd('2022-01-03')  # Monday
MID = pd("2022-08-15")
#END = pd("2021-10-15")
END = pd("2023-05-01")

TODAY = datetime.today()


def plot_grid(dates_weekly):
    plt.axhline(0, color="#E0E0E0", label='_nolegend_')

    for d in dates_weekly:
        plt.axvline(d, color="#E0E0E0", label='_nolegend_')

    plt.axvline(TODAY, color="#800000", label='_nolegend_')


def plot_milage(subplot_args, dates_monthly, dates_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Distance (km)")

    plt.axhline(30, color="#E0E0E0", label='_nolegend_')
    plt.axhline(40, color="#E0E0E0", label='_nolegend_')
    plt.axhline(50, color="#E0E0E0", label='_nolegend_')
    plt.axhline(60, color="#E0E0E0", label='_nolegend_')

    plt.axhline(120, color="#E0E0E0", label='_nolegend_')
    plt.axhline(160, color="#E0E0E0", label='_nolegend_')
    plt.axhline(200, color="#E0E0E0", label='_nolegend_')
    plt.axhline(240, color="#E0E0E0", label='_nolegend_')

    def date_ym_eq(a, b):
        return (a.year == b.year) and (a.month == b.month)

    def isocal_ym_eq(a, b):
        a_y, a_weekn, _ = a.isocalendar()
        b_y, b_weekn, _ = b.isocalendar()
        return (a_y == b_y) and (a_weekn == b_weekn)

    xs = dates_monthly
    dss = [
        [r.distance for r in RUNS if date_ym_eq(r.date, d)]
        for d in dates_monthly
    ]
    months_length = [monthrange(d.year, d.month)[1] for d in dates_monthly]
    plt.bar(xs, [sum(ds) for ds in dss], align='edge', width=months_length)
    print("\n== Milage (monthly) ==")
    for x, ds in zip(xs, dss):
        print("%s: %2dx - %3d km" % (x, len(ds), sum(ds)))

    xs = dates_weekly
    dss = [
        [r.distance for r in RUNS if isocal_ym_eq(r.date, d)]
        for d in dates_weekly
    ]
    plt.bar(xs, [sum(ds) for ds in dss], align='edge', width=7)
    print("\n== Milage (weekly) ==")
    for x, ds in zip(xs, dss):
        print("%s: %2dx - %3d km" % (x, len(ds), sum(ds)))

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
        plt.bar(dt, dist, align='edge', width=1, color=color)


def plot_speed_simple(subplot_args, dates_monthly, dates_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Speed (km/h)")
    plt.ylim((10.0, 15.5))

    for s in range(11, 14+1):
        plt.axhline(s, color="#E0E0E0")

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


def plot_speed_prog(subplot_args):
    def is_plus_minus_10_percent(ref, dist):
        return abs(ref/dist - 1) < 0.10

    plt.subplot(*subplot_args, sharex=plt.gca())
    plt.ylabel("Speed (km/h)")
    plt.ylim((11.5, 15.5))

    REF_DISTS = [6, 9, 12, 15, 18, 21, 24]

    legend = []

    for v in range(120, 150+1, 5):
        plt.axhline(v/10, color='#E0E0E0', label='_nolegend_')

    for m in range(3, 12+1):
        plt.axvline(pd('2022-%02d-01' % m), color='#E0E0E0', label='_nolegend_')
    for m in range(1, 4+1):
        plt.axvline(pd('2023-%02d-01' % m), color='#E0E0E0', label='_nolegend_')

    # hline = plt.axhline(20.0/1.5, ls="--", color='#808080')
    # legend.append((hline, "20 km / 1h30 = %.2f" % (20.0/1.5)))
    # hline = plt.axhline(42.2/3.0, ls="--", color='#808080')
    # legend.append((hline, "42.2 km / 3h00 = %.2f" % (42.2/3.0)))
    # hline = plt.axhline(42.2/3.25, ls="--", color='#808080')
    # legend.append((hline, "42.2 km / 3h15 = %.2f" % (42.2/3.25)))
    # hline = plt.axhline(42.2/3.5, ls="--", color='#808080')
    # legend.append((hline, "42.2 km / 3h30 = %.2f" % (42.2/3.5)))

    """
        04     : 12.0
        07 (+3): 13.5 -> 0.50/m
        11 (+4): 14.5 -> 0.33/m
        03 (+4): 15.0 -> 0.25/m
    """
    plt.plot(
        [pd('2022-04-24'), pd('2022-07-24'), pd('2022-11-27'), pd('2023-04-02')],
        [12.00, 13.50, 14.50, 15.00],
        '--', color='#808080',
    )

    plt.plot(pd('2022-07-24'), 20*60/90, 'o', color='#808080', label='_nolegend_')
    plt.plot(pd('2022-11-27'), 21.1*60/90, 'o', color='#808080', label='_nolegend_')
    plt.plot(pd('2023-04-02'), 21.1*60/90+1.0, 'o', color='#808080', label='_nolegend_')

    print("\n== Progress ==\nd (km)  progress (km/h) in 1 month")
    for ref_dist in REF_DISTS:
        runs = [
            r for r in RUNS
            if r.date > pd('2022-03-15') and is_plus_minus_10_percent(ref_dist, r.distance)
        ]

        xs, ys = [r.date for r in runs], [r.speed for r in runs]

        model = LinearRegression().fit([[date2datetime(x).timestamp()] for x in xs], [[y] for y in ys])

        x0 = date2datetime(START) # date2datetime(pd('2022-03-01'))
        x1 = date2datetime(END) # date2datetime(pd('2022-11-01'))
        y0 = model.coef_[0][0]*x0.timestamp() + model.intercept_[0]
        y1 = model.coef_[0][0]*x1.timestamp() + model.intercept_[0]

        p, = plt.plot(xs, ys, 'o-')
        plt.plot([x0, x1], [y0, y1], '--', color=p.get_color())
        legend.append((p, ref_dist))

        print("* Reg %d km: vel(t) = %3d*10**-9 * t + %.3f km/h => %5.2f km/h / month" % (ref_dist, model.coef_[0][0]*10**9, model.intercept_[0], model.coef_[0][0]*86400*365/12))

    plt.legend([tup[0] for tup in legend], [tup[1] for tup in legend])


def plot_temp():

    plt.axhline(5, color='#E0E0E0')
    plt.axhline(15, color='#E0E0E0')

    for m in range(3, 12+1):
        plt.axvline(pd('2022-%02d-01' % m), color='#E0E0E0', label='_nolegend_')
    for m in range(1, 4+1):
        plt.axvline(pd('2023-%02d-01' % m), color='#E0E0E0', label='_nolegend_')

    xs, ys = [r.date for r in RUNS], [r.temp for r in RUNS]
    plt.plot(xs, ys, 'o-')


def main():
    start_weekly = START.replace(day=START.day-START.weekday())
    start_monthly = START.replace(day=1)

    dates_weekly = [d.date() for d in rrule.rrule(rrule.WEEKLY, dtstart=start_weekly, until=END)]
    dates_monthly = [d.date() for d in rrule.rrule(rrule.MONTHLY, dtstart=start_monthly, until=END)]

    plt.figure()
    plt.xlim((START, MID))
    plot_milage((2, 1, 1), dates_monthly, dates_weekly)
    plot_distance((2, 1, 2), dates_monthly, dates_weekly)

    plt.figure()
    plt.xlim((START, END))
    #plt.xlim((date2datetime(pd('2022-02-01')), date2datetime(pd('2023-05-01'))))
    plot_speed_simple((2, 1, 1), dates_monthly, dates_weekly)
    plot_speed_prog((2, 1, 2))

    plt.figure()
    plt.xlim((START, END))
    plot_temp()

    plt.show()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib.dates import date2num
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter

from data import date2datetime, pd, RunShort, RunLong, RunRace, RunGoal


TODAY = datetime.today()


RUN2COLORS = {
    RunShort: "blue",
    RunLong: "green",
    RunRace: "brown",
    RunGoal: "gray",
}
RUN2LABEL = {
    RunShort: "Short run",
    RunLong: "Long run",
    RunRace: "Race",
    RunGoal: "Goal",
}

C_LINE = "#E0E0E0"
C_TODAY = "#FF0000"


def plot_grid(dates_weekly):
    plt.axhline(0, color=C_LINE, label='_nolegend_')

    for d in dates_weekly:
        plt.axvline(d, color=C_LINE, label='_nolegend_')

    plt.axvline(TODAY, color=C_TODAY, label='_nolegend_')


def plot_legend():
    """
    Show the legend:
    * Labels deduplicated (with a dict)
    * Sorted (by labels)
    * In the top left corner
    """
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(sorted(zip(labels, handles), key=lambda tup: tup[0]))
    plt.legend(by_label.values(), by_label.keys(), loc="upper left")


def plot_distance(subplot_args, dates_weekly, runs):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Distance (km)")

    for y in [6, 12, 18, 24, 30, 36]:
        plt.axhline(y, color=C_LINE)

    # plt.plot([START, MID], [5, 30], color=C_LINE)
    # plt.plot([MID, END], [30, 25], color=C_LINE)
    # plt.plot([START, MID], [3, 15], color=C_LINE)
    # plt.plot([MID, END], [15, 12], color=C_LINE)

    for run in runs:
        color = RUN2COLORS[run.__class__]
        label = RUN2LABEL[run.__class__]
        plt.bar(run.date, run.distance, align='edge', width=1, color=color, label=label)

    plot_legend()


def plot_milage(subplot_args, dates_monthly, dates_weekly, runs, mileage_monthly, mileage_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Distance (km)")

    plt.axhline(30, color=C_LINE, label='_nolegend_')
    plt.axhline(40, color=C_LINE, label='_nolegend_')
    plt.axhline(50, color=C_LINE, label='_nolegend_')
    plt.axhline(60, color=C_LINE, label='_nolegend_')

    plt.axhline(120, color=C_LINE, label='_nolegend_')
    plt.axhline(160, color=C_LINE, label='_nolegend_')
    plt.axhline(200, color=C_LINE, label='_nolegend_')
    plt.axhline(240, color=C_LINE, label='_nolegend_')

    print("\n== Milage (yearly) ==")

    for y in [2021, 2022]:
        runs_2022 = [r for r in runs if pd('%d-01-01' % y) <= r.date <= pd('%d-12-31' % y)]
        runs_2022_dist = sum([r.distance for r in runs_2022])
        runs_2022_n = len(runs_2022)
        runs_2022_t = sum([r.time_h for r in runs_2022])
        print("Total %d: %d km - %d runs - %d h" % (y, runs_2022_dist, runs_2022_n, runs_2022_t))

    SCORE_MAX_WEEK = 1000  # Objective peak training: (12+12+15+30)*14.5 = 1000

    # TODO move to process
    def estimate_time(d1, t1, d2):
        b = 1.06
        t2 = t1 * (d2 / d1)**b
        return t2

    print("\n== Milage (monthly) ==")
    for m in dates_monthly:
        data = mileage_monthly[m]
        score = 100 * sum(data["dists"])*data["avg_speed"] / (SCORE_MAX_WEEK*52/12)
        t = sum(data["dists"]) / data["avg_speed"] if data["avg_speed"] else 0
        v21 = 21.1 / estimate_time(data["avg_dist"], data["avg_dist"]/data["avg_speed"], 21.1) if data["avg_speed"] else 0
        v42 = 42.2 / estimate_time(data["avg_dist"], data["avg_dist"]/data["avg_speed"], 42.2) if data["avg_speed"] else 0
        print(
            "%s: %2d runs - %3d km - %4.1f h - AVG/run: %4.1f km * %5.2f km/h - score: %3d%% - v21/42: %5.2f/%5.2f km/h" % (
                m, len(data["dists"]), sum(data["dists"]), t, data["avg_dist"], data["avg_speed"], score, v21, v42,
            )
        )

    ys = [sum(mileage_monthly[month]["dists"]) for month in dates_monthly]
    months_length = [mileage_monthly[month]["length"] for month in dates_monthly]
    plt.bar(dates_monthly, ys, align='edge', width=months_length, label="Montly")

    print("\n== Milage (weekly) ==")
    for w in dates_weekly:
        data = mileage_weekly[w]
        score = 100 * sum(data["dists"])*data["avg_speed"] / SCORE_MAX_WEEK
        t = sum(data["dists"]) / data["avg_speed"] if data["avg_speed"] else 0
        v21 = 21.1 / estimate_time(data["avg_dist"], data["avg_dist"]/data["avg_speed"], 21.1) if data["avg_speed"] else 0
        v42 = 42.2 / estimate_time(data["avg_dist"], data["avg_dist"]/data["avg_speed"], 42.2) if data["avg_speed"] else 0
        print(
            "%s: %2d runs - %3d km - %4.1f h - AVG/run: %4.1f km * %5.2f km/h - score: %3d%% - v21/42: %5.2f/%5.2f km/h" % (
                w, len(data["dists"]), sum(data["dists"]), t, data["avg_dist"], data["avg_speed"], score, v21, v42,
            )
        )

    ys = [sum(mileage_weekly[week]["dists"]) for week in dates_weekly]
    plt.bar(dates_weekly, ys, align='edge', width=7, label="Weekly")

    plot_legend()


def plot_avg(subplot_args, dates_monthly, dates_weekly, mileage_monthly, mileage_weekly):
    plot_grid(dates_weekly)
    plt.ylabel("Speed (km/h)")
    plt.ylim((10.0, 15.5))

    for m, dic in mileage_monthly.items():
        if len(dic["speeds"]) == 0:
            return

        # Note: "matplotlib uses its own representation of dates/times (floating number of days)"
        x0 = date2num(m)+dic["length"]*0/4
        x25 = date2num(m)+dic["length"]*1/4
        x50 = date2num(m)+dic["length"]*2/4
        x75 = date2num(m)+dic["length"]*3/4
        x1 = date2num(m)+dic["length"]*4/4
        mean = dic["avg_speed"]
        std = dic["std_speed"]
        mi = min(dic["speeds"])
        ma = max(dic["speeds"])

        # min-max vert line
        plt.plot([x50, x50], [mi, ma], color="blue")

        # min and max horiz lines
        plt.plot([x25, x75], [mi, mi], color="blue")
        plt.plot([x25, x75], [ma, ma], color="blue")

        # std dev rectangle
        dx = x1-x0
        y0, dy = mean-std, 2*std
        plt.gca().add_patch(Rectangle((x0, y0), dx, dy, color="blue", fill=False))

        # mean horiz line
        plt.plot([x0, x1], [mean, mean], color="blue")

    plot_legend()


def plot_speed_simple(subplot_args, dates_weekly, runs):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Speed (km/h)")
    plt.ylim((10.0, 15.5))

    for s in range(11, 15+1):
        plt.axhline(s, color=C_LINE)

    for run in runs:
        color = RUN2COLORS[run.__class__]
        label = RUN2LABEL[run.__class__]
        plt.plot(run.date, run.speed, 'x', color=color, label=label)

    plot_legend()


def plot_speed_prog(subplot_args, runs, speed_regressions):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plt.ylabel("Speed (km/h)")
    plt.ylim((11.5, 15.5))

    legend = []

    for v in range(120, 150+1, 5):
        plt.axhline(v/10, color=C_LINE, label='_nolegend_')

    for m in range(3, 12+1):
        plt.axvline(pd('2022-%02d-01' % m), color=C_LINE, label='_nolegend_')
    for m in range(1, 4+1):
        plt.axvline(pd('2023-%02d-01' % m), color=C_LINE, label='_nolegend_')

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

    for r in runs:
        if isinstance(r, RunGoal):
            plt.plot(r.date, r.speed, 'o', color='#808080', label='_nolegend_')

    print("\n== Progress ==\n")
    print("dist (km): progress in 3 -> 2 -> 1 (km/h/month)")
    for dist_ref, sr_data_all in speed_regressions.items():
        # plot all runs
        sr_data = sr_data_all["all"]
        xs, ys = [r.date for r in sr_data], [r.speed for r in sr_data]
        p, = plt.plot(xs, ys, 'o-')
        legend.append((p, "%s km" % dist_ref))

        # plot reg
        sr_data = sr_data_all[3]
        plt.plot([sr_data["t0"], sr_data["t1"]], [sr_data["y0"], sr_data["y1"]], '--', color=p.get_color())

        # print reg
        print("* %-3s km: %5.2f -> %5.2f -> %5.2f km/h/month" % (
            dist_ref,
            sr_data_all[3]["k1"]*86400*365/12,
            sr_data_all[2]["k1"]*86400*365/12,
            sr_data_all[1]["k1"]*86400*365/12,
        ))

    plt.legend([tup[0] for tup in legend], [tup[1] for tup in legend])


def plot_temp(speed_regressions):
    plt.ylabel("Temperature (°C)")

    plt.axhline(5, color=C_LINE)
    plt.axhline(15, color=C_LINE)

    for m in range(3, 12+1):
        plt.axvline(pd('2022-%02d-01' % m), color=C_LINE, label='_nolegend_')
    for m in range(1, 4+1):
        plt.axvline(pd('2023-%02d-01' % m), color=C_LINE, label='_nolegend_')

    for sr_data_all in speed_regressions.values():
        for r in sr_data_all["all"]:
            if r not in sr_data_all[1]["runs"]:
                x, y = r.date, r.temp
                plt.plot(x, y, 'o', color="gray")

        for r in sr_data_all[1]["runs"]:
            k1 = sr_data_all[1]["k1"]
            k0 = sr_data_all[1]["k0"]

            x, y = r.date, r.temp

            d = r.speed - (k1*date2datetime(r.date).timestamp() + k0)
            c = "gray"
            l = "-"
            if d < -0.30:
                c = "red"
                l = "Much slower than usual"
            if d < -0.15:
                c = "orange"
                l = "Slower than usual"
            if d > +0.15:
                c = "blue"
                l = "A little faster than usual"
            if d > +0.30:
                c = "green"
                l = "Much faster than usual"

            plt.plot(x, y, 'o', color=c, label=l)

    plot_legend()


def plot_predict_times(predicted_times):
    def formatter_factory(dist):
        def formatter(x, pos):
            h = int(x)
            mn = int(60*x-60*h)
            sec = int(3600*x-3600*h-60*mn)
            speed = dist/x
            return f'{h}:{mn:02d}:{sec:02d} - {speed:.2f}'
        return formatter

    #
    # Marathon
    #

    plt.subplot(2, 1, 1, sharex=plt.gca())
    plt.ylabel("Predicted time (h:m:s - km/h)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter_factory(42.2)))

    plt.ylim((2.50, 4.00))

    for y in range(250, 400+1, 25):
        plt.axhline(y/100, color=C_LINE)

    for p in predicted_times:
        color = RUN2COLORS[p["run"].__class__]
        label = RUN2LABEL[p["run"].__class__]
        plt.plot(p["run"].date, p['p42'], 'o', color=color, label=label)

    plot_legend()

    #
    # Half-marathon
    #

    plt.subplot(2, 1, 2, sharex=plt.gca())
    plt.ylabel("Predicted time (h:m:s - km/h)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter_factory(21.1)))

    plt.ylim((1.25, 2.00))

    for y in range(125, 200+1, 25):
        plt.axhline(y/100, color=C_LINE)

    for p in predicted_times:
        color = RUN2COLORS[p["run"].__class__]
        label = RUN2LABEL[p["run"].__class__]
        plt.plot(p["run"].date, p['p21'], 'o', color=color, label=label)

    plot_legend()


def plot_predict_distances(runs):

    # TODO move to process

    def calc_d(d1, t1):
        """
        Can not solve it mathematically, wolframalpha says:
            d2 = 10**-19 * d1**(53/3) / t1**(50/3)
            d2 = 10**-19 * d1**(1.06*50/3) / t1**(50/3)
        Big coeff are imprecise, using an iterative solution instead.
        """

        for d in range(1, 42200, 100):
            d2 = d/1000

            t2 = t1 * (d2 / d1)**1.06

            if d2/t2 < 14.1:
                return d2

        return 42.2

    pds = []
    for r in runs:
        pds.append((r.date, r.distance, calc_d(r.distance, r.time_h), RUN2COLORS[r.__class__]))

    plt.ylabel("Predicted distance (km) at 14.1 km/h")

    plt.axhline(21.1, color=C_LINE)
    plt.axhline(42.2, color=C_LINE)
    for (date, distance, dp, color) in pds:
        plt.plot(date, distance, "x", color=C_LINE)
        plt.plot(date, dp, "o", color=color)

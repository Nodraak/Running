#!/usr/bin/env python3

from calendar import monthrange
from datetime import datetime, timedelta

from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

from data import date2datetime, pd, RunShort, RunLong, RunRace


TODAY = datetime.today()


RUN2COLORS = {
    RunShort: "blue",
    RunLong: "green",
    RunRace: "brown",
}
RUN2LABEL = {
    RunShort: "Short run",
    RunLong: "Long run",
    RunRace: "Race",
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

    plt.axhline(6, color=C_LINE)
    plt.axhline(12, color=C_LINE)
    plt.axhline(18, color=C_LINE)
    plt.axhline(21, color=C_LINE)

    # plt.plot([START, MID], [5, 30], color=C_LINE)
    # plt.plot([MID, END], [30, 25], color=C_LINE)
    # plt.plot([START, MID], [3, 15], color=C_LINE)
    # plt.plot([MID, END], [15, 12], color=C_LINE)

    for run in runs:
        color = RUN2COLORS[run.__class__]
        label = RUN2LABEL[run.__class__]
        plt.bar(run.date, run.distance, align='edge', width=1, color=color, label=label)

    plot_legend()


def plot_milage(subplot_args, dates_monthly, dates_weekly, mileage_monthly, mileage_weekly):
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

    print("\n== Milage (monthly) ==")
    for m in dates_monthly:
        data = mileage_monthly[m]
        print(
            "%s: %2dx - %3d km - AVG/run: %4.1f km - %4.1f km/h" % (
                m, len(data["dists"]), sum(data["dists"]), data["avg_dist"], data["avg_speed"],
            )
        )

    ys = [sum(mileage_monthly[month]["dists"]) for month in dates_monthly]
    months_length = [monthrange(month.year, month.month)[1] for month in dates_monthly]
    plt.bar(dates_monthly, ys, align='edge', width=months_length, label="Montly")

    print("\n== Milage (weekly) ==")
    for w in dates_weekly:
        data = mileage_weekly[w]
        print(
            "%s: %2dx - %3d km - AVG/run: %4.1f km - %4.1f km/h" % (
                w, len(data["dists"]), sum(data["dists"]), data["avg_dist"], data["avg_speed"],
            )
        )

    ys = [sum(mileage_weekly[week]["dists"]) for week in dates_weekly]
    plt.bar(dates_weekly, ys, align='edge', width=7, label="Weekly")

    plot_legend()


def plot_avg(subplot_args, dates_monthly, dates_weekly, mileage_monthly, mileage_weekly):
    plt.subplot(*subplot_args, sharex=plt.gca())
    plot_grid(dates_weekly)
    plt.ylabel("Speed (km/h)")
    plt.ylim((10.0, 15.5))

    for m, dic in mileage_monthly.items():
        month_length = monthrange(m.year, m.month)[1]
        plt.plot([m, m+timedelta(days=month_length)], [dic["avg_speed"], dic["avg_speed"]], color="blue", label="Monthly")

    for w, dic in mileage_weekly.items():
        plt.plot([w, w+timedelta(days=7)], [dic["avg_speed"], dic["avg_speed"]], color="orange", label="Weekly")

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


def plot_speed_prog(subplot_args, speed_regressions):
    REF_DISTS = [6, 9, 12, 15, 18, 21, 24]

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

    plt.plot(pd('2022-07-24'), 20*60/90, 'o', color='#808080', label='_nolegend_')
    plt.plot(pd('2022-11-27'), 21.1*60/90, 'o', color='#808080', label='_nolegend_')
    plt.plot(pd('2023-04-02'), 21.1*60/90+1.0, 'o', color='#808080', label='_nolegend_')

    print("\n== Progress ==\nd (km)  progress (km/h) in 1 month")
    for ref_dist in REF_DISTS:
        sr_data = speed_regressions[ref_dist]

        xs, ys = [r.date for r in sr_data["runs"]], [r.speed for r in sr_data["runs"]]

        p, = plt.plot(xs, ys, 'o-')
        legend.append((p, "%d km" % ref_dist))

        plt.plot([sr_data["t0"], sr_data["t1"]], [sr_data["y0"], sr_data["y1"]], '--', color=p.get_color())

        print(
            "* Reg %d km: vel(t) = %3d*10**-9 * t + %.3f km/h => %5.2f km/h / month" % (
                ref_dist, sr_data["k1"]*10**9, sr_data["k0"], sr_data["k1"]*86400*365/12,
            )
        )

    plt.legend([tup[0] for tup in legend], [tup[1] for tup in legend])


def plot_temp(speed_regressions):
    plt.ylabel("Temperature (°C)")

    plt.axhline(5, color=C_LINE)
    plt.axhline(15, color=C_LINE)

    for m in range(3, 12+1):
        plt.axvline(pd('2022-%02d-01' % m), color=C_LINE, label='_nolegend_')
    for m in range(1, 4+1):
        plt.axvline(pd('2023-%02d-01' % m), color=C_LINE, label='_nolegend_')

    for sr in speed_regressions.values():
        for r in sr["runs"]:
            k1 = sr["k1"]
            k0 = sr["k0"]

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
    def formatter(x, pos):
        h = int(x)
        mn = int((x-h)*60)
        return f'{h}:{mn:02d}'

    #
    # Marathon
    #

    plt.subplot(2, 1, 1, sharex=plt.gca())
    plt.ylabel("Predicted time (h)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter))

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
    plt.ylabel("Predicted time (h)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter))

    plt.ylim((1.25, 2.00))

    for y in range(125, 200+1, 25):
        plt.axhline(y/100, color=C_LINE)

    for p in predicted_times:
        color = RUN2COLORS[p["run"].__class__]
        label = RUN2LABEL[p["run"].__class__]
        plt.plot(p["run"].date, p['p21'], 'o', color=color, label=label)

    plot_legend()

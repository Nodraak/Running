#!/usr/bin/env python3
"""
Functions to plot and print.

Data has been pre-processed and is (should be) easy to plot.
"""
# pylint: disable=invalid-name

from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib.dates import date2num
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter

from utils import date2timestamp, date_ym_eq, RunGoal, RunLong, RunRace, RunRelax, RunShort, RunCross


FIGSIZE = (1200, 900)
DPI = 100

RUN2COLORS = {
    RunGoal: "orange",
    RunLong: "green",
    RunRace: "brown",
    RunRelax: "gray",
    RunShort: "blue",
    RunCross: "gray",
}
RUN2LABEL = {
    RunGoal: "Goal",
    RunLong: "Long run",
    RunRace: "Race",
    RunRelax: "Relaxed run",
    RunShort: "Short run",
    RunCross: "Cross training",
}

C_LINE = "#E0E0E0"
C_TODAY = "#FF0000"

#
# utils
#

def plot_grid(dates):
    """
    Plot a basic grid with
    * Horizontal y=0
    * Vertical for each value of *dates*
    * Vertical x=today
    """
    plt.axhline(0, color=C_LINE, label='_nolegend_')

    for d in dates:
        plt.axvline(d, color=C_LINE, label='_nolegend_')

    plt.axvline(datetime.today(), color=C_TODAY, label='_nolegend_')


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


def plot_err_bar(date, x_size, ys):
    """
    Plot a standard error bar box.

    Parameters:
    * data: date where to plot the data
    * x_size: width of the box
    * ys: must contain min, max, mean and std
    """
    y_min, y_max, y_mean, y_std = ys["f_min"], ys["f_max"], ys["f_mean"], ys["f_std"]

    # Note: "matplotlib uses its own representation of dates/times (floating number of days)"
    x0 = date2num(date)+x_size*0/4
    x25 = date2num(date)+x_size*1/4
    x50 = date2num(date)+x_size*2/4
    x75 = date2num(date)+x_size*3/4
    x1 = date2num(date)+x_size*4/4

    # min-max vert line
    plt.plot([x50, x50], [y_min, y_max], color="blue")

    # min and max horiz lines
    plt.plot([x25, x75], [y_min, y_min], color="blue")
    plt.plot([x25, x75], [y_max, y_max], color="blue")

    # std dev rectangle
    dx = x1-x0
    y0, dy = y_mean-y_std, 2*y_std
    plt.gca().add_patch(Rectangle((x0, y0), dx, dy, color="blue", fill=False))

    # mean horiz line
    plt.plot([x0, x1], [y_mean, y_mean], color="blue")

    # median
    plt.plot(x50, ys["f_median"], "o", color="blue")

#
# plot
#

def plot_all(data, start, end):
    print_distance_and_mileage(data)
    print_speed_prog(data)

    # (Real) Distance and mileage
    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Distance and milage")
    plot_distance_and_mileage(data, start, end)
    plt.savefig("build/trainings-1-distance-and-milage.png")

    # (Real) Speed (all, prog by distance)
    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Speed (progression)")
    plot_speed_prog(data, start, end)
    plt.savefig("build/trainings-2-speed-prog.png")

    # Speed (all, monthly) (Real, Predicted)
    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Speed (monthly average)")
    plot_speed_avg(data, start, end)
    plt.savefig("build/trainings-3-speed-avg.png")

    # (Predicted HM, M) Time (all, monthly) - (Predicted HM, M) Speed (all, monthly)
    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Predicted marathon and half-marathon times")
    plot_predict_time(data, start, end)
    plt.savefig("build/trainings-4-predict-time.png")

    # (Predicted) Distance (all, monthly)
    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Predicted distance (km) at 14.1 km/h")
    plot_predict_distance(data, start, end)
    plt.savefig("build/trainings-5-predict-dist.png")

    plt.show()


def print_distance_and_mileage(data):
    def print_(d):
        for date, dic in zip(d["dates"], d["stats"]):
            if datetime.today().date() < date:
                return

            print(
                "%s: %2d runs - %4d km / %4.1f h - a_avg/run: %4.1f km, %5.2f km/h - f_predicted_med: %5.2f/%5.2f km/h" % (
                    date,
                    len(dic["dist"]["a_all"]),
                    dic["dist"]["a_sum"], dic["time_h"]["a_sum"],
                    dic["dist"]["a_mean"], dic["speed"]["a_mean"],
                    dic["predicted"]["hm_speed"]["f_median"], dic["predicted"]["m_speed"]["f_median"],
                )
            )

    print("\n== Milage (yearly) ==")
    print_(data["yearly"])

    print("\n== Milage (monthly) ==")
    print_(data["monthly"])

    print("\n== Milage (weekly) ==")
    print_(data["weekly"])


def print_speed_prog(data):
    print("\n== Progress ==\n")
    print("(f(month) = km/h/month ; by distance)")
    print("")
    print("        |    12     9     6     3     2     1")
    print("--------+-------+-----+-----+-----+-----+-----+")
    for dist_ref, sr_data_all in data["regressions"].items():
        # print reg
        print("%4s km |  %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f" % (
            dist_ref,
            sr_data_all[12]["k1"]*86400*365/12,
            sr_data_all[9]["k1"]*86400*365/12,
            sr_data_all[6]["k1"]*86400*365/12,
            sr_data_all[3]["k1"]*86400*365/12,
            sr_data_all[2]["k1"]*86400*365/12,
            sr_data_all[1]["k1"]*86400*365/12,
        ))


def plot_distance_and_mileage(data, start, end):
    #
    # distance
    #

    plt.subplot(2, 1, 1, sharex=plt.gca())
    plt.ylabel("Distance (km)")
    plt.xlim((start, end))
    plot_grid(data["weekly"]["dates"])

    for y in [6, 12, 18, 24, 30, 36, 42]:
        plt.axhline(y, color=C_LINE)

    for run in data["runs"]:
        color = RUN2COLORS[run.__class__]
        label = RUN2LABEL[run.__class__]
        plt.bar(run.date, run.distance, align='edge', width=1, color=color, label=label)

    plot_legend()

    #
    # mileage
    #

    plt.subplot(2, 1, 2, sharex=plt.gca())
    plt.ylabel("Distance (km)")
    plt.xlim((start, end))
    plot_grid(data["weekly"]["dates"])

    plt.axhline(30, color=C_LINE, label='_nolegend_')
    plt.axhline(40, color=C_LINE, label='_nolegend_')
    plt.axhline(50, color=C_LINE, label='_nolegend_')
    plt.axhline(60, color=C_LINE, label='_nolegend_')

    plt.axhline(120, color=C_LINE, label='_nolegend_')
    plt.axhline(160, color=C_LINE, label='_nolegend_')
    plt.axhline(200, color=C_LINE, label='_nolegend_')
    plt.axhline(240, color=C_LINE, label='_nolegend_')

    ys = [dic["dist"]["a_sum"] for dic in data["monthly"]["stats"]]
    months_length = [dic["duration_days"] for dic in data["monthly"]["stats"]]
    plt.bar(data["monthly"]["dates"], ys, align='edge', width=months_length, label="Monthly")

    ys = [dic["dist"]["a_sum"] for dic in data["weekly"]["stats"]]
    weeks_length = [dic["duration_days"] for dic in data["weekly"]["stats"]]
    plt.bar(data["weekly"]["dates"], ys, align='edge', width=weeks_length, label="Weekly")

    plot_legend()


def plot_speed_prog(data, start, end):
    #
    # Speed all
    #

    plt.subplot(2, 1, 1, sharex=plt.gca())
    plt.ylabel("Speed (km/h)")
    plt.xlim((start, end))
    plt.ylim((10.0, 15.5))
    plot_grid(data["weekly"]["dates"])

    for s in range(11, 15+1):
        plt.axhline(s, color=C_LINE)

    for run in data["runs"]:
        plt.plot(run.date, run.speed, 'x', color=RUN2COLORS[run.__class__], label=RUN2LABEL[run.__class__])

    plot_legend()

    #
    # Speed prog
    #

    plt.subplot(2, 1, 2, sharex=plt.gca())
    plt.ylabel("Speed (km/h)")
    plt.xlim((start, end))
    plt.ylim((11.5, 15.5))

    for v in range(120, 150+1, 5):
        plt.axhline(v/10, color=C_LINE, label='_nolegend_')

    for m in data["monthly"]["dates"]:
        plt.axvline(m, color=C_LINE, label='_nolegend_')

    for r in data["runs"]:
        if isinstance(r, RunGoal):
            plt.plot(r.date, r.speed, 'o', color=RUN2COLORS[RunGoal], label='_nolegend_')

    legend = []
    for dist_ref, sr_data_all in data["regressions"].items():
        # plot all runs
        xs, ys = [r.date for r in sr_data_all["all"]], [r.speed for r in sr_data_all["all"]]
        p, = plt.plot(xs, ys, 'o-')
        legend.append((p, "%s km" % dist_ref))

        # plot reg
        y0 = sr_data_all[3]["k1"]*date2timestamp(start) + sr_data_all[3]["k0"]
        y1 = sr_data_all[3]["k1"]*date2timestamp(end) + sr_data_all[3]["k0"]
        plt.plot([start, end], [y0, y1], '--', color=p.get_color())

    plt.legend([tup[0] for tup in legend], [tup[1] for tup in legend])


def plot_speed_avg(data, start, end):
    #
    # Speed (Real)
    #

    plt.subplot(2, 1, 1, sharex=plt.gca())
    plt.ylabel("Speed (km/h)")
    plt.xlim((start, end))
    plt.ylim((10.0, 15.5))
    plot_grid(data["weekly"]["dates"])
    plt.axhline(14.1, color=C_LINE, label='_nolegend_')

    for m, dic in zip(data["monthly"]["dates"], data["monthly"]["stats"]):
        if len(dic["dist"]["a_all"]) == 0:
            continue

        for r in data["runs"]:
            if date_ym_eq(r.date, m):
                plt.plot(r.date, r.speed, "x", color="gray")

        plot_err_bar(m, dic["duration_days"], dic["speed"])

    #
    # Speed (Predicted)
    #

    plt.subplot(2, 1, 2, sharex=plt.gca())
    plt.ylabel("Speed (km/h)")
    plt.xlim((start, end))
    plt.ylim((10.0, 15.5))
    plot_grid(data["weekly"]["dates"])
    plt.axhline(14.1, color=C_LINE, label='_nolegend_')

    for m, dic in zip(data["monthly"]["dates"], data["monthly"]["stats"]):
        if len(dic["dist"]["a_all"]) == 0:
            continue

        for r in data["runs"]:
            if date_ym_eq(r.date, m):
                plt.plot(r.date, r.hm_speed, "x", color="gray")

        plot_err_bar(m, dic["duration_days"], dic["predicted"]["hm_speed"])


def plot_predict_time(data, start, end):
    def formatter_factory(dist):
        def formatter(x, _pos):
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
    plt.xlim((start, end))
    plt.ylim((2.50, 4.00))

    for y in range(250, 400+1, 25):
        plt.axhline(y/100, color=C_LINE)

    for r in data["runs"]:
        plt.plot(r.date, r.m_time, 'o', color=RUN2COLORS[r.__class__], label=RUN2LABEL[r.__class__])

    # TODO? plot_err_bar(m, dic["duration_days"], dic["speed"])

    plot_legend()

    #
    # Half-marathon
    #

    plt.subplot(2, 1, 2, sharex=plt.gca())
    plt.ylabel("Predicted time (h:m:s - km/h)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter_factory(21.1)))
    plt.xlim((start, end))
    plt.ylim((1.25, 2.00))

    for y in range(125, 200+1, 25):
        plt.axhline(y/100, color=C_LINE)

    for r in data["runs"]:
        plt.plot(r.date, r.hm_time, 'o', color=RUN2COLORS[r.__class__], label=RUN2LABEL[r.__class__])

    plot_legend()


def plot_predict_distance(data, start, end):
    plt.ylabel("Predicted distance (km) at 14.1 km/h")
    plt.xlim((start, end))

    plt.axhline(21.1, color=C_LINE)
    plt.axhline(42.2, color=C_LINE)

    for r in data["runs"]:
        plt.plot(r.date, r.distance, "x", color=C_LINE)
        plt.plot(r.date, r.dist_at_14_1_kmph, "o", color=RUN2COLORS[r.__class__])

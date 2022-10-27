#!/usr/bin/env python3

import json
import sys

from matplotlib import pyplot as plt
from matplotlib import ticker
import numpy as np


FIGSIZE = (1200, 900)
DPI = 100


def main():
    FILEPATH_METADATA = "./%s/metadata.json" % sys.argv[1]
    FILEPATH_DATA = "./%s/data.json" % sys.argv[1]
    FILEPATH_GRAPH_1 = "build/%s-Figure_1.png" % (sys.argv[1].replace("/", ""))
    FILEPATH_GRAPH_2 = "build/%s-Figure_2.png" % (sys.argv[1].replace("/", ""))

    PERCENTS = [1, 5, 10, 15, 20, 50]
    COLORS = ["r", "r", "g", "g", "g", "orange"]

    N_BINS = 75

    def formatter_participants_factory(scale):
        def formatter_participants(x, pos=None):
            return "%d%% (N=%d)" % (x, x/scale)
        return formatter_participants

    def formatter_time(x, pos=None):
        h = int(x / 3600)
        m = int((x % 3600) / 60)
        s = int(x % 60)

        return "%d:%02d:%02d" % (h, m, s)

    #
    # load
    #

    with open(FILEPATH_METADATA) as f:
        data = json.load(f)

    ME_TIME = data["me_time"]
    ME_RANK = data["me_rank"]
    ME_LEGEND = data["me_legend"]

    ME_COLOR = "gray"

    with open(FILEPATH_DATA) as f:
        print("Loading %s..." % FILEPATH_DATA)
        data = json.load(f)
    print("Ok!")

    #
    # prepare
    #

    SCALE = 100/len(data)

    times_all = [tup["time_raw"] for tup in data]

    indexes = [p/SCALE for p in PERCENTS]
    times_slots = [data[int(i)]["time_raw"] for i in indexes]

    #
    # plot
    #

    # f1

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatter_participants_factory(SCALE)))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter_time))
    plt.ylabel("Time")
    plt.xlabel("Runners")

    xs = [i*SCALE for i in range(1, len(times_all)+1)]
    plt.plot(xs, times_all)

    for p, c, i, t in zip(PERCENTS, COLORS, indexes, times_slots):
        legend = "p=%d%% (%d), t=%s" % (p, i, formatter_time(t))
        plt.plot((int(i)+1)*SCALE, t, "x", label=legend, color=c)

    plt.axhline(ME_TIME, label=ME_LEGEND, color=ME_COLOR)
    plt.axvline(ME_RANK*SCALE, label=ME_LEGEND, color=ME_COLOR)

    plt.legend(loc="upper left")

    plt.savefig(FILEPATH_GRAPH_1)

    # f2

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)

    plt.ylabel("Runners (histogram)")
    plt.xlabel("Time")

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatter_time))

    plt.hist(times_all, bins=N_BINS)

    for p, c, i, t in zip(PERCENTS, COLORS, indexes, times_slots):
        legend = "p=%d%% (%d), t=%s" % (p, i, formatter_time(t))
        plt.axvline(t, linestyle="--", label=legend, color=c)

    plt.axvline(ME_TIME, label=ME_LEGEND, color=ME_COLOR)

    plt.legend(loc="upper left")

    plt.savefig(FILEPATH_GRAPH_2)

    # show

    plt.show()


if __name__ == "__main__":
    main()

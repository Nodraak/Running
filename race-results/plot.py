import json
import sys

from matplotlib import pyplot as plt
from matplotlib import ticker
import numpy as np


def main():
    FILEPATH_METADATA = "./%s/metadata.json" % sys.argv[1]
    FILEPATH_DATA = "./%s/data.json" % sys.argv[1]

    PERCENTS = [1, 5, 10, 15, 20, 50]
    COLORS = ["r", "r", "g", "g", "g", "orange"]

    N_BINS = 75

    def formatter(x, pos=None):
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
    ME_LEGEND = data["me_legend"]

    with open(FILEPATH_DATA) as f:
        print("Loading %s..." % FILEPATH_DATA)
        data = json.load(f)
    print("Ok!")

    #
    # prepare
    #

    times_all = [tup["time_raw"] for tup in data]

    indexes = [len(data)*p/100 for p in PERCENTS]
    times_slots = [data[int(i)]["time_raw"] for i in indexes]

    #
    # plot
    #

    # f1

    plt.figure()

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))
    plt.ylabel("Time")
    plt.xlabel("Runners")

    plt.plot(times_all)
    for p, c, i, t in zip(PERCENTS, COLORS, indexes, times_slots):
        legend = "p=%d%% (%d), t=%s" % (p, i, formatter(t))
        plt.plot(int(i), t, "x", label=legend, color=c)

    plt.axhline(ME_TIME, label=ME_LEGEND, color="orange")

    plt.legend()

    # f2

    plt.figure()

    plt.ylabel("Runners (histogram)")
    plt.xlabel("Time")

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatter))

    plt.hist(times_all, bins=N_BINS)
    plt.axvline(ME_TIME, label=ME_LEGEND, color="orange")

    plt.legend()

    # show

    plt.show()


if __name__ == "__main__":
    main()

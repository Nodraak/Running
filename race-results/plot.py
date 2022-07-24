import json
import sys

from matplotlib import pyplot as plt
from matplotlib import ticker
import numpy as np


# TODO: automate
ME_TIME = 3600 + 46*60 + 0  # Spreewald
#ME_TIME = 3600 + 29*60 + 20  # 20 km CDGR


def main():
    FILEPATH = sys.argv[1]  # "./data.json"

    #
    # load
    #

    with open(FILEPATH) as f:
        print("Loading...")
        data = json.load(f)
    print("Ok!")

    #
    # prepare
    #

    PERCENTS = [1, 5, 10, 15, 20, 50]

    times_all = [tup["time_raw"] for tup in data]

    indexes = [len(data)*p/100 for p in PERCENTS]
    times_slots = [data[int(i)]["time_raw"] for i in indexes]

    #
    # plot
    #

    def formatter(x, pos=None):
        h = int(x / 3600)
        m = int((x % 3600) / 60)
        s = int(x % 60)

        return "%d:%02d:%02d" % (h, m, s)

    # f1

    plt.figure()

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter))

    plt.plot(times_all)
    for p, i, t in zip(PERCENTS, indexes, times_slots):
        legend = "p=%d%% (%d), t=%s" % (p, i, formatter(t))
        plt.axhline(t, label=legend)

    plt.axhline(ME_TIME, color="orange")

    plt.legend()

    # fé

    plt.figure()

    N_BINS = int(len(data)/10)

    plt.hist(times_all, bins=N_BINS)
    plt.axvline(ME_TIME, color="orange")

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatter))

    # show

    plt.show()


if __name__ == "__main__":
    main()

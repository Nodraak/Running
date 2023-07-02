#!/usr/bin/env python3
"""
## (Parsed) data format

```py
[
  [
    # basic
    name,
    gender,
    time_raw
    place_global,

    # Spreewald
    age,
    registrationdate,
    place_age,
    speed,

    # 20 km CDGR
    place_cat,
    time_net,
    nat,
  ],
]
```
"""

import json
import sys

from matplotlib import pyplot as plt
from matplotlib import ticker
import numpy as np


FILEPATH_METADATA = "{path}/metadata.json"
FILEPATH_DATA = "{path}/data.json"
FILEPATH_GRAPH_1 = "build/{path}-Figure_1.png"
FILEPATH_GRAPH_2 = "build/{path}-Figure_2.png"

PERCENTS = [0, 1, 5, 10, 15, 20, 50, 99.999]
COLORS = ["r", "r", "r", "g", "g", "g", "orange", "black"]
ME_COLOR = "gray"

N_BINS = 2*75  # TODO scale based on distance or nb of participants

FIGSIZE = (1200, 900)
DPI = 100


def formatter_participants_factory(scale):
    def formatter_participants(x, pos=None):
        return "%d%% (N=%d)" % (x, x/scale)
    return formatter_participants

def formatter_time(x, pos=None):
    h = int(x / 3600)
    m = int((x % 3600) / 60)
    s = int(x % 60)

    return "%d:%02d:%02d" % (h, m, s)


def load(folder):
    metadata_path = FILEPATH_METADATA.format(path=folder)
    data_path = FILEPATH_DATA.format(path=folder)

    #
    # load
    #

    with open(metadata_path) as f:
        print("Loading %s..." % metadata_path)
        metadata = json.load(f)

    with open(data_path) as f:
        print("Loading %s..." % data_path)
        data = json.load(f)

    print("Ok!")

    #
    # prepare
    #

    times_all = [tup["time_raw"] for tup in data]

    scale = 100/len(data)
    indexes = [int(p/scale) for p in PERCENTS]
    times_slots = [times_all[i] for i in indexes]

    return metadata, times_all, scale, indexes, times_slots


def main():
    assert len(sys.argv) == 2, "Usage: python3 race-results/plot.py race-results/2022-04-24-Spreewald-21.1km/"

    graph_1_path = FILEPATH_GRAPH_1.format(path=sys.argv[1].strip("/").replace("/", "-"))
    graph_2_path = FILEPATH_GRAPH_2.format(path=sys.argv[1].strip("/").replace("/", "-"))

    #
    # load
    #

    metadata, times_all, scale, indexes, times_slots = load(sys.argv[1])

    #
    # plot
    #

    # f1

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatter_participants_factory(scale)))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter_time))
    plt.ylabel("Time")
    plt.xlabel("Runners")

    xs = [(i+1)*scale for i in range(len(times_all))]
    plt.plot(xs, times_all)

    print("| Percent | Place |   Time   | Speed |")
    print("|---------|-------|----------|-------|")
    for p, c, i, t in zip(PERCENTS, COLORS, indexes, times_slots):
        legend = "p=%d%% (%d), t=%s" % (p, i+1, formatter_time(t))
        print("|    %3d%% | %5d |  %s |  %4.1f |" % (p, i+1, formatter_time(t), 42.2*3600/t))  # TODO: load dist from metadata
        plt.plot((i+1)*scale, t, "x", label=legend, color=c)

    plt.axhline(metadata["me_time"], label=metadata["me_legend"], color=ME_COLOR)
    plt.axvline(metadata["me_rank"]*scale, label="_nolabel", color=ME_COLOR)

    plt.legend(loc="upper left")

    plt.savefig(graph_1_path)

    # f2

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)

    plt.ylabel("Runners (histogram)")
    plt.xlabel("Time")

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(formatter_time))

    print("binsize: %d sec" % ((times_all[-1]-times_all[0])/N_BINS))
    plt.hist(times_all, bins=N_BINS)

    for p, c, i, t in zip(PERCENTS, COLORS, indexes, times_slots):
        legend = "p=%d%% (%d), t=%s" % (p, i+1, formatter_time(t))
        plt.axvline(t, linestyle="--", label=legend, color=c)

    plt.axvline(metadata["me_time"], label=metadata["me_legend"], color=ME_COLOR)

    plt.legend(loc="upper left")

    plt.savefig(graph_2_path)

    # show

    plt.show()


if __name__ == "__main__":
    main()

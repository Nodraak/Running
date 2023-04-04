"""

"""

import datetime
import json
import os
import random
import re

from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter


FOLDER_IN = "data-splits/"


def parse_time(string):
    matches = re.findall(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", string)
    assert len(matches) == 1
    assert len(matches[0]) == 3

    h, m, s = matches[0]
    if h == '': h = 0
    if m == '': m = 0
    if s == '': s = 0

    return int(h)*3600 + int(m)*60 + int(s)


def load():
    """
    Load split stats from raw files.

    Takes ~10 sec.

    For each file
        For each checkpoint
            if name == KMxx
                save totalTime and distance (name)

    Note: files with issues:
        * data-splits/splits.43640705
        * data-splits/splits.43635519

    """

    data_ret = []

    for filename in os.listdir(FOLDER_IN):
        print("Loading %s ..." % filename)

        with open(FOLDER_IN + "/" + filename) as f:
            data_json = json.load(f)

        data_splits = [(0, 0, 0)]
        for data_checkpoint in data_json:
            if data_checkpoint["name"].startswith("KM"):
                dist = int(data_checkpoint["name"][2:])
                if data_checkpoint["missing"] or "result" not in data_checkpoint:
                    data_splits.append((dist, 0, 0))
                else:
                    time_sec = parse_time(data_checkpoint["totalTime"])
                    speed_kmph = float(data_checkpoint["speed"])
                    data_splits.append((dist, time_sec, speed_kmph))

        data_ret.append(data_splits)

    print("Loaded %d files" % len(data_ret))

    return data_ret


def plot(data):
    def formatter(x, _pos):
        sec = int(x) % 60
        mn = int(x/60) % 60
        h = int(x/3600)
        return f'{h}:{mn:02d}:{sec:02d}'

    # plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter))

    for d in random.sample(data, 1000):
        xs = [tup[0] for tup in d]
        # ys = [tup[1] for tup in d]  # time
        ys = [tup[2] for tup in d]  # speed

        plt.plot(xs, ys, "x-", color="gray")



def main():
    data = load()
    plot(data)
    print("show...")
    plt.show()


main()

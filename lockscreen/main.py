#!/usr/bin/env python3

import importlib.util
import os
import sys

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np


FIGSIZE = (1024*1.3, 2048*1.3)
DPI = 100

"""
Honor:

Height: top=8, bottom=6
Length: 27 char
"""

FONTSIZE = 40
LINEHEIGHT = FONTSIZE*1.5

SCREEN_TEXTTOP_Y0 = 1230
SCREEN_TEXTBOTTOM_Y0 = 430


def checkpoint_calc_split_speeds(dtot, ttot_h, split_v):
    vtot = dtot / ttot_h

    vs = vtot+split_v/2, vtot+split_v/4, vtot-split_v/4, vtot-split_v/2

    ts = [dtot/len(vs) / v for v in vs]
    err_h = sum(ts) - ttot_h
    assert err_h*3600 < 30, "The split adjustment yields a suspicious result (err_s=%d), check the correctness of the speeds and times." % (err_h*3600)

    return vs


def checkpoint_calc_and_format_time(checkpoint_dist_km, total_dist_km, goal_time_s):
    """
    Considerations:

    * Split:
        * Positive, d=0.8 km/h for 42.2
        * Total distance split in 4 sections, assumed steady speed for each
    * Slow start: 1 mn
    """
    SPLIT_42_DV = 0.8
    SLOW_START_S = 60
    TIME_ROUND_S = 5

    # Split - Compute time taking into account 4 different velocities

    vs = checkpoint_calc_split_speeds(total_dist_km, goal_time_s/3600, SPLIT_42_DV * total_dist_km/42.2)

    time_split_s = 0
    for i, v in enumerate(vs):
        d = np.clip(checkpoint_dist_km - i/len(vs)*total_dist_km, 0, total_dist_km/len(vs))
        t_s = d / v * 3600
        time_split_s += t_s

    # Slow start - Map checkpoint_dist_km [0; total_dist_km] to [+SLOW_START_S; 0]

    time_adjust_slow_start_s = SLOW_START_S * (1 - checkpoint_dist_km/total_dist_km)

    # Time

    time_s = time_split_s + time_adjust_slow_start_s

    # Format

    time_f_m = int(time_s/60) % 60
    time_f_s = int(time_s/1) % 60

    ret = "%2d:%02d" % (time_f_m, time_f_s)

    return ret


def racescreen_setup():
    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.xlim((1, 1024))
    plt.ylim((1, 2048))


def racescreen_background():
    plt.gca().add_patch(Rectangle((1, 1), 1024, 2048, color="#E0E0E0"))

    # top
    plt.gca().add_patch(Rectangle((1, SCREEN_TEXTTOP_Y0), 1024, 8*LINEHEIGHT, fill=False, edgecolor="k", lw=1))

    # bottom
    plt.gca().add_patch(Rectangle((1, SCREEN_TEXTBOTTOM_Y0), 1024, 6*LINEHEIGHT, fill=False, edgecolor="k", lw=1))


def _racescreen_lines(conf, lines, x0, y0):
    for i, line in enumerate(lines):
        x = x0
        y = y0 + LINEHEIGHT * (len(lines) - (i + 0.5))

        km_time = conf["RACE_GOAL_TIME_S"] / conf["RACE_DIST_KM"]

        kwargs = line["kwargs"].copy()
        kwargs.update({
            "race_goal_time": conf["RACE_GOAL_TIME_S"] / 60,
            "race_goal_speed": conf["RACE_DIST_KM"] * 3600 / conf["RACE_GOAL_TIME_S"],
            "km_time": "%2d:%02d" % (km_time/60, km_time%60),
            "time": checkpoint_calc_and_format_time(line["kwargs"].get("dist", 0), conf["RACE_DIST_KM"], conf["RACE_GOAL_TIME_S"]),
        })

        txt = line["fmt"].format(**kwargs)
        assert len(txt) <= 27, "Line is too long: '%s' -> '%s'" % (line["fmt"], txt)

        plt.text(x, y, txt, fontname="monospace", weight="bold", fontsize=FONTSIZE, ha="left", va="center", **line["plt_kwargs"])


def racescreen_text(conf):
    assert len(conf["TEXT_TOP_LEFT"]) == 8
    assert len(conf["TEXT_BOTTOM_LEFT"]) == 6

    _racescreen_lines(conf, conf["TEXT_TOP_LEFT"], 70, SCREEN_TEXTTOP_Y0)
    _racescreen_lines(conf, conf["TEXT_BOTTOM_LEFT"], 70, SCREEN_TEXTBOTTOM_Y0)


def main():
    assert len(sys.argv) == 2, "Expected a config file"

    FILE = sys.argv[1]
    assert FILE.endswith(".py")

    barename, _ = os.path.splitext(os.path.basename(FILE))
    OUT = "build/" + "lockscreen-" + barename + ".png"

    spec = importlib.util.spec_from_file_location("data", FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    racescreen_setup()
    racescreen_background()
    racescreen_text(module.CONF)
    plt.savefig(OUT, bbox_inches="tight", pad_inches=0, dpi=DPI)
    print("Lockscreen saved as: %s" % OUT)
    #plt.show()


main()

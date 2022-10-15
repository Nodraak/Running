#!/usr/bin/env python3

import importlib.util
import os
import sys

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


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


def _racescreen_lines(lines, x0, y0):

    for i, (line, kwargs) in enumerate(lines):
        x = x0
        y = y0 + LINEHEIGHT * (len(lines) - (i + 0.5))
        plt.text(x, y, line, fontname="monospace", weight="bold", fontsize=FONTSIZE, ha="left", va="center", **kwargs)


def racescreen_text(text_top, text_bottom):
    _racescreen_lines(text_top, 70, SCREEN_TEXTTOP_Y0)
    _racescreen_lines(text_bottom, 70, SCREEN_TEXTBOTTOM_Y0)


def main():
    assert len(sys.argv) == 2

    FILE = sys.argv[1]
    assert FILE.endswith(".py")

    barename, _ = os.path.splitext(os.path.basename(FILE))
    OUT = "build/" + "lockscreen-" + barename + ".png"

    spec = importlib.util.spec_from_file_location("data", FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    racescreen_setup()
    racescreen_background()
    racescreen_text(module.TEXT_TOP_LEFT, module.TEXT_BOTTOM_LEFT)
    plt.savefig(OUT, bbox_inches="tight", pad_inches=0, dpi=DPI)
    #plt.show()


main()

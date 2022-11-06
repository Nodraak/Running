
from plot import load

import subprocess

from matplotlib import pyplot as plt
from matplotlib import ticker


FIGSIZE = (1200, 900)
DPI = 100

ME_COLOR = "gray"


def formatter_time(x, pos=None):
    h = int(x / 3600)
    m = int((x % 3600) / 60)
    s = int(x % 60)

    return "%d:%02d:%02d" % (h, m, s)


files_raw = subprocess.check_output("find race-results/ | grep metadata.json", shell=True).decode('utf-8')
files = [file.strip() for file in files_raw.strip().split("\n")]
folders = sorted([file[:-len("metadata.json")] for file in files])


plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)

plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(formatter_time))
plt.ylabel("Time")
plt.xlabel("Runners")

for folder in folders:
    metadata, times_all, scale, indexes, times_slots = load(folder)

    xs = [i*scale for i in range(1, len(times_all)+1)]
    legend = "%s - N=%d - %s" % (metadata["me_legend"], len(times_all), folder)

    p, = plt.plot(xs, times_all, label=legend)
    plt.plot(metadata["me_rank"]*scale, metadata["me_time"], "x", color=p.get_color(), label="_nolegend_")

plt.legend(loc="upper left")


plt.savefig("build/race-results-all.png")
plt.show()

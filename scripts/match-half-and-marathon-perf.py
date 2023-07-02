"""
Match competitors results between Boulogne's half and Paris's Marathon to find
out how fast can one expect to run a marathon based on a half marathon time.
Generates graphs and prints.

---

Boulogne: 8071
Paris:    34128
Matched:  950


Conclusions:
* 3h marathon requires half in (1h18-1h25)
* 1h25 half allows 3h14 (3h05-3h25)
* 1h27 half allows 3h17 (3h08-3h28)
* 1h29 half allows 3h21 (3h05-3h30)
* Factor marathon/half
    * Note: if less than 2.00, they clearly ran a very relaxed half
    * Formula: 2.10
    * Reality: median is around 2.20-2.30 (1.80-2.50)
    * 1h27 * 2.25 = 3h16
    * 1h25 * 2.25 = 3h11
    * 1h20 * 2.25 = 3h00
* heatmap:
    * half 1h25-1h30:
        * Factor 2.30 (2.10-2.50)
        * -> expected marathon: 3h20 (3h05-3h35)

TODOs:
    * Check age
    * How to know who did a relaxed half?
        * Look at more races
        * Look at splits and spot anything irregular

---

## Displays a graph

With the matched results:
    x=Boulogne's time
    y=Paris's time
And with y=f(x):
    y=t2=estimate_time(d1=21.1, t1=x, d2=42.2)

## Input

Boulogne:
[
    {
        "gender": "M",
        "name": "RAILEANU MAXIM",
        "place_overall": 1,
        "splits": [
          0,
          916,
          1711,
          2699,
          3789
        ],
        "time_raw": 3789
    },
    ...
]

Paris:
[
    {
        "age": 24,
        "gender": "M",
        "name": "GELMISA DESO",
        "time_raw": 7507
    },
    ...
]
"""

import json

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter


def estimate_time(d1, t1, d2, b=1.06):
    """
    Estimate the time for running distance d2, based on the performance
    (distance, time) (d1, t1). Scaling is not fully linear.

    Based on Peter Riegel's 1981's formula: T2 = T1 * (D2/D1)**1.06
    """
    # b = 1.06
    t2 = t1 * (d2 / d1)**b
    return t2


def main():

    # Load Boulogne - as dict{key:val}, where key=name, val=time_sec

    with open("race-results/2022-11-27-Boulogne-21.1km/data.json", "r") as f:
        data_b_raw = json.loads(f.read())
    data_b = {d["name"]: d["time_raw"] for d in data_b_raw}

    # Load Paris

    with open("race-results/Paris-2022/data.json", "r") as f:
        data_p_raw = json.loads(f.read())
    data_p = {d["name"]: d["time_raw"] for d in data_p_raw}


    data = []  # (half, marathon, factor)
    heatmap = [
        [0 for _ in range(4*60)] # x: half, 0-4h, step 1 min (1/60 h)
    for _ in range(5*10)]  # y: factor, 0.0-5.0, step 0.10 (1/10)
    # for data in Paris
    for p_name, p_time in data_p.items():
        # if in Boulogne
        if p_name in data_b:
            # add both times to ret
            b_time = data_b[p_name]
            data.append((b_time, p_time, p_time/b_time))

            print(int(p_time/b_time*10))
            heatmap[int(p_time/b_time*10)][int(b_time/60)] += 1

    print("Boulogne: %d" % len(data_b))
    print("Paris:    %d" % len(data_p))
    print("Matched:  %d" % len(data))

    factors = [tup[2] for tup in data]
    hist, bin_edges = np.histogram(factors, bins=2*5*2*2, range=(1.0, 3.0))
    for a, b, x in zip(bin_edges[:-1], bin_edges[1:], hist):
        print("%.2f-%.2f -> %3d" % (a, b, x))
    print("median", np.median(factors))


    # plot graphs

    def formatter_factory(dist):
        def formatter(x, _pos):
            time_sec = x

            s = int(time_sec) % 60
            m = int(time_sec/60) % 60
            h = int(time_sec/3600)

            pace_sec = time_sec / dist

            pace_secpkm_m = int(time_sec / dist / 60)
            pace_secpkm_s = int(time_sec / dist) % 60

            return f"{h:d}:{m:02d}:{s:02d}\n({pace_secpkm_m:d}:{pace_secpkm_s:02d} / km)"
        return formatter

    plt.figure()

    plt.xlabel("21.1 km (Boulogne)")
    plt.ylabel("42.2 km (Paris)")

    plt.gca().xaxis.set_major_formatter(FuncFormatter(formatter_factory(21.1)))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter_factory(42.2)))

    plt.plot(
        [3600, 3*3600],
        [estimate_time(d1=21.1, t1=3600, d2=42.2), estimate_time(d1=21.1, t1=3*3600, d2=42.2)],
        "-", color="gray",
    )

    xs = [tup[0] for tup in data]
    ys = [tup[1] for tup in data]
    plt.plot(xs, ys, "x")


    plt.figure()

    plt.imshow(heatmap, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()


    plt.show()


main()

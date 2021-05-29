#!/usr/bin/env python3

from datetime import datetime, timedelta
from matplotlib import pyplot as plt


#
# Data
#

# date, distance (km), speed (km/h), kind
RUNS = (
    ('2021-03-27', 4.14, 10.6, "ShortRun"),
    ('2021-04-02', 6.42, 11.2, "ShortRun"),
    ('2021-04-08', 6.45, 11.4, "ShortRun"),
    ('2021-04-11', 7.24, 11.0, "LongRun"),
    ('2021-04-14', 3.9, 7.5, "ShortRun"),
    ('2021-04-18', 3.3, 10.0, "LongRun"),
    ('2021-04-22', 7.8, 11.9, "ShortRun"),
    ('2021-04-24', 11.3, 11.8, "LongRun"),  # 8
    ('2021-04-27', 6.6, 11.6, "ShortRun"),  # 9

    ('2021-05-01', 13.5, 12.0, "LongRun"),  # 10
    ('2021-05-06', 6.0, 12.4, "ShortRun"),  # 11
    ('2021-05-08', 14.4, 11.9, "LongRun"),  # 12
    ('2021-05-12', 5.8, 12.3, "ShortRun"),  # 13
    ('2021-05-14', 6.4, 12.6, "ShortRun"),  # 14
    ('2021-05-15', 15.0, 11.4, "LongRun"),  # 15
    ('2021-05-18', 5.8, 12.0, "ShortRun"),  # 16
    ('2021-05-20', 4, 12, "Strides"),       # 17
    ('2021-05-23', 17.0, 10.7, "LongRun"),  # 18
    ('2021-05-25', 6.2, 12.4, "ShortRun"),  # 19
    ('2021-05-27', 6.2, 12.8, "ShortRun"),  # 20
    ('2021-05-28', 13.6, 12.4, "LongRun"),  # 21
)

# for weekly milage stats
START = '2021-03-22'  # Monday


#
# Parse/prepare
#

def parse_date(s):
    return datetime.strptime(s, '%Y-%m-%d').date()


def get_week_from_start(d):
    return d.isocalendar()[1] - START.isocalendar()[1]


# parse dates

START = parse_date(START)
RUNS = [
    (parse_date(tup[0]), *tup[1:])
    for tup in RUNS
]

# prepare date for plot 1

dates = [tup[0] for tup in RUNS]
distances = [tup[1] for tup in RUNS]
speeds = [tup[2] for tup in RUNS]
is_long_runs = [tup[3] for tup in RUNS]

# prepare date for plot 2

# date (week), milage
weekly_data = {}
for date, dist, _, _ in RUNS:
    k = START + timedelta(weeks=get_week_from_start(date))
    if k not in weekly_data:
        weekly_data[k] = 0
    weekly_data[k] += dist

weekly_data = sorted(weekly_data.items())

weekly_dates = [tup[0] for tup in weekly_data]
weekly_distances = [tup[1] for tup in weekly_data]

#
# Plot and print
#

print("Month  Distance (km)")
for m in range(3, 10):
    ds = [tup[1] for tup in RUNS if tup[0].month == m]
    print("%2d     %5d" % (m, sum(ds)))

ddist_per_week = (30-5)/((8-3.5)*(4.33-1))  # dist / (months * week_per_months)
print("ddist_per_week: %.1f km" % ddist_per_week)
dmilage_per_week = (60-5)/((8-3.5)*(4.33-1))
print("dmilage_per_week: %.1f km" % dmilage_per_week)
# env +10% per week, we're ok

plt.subplot(3, 1, 1)
plt.ylabel("Distance (km)")
for x in weekly_dates:
    plt.axvline(x, color="#E0E0E0")
plt.axhline(0, color="gray")
plt.plot([START, parse_date("2021-08-15")], [5, 30], color="gray")
plt.plot([parse_date("2021-08-15"), parse_date("2021-10-15")], [30, 25], color="gray")
plt.plot([START, parse_date("2021-08-15")], [3, 15], color="gray")
plt.plot([parse_date("2021-08-15"), parse_date("2021-10-15")], [15, 12], color="gray")
for dt, dist, kind in zip(dates, distances, is_long_runs):
    color = {
        "ShortRun": "blue",
        "LongRun": "green",
        "Strides": "red",
    }[kind]
    plt.plot(dt, dist, 'x', color=color)

plt.subplot(3, 1, 2, sharex=plt.gca())
plt.ylabel("Speed (km/h)")
for x in weekly_dates:
    plt.axvline(x, color="#E0E0E0")
plt.axhline(0, color="gray")
plt.axhline(12, color="gray")
plt.gca().set_ylim((0, 15))
for d, s, kind in zip(dates, speeds, is_long_runs):
    color = {
        "ShortRun": "blue",
        "LongRun": "green",
        "Strides": "red",
    }[kind]
    plt.plot(d, s, 'x', color=color)

plt.subplot(3, 1, 3, sharex=plt.gca())
plt.ylabel("Weekly milage (km)")
for x in weekly_dates:
    plt.axvline(x, color="#E0E0E0")
plt.axhline(0, color="gray")
plt.plot([START, parse_date("2021-05-01")], [8, 16], color="gray")
plt.plot([parse_date("2021-05-01"), parse_date("2021-08-15")], [16, 15+15+30], color="gray")
plt.plot([parse_date("2021-08-15"), parse_date("2021-10-15")], [15+15+30, 12+12+25], color="gray")
plt.plot([d+timedelta(days=3) for d in weekly_dates], weekly_distances, 'x-')  # plot on the middle of the week

plt.show()

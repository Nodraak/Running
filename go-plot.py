#!/usr/bin/env python3

from datetime import datetime, timedelta
from matplotlib import pyplot as plt


#
# Data
#

# date, distance (km), speed (km/h)
RUNS = (
    # gps not reviewed
    ('2021-03-27', 4.14, 10.6),
    ('2021-04-02', 6.42, 11.2),
    ('2021-04-08', 6.45, 11.4),
    ('2021-04-11', 7.24, 11.0),
    ('2021-04-14', 3.9, 7.5),
    ('2021-04-18', 3.3, 10.0),
    ('2021-04-22', 7.8, 11.9),
    # clean(er) gps
    ('2021-04-24', 11.3, 11.8),     # 8
    ('2021-04-27', 6.6, 11.6),      # 9
    ('2021-05-01', 13.5, 12.0),     # 10
    ('2021-05-06', 6.0, 12.4),      # 11
    ('2021-05-08', 14.4, 11.9),     # 12
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
    (parse_date(tup[0]), tup[1], tup[2])
    for tup in RUNS
]

# prepare date for plot 1

dates = [tup[0] for tup in RUNS]
distances = [tup[1] for tup in RUNS]
speeds = [tup[2] for tup in RUNS]

# prepare date for plot 2

# date (week), milage
weekly_data = {}
for date, dist, _ in RUNS:
    k = START + timedelta(weeks=get_week_from_start(date))
    if k not in weekly_data:
        weekly_data[k] = 0
    weekly_data[k] += dist

weekly_data = sorted(weekly_data.items())

weekly_dates = [tup[0] for tup in weekly_data]
weekly_distances = [tup[1] for tup in weekly_data]

#
# Plot
#

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
plt.plot([parse_date("2021-08-15"), parse_date("2021-10-15")], [30, 20], color="gray")
plt.plot(dates, distances, 'x')

plt.subplot(3, 1, 2, sharex=plt.gca())
plt.ylabel("Speed (km/h)")
for x in weekly_dates:
    plt.axvline(x, color="#E0E0E0")
plt.axhline(0, color="gray")
plt.gca().set_ylim((0, 15))
plt.plot(dates, speeds, 'x')

plt.subplot(3, 1, 3, sharex=plt.gca())
plt.ylabel("Weekly milage (km)")
for x in weekly_dates:
    plt.axvline(x, color="#E0E0E0")
plt.axhline(0, color="gray")
plt.plot([START, parse_date("2021-08-15")], [10, 15+15+30], color="gray")
plt.plot([parse_date("2021-08-15"), parse_date("2021-10-15")], [15+15+30, 10+10+20], color="gray")
plt.plot([d+timedelta(days=3) for d in weekly_dates], weekly_distances, 'x-')  # plot on the middle of the week

plt.show()

"""
"""

import json
from matplotlib import pyplot as plt
import numpy as np

FILEPATH = "./data/data.json"

with open(FILEPATH) as f:
    print("Loading...")
    data = json.load(f)
print("Ok!")

# {
#   "firstname lastname": [
#     (gender, age, registrationdate),
#     (place_global, place_age, time_raw, speed),
#   ],
# }

data_42 = data["42"].values()
data_42_ages_all = [tup[0][1] for tup in data_42]
data_42_ages_men = [tup[0][1] for tup in data_42 if tup[0][0] == "m"]
data_42_ages_women = [tup[0][1] for tup in data_42 if tup[0][0] == "w"]

data_21 = data["21"].values()
data_21_ages_all = [tup[0][1] for tup in data_21]
data_21_ages_men = [tup[0][1] for tup in data_21 if tup[0][0] == "m"]
data_21_ages_women = [tup[0][1] for tup in data_21 if tup[0][0] == "w"]

def age_speed_filter(tup):
    return (tup[1] is not None) and (tup[1][3] < 21)

age_speed_21 = [(tup[0][1], tup[1][3]) for tup in data["21"].values() if age_speed_filter(tup)]
age_speed_42 = [(tup[0][1], tup[1][3]) for tup in data["42"].values() if age_speed_filter(tup)]


plt.figure()

plt.subplot(2, 1, 1, title="42")
bins = range(min(data_42_ages_all), max(data_42_ages_all)+1)
plt.hist(data_42_ages_men, bins=bins, histtype="step", label="men")
plt.hist(data_42_ages_women, bins=bins, histtype="step", label="women")
plt.xlim((15, 85))
plt.legend(loc="upper right")

plt.subplot(2, 1, 2, title="21")
bins = range(min(data_21_ages_all), max(data_21_ages_all)+1)
plt.hist(data_21_ages_men, bins=bins, histtype="step", label="men")
plt.hist(data_21_ages_women, bins=bins, histtype="step", label="women")
plt.xlim((15, 85))
plt.legend(loc="upper right")


left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005
rect_plot = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

fig = plt.figure()

ax = fig.add_axes(rect_plot)
ax_histx = fig.add_axes(rect_histx, sharex=ax)
ax_histy = fig.add_axes(rect_histy, sharey=ax)

#plt.subplot(2, 1, 1, title="42")
xs = [tup[0] for tup in age_speed_42]
ys = [tup[1] for tup in age_speed_42]
#plt.plot(xs, ys, "x")
#plt.hist2d(xs, ys, bins=[80, 40])
ax.hist2d(xs, ys, bins=[80, 40])
ax_histx.hist(xs, bins=80)
ax_histy.hist(ys, bins=40, orientation='horizontal')
plt.xlabel("age (years)")
plt.ylabel("speed (km/h)")
#plt.xlim((15, 85))
#plt.ylim((-1, 21))
#plt.ylim((6, 16))




fig = plt.figure()

ax = fig.add_axes(rect_plot)
ax_histx = fig.add_axes(rect_histx, sharex=ax)
ax_histy = fig.add_axes(rect_histy, sharey=ax)

#plt.subplot(2, 1, 2, title="21")
xs = [tup[0] for tup in age_speed_21]
ys = [tup[1] for tup in age_speed_21]
#plt.plot(xs, ys, "x")
#plt.hist2d(xs, ys, bins=[80, 40])
ax.hist2d(xs, ys, bins=[80, 40])
ax_histx.hist(xs, bins=80)
ax_histy.hist(ys, bins=40, orientation='horizontal')
plt.xlabel("age (years)")
plt.ylabel("speed (km/h)")
#plt.xlim((15, 85))
#plt.ylim((-1, 21))
#plt.ylim((6, 16))


"""
get all times, sort, plot
plot 25%, 20%, 10%, 5%, 2%, 1%
legend pace, time
"""



plt.show()

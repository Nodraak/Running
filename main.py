#!/usr/bin/env python3

from dateutil import rrule
from matplotlib import pyplot as plt

from data import date2datetime, pd, RUNS
from plot import plot_distance, plot_milage, plot_avg, plot_speed_simple, plot_speed_prog, plot_temp, plot_predict_times
from process import process_mileage, process_speed, process_predict_times


#START = pd('2020-11-23')  # Monday
#START = pd('2021-03-22')  # Monday
START = pd('2022-01-03')  # Monday
MID = pd("2022-10-15")
END = pd("2023-05-01")


START_WEEKLY = START.replace(day=START.day-START.weekday())
START_MONTHLY = START.replace(day=1)


FIGSIZE = (1200, 900)
DPI = 100


def main():
    dates_monthly = [d.date() for d in rrule.rrule(rrule.MONTHLY, dtstart=START_MONTHLY, until=END)]
    dates_weekly = [d.date() for d in rrule.rrule(rrule.WEEKLY, dtstart=START_WEEKLY, until=END)]

    t0 = date2datetime(START) # date2datetime(pd('2022-03-01'))
    t1 = date2datetime(END) # date2datetime(pd('2022-11-01'))

    mileage_monthly, mileage_weekly = process_mileage(RUNS, dates_monthly, dates_weekly)
    speed_regressions = process_speed(RUNS, t0, t1)
    predicted_times = process_predict_times(RUNS)

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Milage")
    plt.xlim((START, MID))
    plot_distance((2, 1, 1), dates_weekly, RUNS)
    plot_milage((2, 1, 2), dates_monthly, dates_weekly, mileage_monthly, mileage_weekly)
    plt.savefig("build/trainings-1-milage.png")

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Speed")
    plt.xlim((START, END))
    #plt.xlim((date2datetime(pd('2022-02-01')), date2datetime(pd('2023-05-01'))))
    plot_speed_simple((2, 1, 1), dates_weekly, RUNS)
    plot_speed_prog((2, 1, 2), speed_regressions)
    plt.savefig("build/trainings-2-speed-prog.png")

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Speed (monthly average)")
    plt.xlim((START, MID))
    plot_avg((1, 1, 1), dates_monthly, dates_weekly, mileage_monthly, mileage_weekly)
    plt.savefig("build/trainings-3-speed-avg.png")

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Temperature")
    plt.xlim((START, END))
    plot_temp(speed_regressions)
    plt.savefig("build/trainings-4-temp.png")

    plt.figure(figsize=(FIGSIZE[0]/DPI, FIGSIZE[1]/DPI), dpi=DPI)
    plt.suptitle("Predicted marathon and half-marathon times")
    plt.xlim((START, END))
    plot_predict_times(predicted_times)
    plt.savefig("build/trainings-5-predict-marathon.png")

    plt.show()


if __name__ == "__main__":
    main()

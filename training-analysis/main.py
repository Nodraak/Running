#!/usr/bin/env python3
"""
Entrypoint.
"""

from data import RUNS
from plot import plot_all
from process import process_all
from utils import pd


#START = pd('2020-11-23')  # Monday
#START = pd('2021-03-22')  # Monday
#START = pd('2022-01-03')  # Monday
START = pd('2022-12-05')  # Monday
# END = pd("2023-04-30")
END = pd("2023-09-30")


def main():
    data = process_all(RUNS, START, END)
    plot_all(data, START, END)


if __name__ == "__main__":
    main()

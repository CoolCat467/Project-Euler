"""Project Euler - Problem 19 Prototype."""

# Programmed by CoolCat467

from __future__ import annotations

# Project Euler - Problem 19 Prototype
# Copyright (C) 2025  CoolCat467
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https:#www.gnu.org/licenses/>.

__title__ = "Project Euler - Problem 19 Prototype"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"


from enum import IntEnum, auto

# You are given the following information, but you may prefer to do some
# research for yourself.
#
#     1 Jan 1900 was a Monday.
#
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#
#     A leap year occurs on any year evenly divisible by 4, but not on a
#     century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?


def is_leap_year(year: int) -> bool:
    """Return if given year is a leap year.

    A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.
    """
    return not year % 400 if not year % 100 else not year % 4


def get_month_group(year: int) -> tuple[int, ...]:
    """Return tuple of days per month given current year."""
    return (
        31,
        28 + is_leap_year(year),  # February
        31,
        30,  # April
        31,
        30,  # June
        31,
        31,
        30,  # September
        31,
        30,  # November
        31,
    )


def get_days_in_year(year: int) -> int:
    """Return number of days in a year."""
    return 365 + is_leap_year(year)


def get_month(day_of_year: int, year: int) -> int:
    """Return month number given day of year (/365) and which year it is."""
    n = day_of_year
    for index, value in enumerate(get_month_group(year)):
        n -= value
        if n <= 0:
            return index + 1
    raise ValueError("Day of year is too large.")


def get_global_day(year: int, month: int, month_offset: int = 0) -> int:
    """Return global day in days since January 0th, 1900 (December 31st 1899)."""
    if year < 1900:
        raise ValueError("Year is pre-1900!")
    day = month_offset
    for current_year in range(1900, year):
        day += get_days_in_year(current_year)
    for days_in_month in get_month_group(year)[: month - 1]:
        day += days_in_month
    return day


def get_date_from_global_day(global_day: int) -> tuple[int, int, int]:
    """Return (year, month, day) from days since January 0th, 1900. (December 31st 1899)."""
    year = 1900
    day = global_day

    while day > 365:
        day -= get_days_in_year(year)
        year += 1

    month = 0
    for month, days_in_month in enumerate(get_month_group(year)):  # noqa: B007
        if day < days_in_month:
            break
        day -= days_in_month
    return year, month + 1, day


class Day(IntEnum):
    """Day of the week."""

    sunday = 0
    monday = auto()
    tuesday = auto()
    wednesday = auto()
    thursday = auto()
    friday = auto()
    saturday = auto()


def get_day_of_week_global_day(global_day: int) -> Day:
    """Return what day of the week it is.

    0 - Sunday
    1 - Monday
    2 - Tuesday
    3 - Wednesday
    4 - Thursday
    5 - Friday
    6 - Saturday
    """
    return Day(global_day % 7)


def get_day_of_week(year: int, month: int, month_offset: int = 0) -> Day:
    """Return what day of the week it is.

    0 - Sunday
    1 - Monday
    2 - Tuesday
    3 - Wednesday
    4 - Thursday
    5 - Friday
    6 - Saturday
    """
    global_day = get_global_day(year, month, month_offset)
    return get_day_of_week_global_day(global_day)


def run() -> None:
    """Run program."""
    # print(f"{is_leap_year(1900) = }")
    # print(f"{is_leap_year(1904) = }")
    # print(f"{is_leap_year(2000) = }")
    # print(f"{get_global_day(2025, 1, 27) = }")
    # print(f"{get_day_of_week(2025, 1, 27) = }")

    # How many Sundays fell on the first of the month during the twentieth
    # century (1 Jan 1901 to 31 Dec 2000)?
    sunday_count = 0
    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            if get_day_of_week(year, month, 1) == Day.sunday:
                sunday_count += 1
    print(f"{sunday_count = }")


if __name__ == "__main__":
    print(f"{__title__}\nProgrammed by {__author__}.\n")
    run()

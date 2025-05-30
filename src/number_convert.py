"""Program that converts numbers to words and vise-versa."""

from __future__ import annotations

# Number convert
# Copyright (C) 2021-2025  CoolCat467
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

__title__ = "number_convert"
__author__ = "CoolCat467"
__license__ = "GNU General Public License Version 3"
__version__ = "0.0.2"

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Collection

FULL = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty": "20",
    "thirty": "30",
    "forty": "40",
    "fifty": "50",
    "sixty": "60",
    "seventy": "70",
    "eighty": "80",
    "ninety": "90",
    "hundred": "100",
    "thousand": "1000",
    "million": "1000000",
    "billion": "1000000000",
    "trillion": "1000000000000",
}

SINGLE = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

PLACELAYERS = ("trillion", "billion", "million", "thousand")


def text_to_number(data: str) -> int:
    """Return integer representation of a number as words."""
    cur = data.split(" ")
    # get places
    values = [int(FULL[x]) for x in cur]
    # for value in values:
    #     if parts and value > parts[-1]:
    #         parts[-1] *= value
    #     else:
    #         parts.append(value)
    results = [0]
    for _idx, item in enumerate(values):
        if item == 100:
            if not results:
                results.append(0)
            results[-1] *= max(1, item)
        elif item < 100:
            if not results:
                results.append(item)
            else:
                results[-1] += item
        else:
            vsum = 0
            for value in results:
                if value < item:
                    vsum += value
            results[-1] = value
            results[-1] *= max(1, item)
            results.append(0)
    return sum(results)


def split_by(
    value: int,
    divs: Collection[int],
    delzero: bool = False,
) -> dict[int, int]:
    """Split a value into sections defined by the divisors in divs.

    Args:
        value (int): The value to be split.
        divs (Collection[int]): A collection of integers that define the divisors.
        delzero (bool): If True, exclude divisors with a remainder of zero from the output.
            Defaults to False.

    Returns:
        A dictionary containing the remainders of the value divided by each divisor in divs.
        The keys are the divisors, and the values are the corresponding remainders.

    """
    value = int(value)

    ret = {}
    for num in sorted(iter(set(divs) - {0}), reverse=True):
        remains, value = divmod(value, num)
        if delzero and remains == 0:
            continue
        ret[num] = remains
    return ret


##def number_to_text(data: int) -> str:
##    """Convert number to string."""
##    # Remember if negative
##    is_negative = False
##    if data < 0:
##        data = abs(data)
##        is_negative = True
##
##    revfull = {int(v): k for k, v in FULL.items()}
##
##    if data == 0:
##        return revfull[data]
##    del revfull[0]  # otherwise zero division later
##
##    revsing = {int(v): k for k, v in SINGLE.items()}
##
##    # get parts of full
##    split = split_by(data, tuple(revfull.keys()), True)
##    text = ""
##    if is_negative:
##        text += "negative "
##
##    # keep track of numbers left to represent
##    left = data
##    for k, val in split.items():
##        left -= val * k
##        # If data to represent in this chunk > 100
##        ##        if data - left > 100:
##        # Get 100s, 10s, and 1s
##        kval = split_by(val, (100, 10, 1), True)
##        if 100 in kval:
##            text += revsing[kval[100]] + " " + revfull[100] + " "
##        if 10 in kval:
##            text += revfull[kval[10] * 10] + " "
##        ##        if 1 in kval:  # and left > 10:
##        parts = split_by(kval[1], revsing.keys(), True)
##        if left > 10 or k >= 100:
##            text += " ".join(revsing[pk] for pk in parts) + " "
##        text += revfull[k] + " "
##        if k == 100:
##            text += "and "
##    return text[:-1].removesuffix(" and")  # no trailing space


def number_to_text(data: int) -> str:
    """Convert number to string in British English format."""
    if data == 0:
        return "zero"

    # Dictionaries for number words
    revfull = {int(v): k for k, v in FULL.items()}
    revsing = {int(v): k for k, v in SINGLE.items()}

    # Place value names
    place_layers = [
        (1_000_000_000_000, "trillion"),
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
    ]

    parts = []

    if data < 0:
        parts.append("negative")
        data = -data

    # Process each place value
    for value, name in place_layers:
        if data >= value:
            count, data = divmod(data, value)
            parts.append(number_to_text(count) + " " + name)

    # Handle hundreds
    if data >= 100:
        hundreds, data = divmod(data, 100)
        parts.append(revsing[hundreds] + " hundred")
        if data > 0:
            parts.append("and")

    # Handle tens and units
    if data >= 20:
        tens, data = divmod(data, 10)
        parts.append(revfull[tens * 10])

    if data > 0:
        parts.append(revfull[data])

    return " ".join(parts)


# def number_to_text(data:int) -> str:
#    #input is int
#    trillions = ['100000000000000', '1000000000000']
#    billions  = ['100000000000',    '1000000000']
#    millions  = ['100000000',       '1000000']
#    thousands = ['100000',          '1000']
#    hundreds  = ['100',             '1']
#    allplaces = []
#    allplaces.extend(trillions)
#    allplaces.extend(billions)
#    allplaces.extend(millions)
#    allplaces.extend(thousands)
#    allplaces.extend(hundreds)
#    typelist = ('trillion', 'billion', 'million', 'thousand', '', '')
#    read = ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9))
#    cur = int(data)
#    tmp = []
#    lst = list(SINGLE.keys())#words list
#    for i in range(5):
#        for ii in range(2):
#            if not cur == 0:
#                dtmp = (cur / int(allplaces[read[i][ii]]))#divide and get float
#                if int(dtmp) >= 1:#did divide into place?
#                    lst = list(FULL.keys())#words list
#                    if str(int(dtmp)) in list(FULL.values()):
#                        idx = int(tuple(FULL.values()).index(str(int(dtmp))))#index pos
#                        tmp.append(lst[idx])#remember tens and one pos
#                    else:#if no representation
#                        pos = int(int(dtmp) - (int(dtmp) % 10))
#                        #get position for one less place value
#                        if str(pos) in list(FULL.values()):#
#                            idx = int(tuple(FULL.values()).index(str(int(pos))))
#                            pos = lst[idx]
#                            if pos != 'zero':
#                                tmp.append(pos)

#                        pos = int(int(dtmp) % 10)
#                        if str(pos) in list(FULL.values()):
#                            idx = int(tuple(FULL.values()).index(str(int(pos))))
#                            pos = lst[idx]
#                            if pos != 'zero':
#                                tmp.append(pos)
#                    if ii == 0:
#                        tmp.append('hundred')
#                    else:
#                        tmp.append(typelist[i])
#                    cur = int(cur - (int(allplaces[read[i][ii]])) * int(dtmp))
#                    #decrease num accordingly
#    cur = tmp
#    cur = []
#    for i in tmp:#add spaces so it looks nice
#        cur.append(i+' ')
#    tmp = list(str(''.join(cur)))
#    del tmp[len(tmp)-1]
#    if (''.join(''.join(tmp).split('trillion billion million thousand hundred '))) in tuple(SINGLE.values()):
#        tmp = ['error']
#    tmp = list(str(''.join(tmp)))
#    toret = str(''.join(tmp[0:len(tmp)-1]))
#    return toret


def run() -> None:
    """Run example."""
    valuetext = (
        "five hundred seventy six trillion one hundred "
        "twenty seven billion four hundred fifty eight "
        "million seven hundred eighty four thousand three "
        "hundred thirty two"
    )
    # valuetext = 'one hundred thousand'

    value = text_to_number(valuetext)

    vtext2 = number_to_text(value)
    print(valuetext)
    print(value)
    print(vtext2)
    if valuetext == vtext2:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    run()

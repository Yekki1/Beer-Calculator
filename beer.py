#!/usr/bin/env python
"""Calculate if you have enough beers left.

Usage:
    python beer.py weeksinquarantine beersleft drinksperweek
    e.g python3 beer.py 3 12 1
"""

import sys
import math

def main(weeks, beerleft, drinksperweek):
    if drinksperweek > 1:
        print("Assuming", drinksperweek, "beers a week with an extra 5 just in case!")
    else:
        print("Assuming", drinksperweek, "beers a week with an extra 5 just in case!")
    for weeksleft in reversed(range(1, weeks+1)):
        beerplurarl = lambda beersleft : f"beer{'s'[beerleft==1:]!s}"
        weeksplurarl = lambda weeksleft : f"week{'s'[weeksleft==1:]!s}"
        if beerleft > 5:
            print(f"{beerleft!s} {beerplurarl(beerleft)!s} for {weeksleft!s} {weeksplurarl(weeksleft)!s} left in quarantine - Probably enough beer")
        else:
            print(f"{beerleft!s} {beerplurarl(beerleft)!s} for {weeksleft!s} {weeksplurarl(weeksleft)!s} left in quarantine - You will run out of beer. Order more!!!!")
        beerleft = max(0, beerleft - drinksperweek)
    else:
        print(f"GO TO THE PUB YOU ARE OUT OF QUARANTINE!!")




if __name__ == '__main__':
    if len(sys.argv) !=4:
        print("Usage: python beer.py weeks-in-quarantine beers-left drinks-per-week (e.g python3 beer.py 3 12 1)")
        raise SystemExit(0)
    else:
        try:
            w = int(sys.argv[1])
            b = int(sys.argv[2])
            d = int(sys.argv[3])
            main(w,b,d)
        except ValueError:
            print("One of these is not a number, dumbarse")
        raise SystemExit(1)

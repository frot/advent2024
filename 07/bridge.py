#!/bin/env python3

import fileinput

ee = [[int(n.strip(':')) for n in ln.strip().split()] for ln in fileinput.input(encoding="utf-8")]


def find1(n, z, nn):
    if n > z and len(nn):
        find1(n, z+nn[0], nn[1:])
        find1(n, z*nn[0], nn[1:])
    else:
        if n == z:
            raise Exception()


def find2(n, z, nn):
    if n > z and len(nn):
        find2(n, z+nn[0], nn[1:])
        find2(n, z*nn[0], nn[1:])
        find2(n, int(f"{z}{nn[0]}"), nn[1:])
    else:
        if n == z:
            raise Exception()


total1 = 0
total2 = 0
for e in ee:
    x = e.pop(0)

    try:
        find1(x, e[0], e[1:])
    except:
        total1 += x

    try:
        find2(x, e[0], e[1:])
    except:
        total2 += x

print(total1)
print(total2)

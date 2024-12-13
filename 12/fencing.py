#!/bin/env python3

import fileinput
from itertools import groupby

mm = [r.strip() for r in fileinput.input(encoding="utf-8")]
aa = [[[[(r, c)], 4] for c in range(len(mm[r]))] for r in range(len(mm))]

# Part 1
for r, rr in enumerate(mm):
    for c, cc in enumerate(rr):
        if c > 0 and mm[r][c - 1] == cc:
            aa[r][c - 1][0].extend(aa[r][c][0])
            aa[r][c - 1][1] += aa[r][c][1] - 2
            aa[r][c] = aa[r][c - 1]
        if r > 0 and mm[r - 1][c] == cc:
            if aa[r - 1][c] is aa[r][c]:
                aa[r - 1][c][1] -= 2
            else:
                aa[r - 1][c][0].extend(aa[r][c][0])
                aa[r - 1][c][1] += aa[r][c][1] - 2
                for r1, c1 in aa[r][c][0]:
                    aa[r1][c1] = aa[r - 1][c]

cost = 0
grps = []
for r in aa:
    for c in r:
        if c[1]:
            cost += len(c[0]) * c[1]
            grps.append(c[0])
            c[1] = 0
print(cost)

# Part2
cost = 0
for g in grps:
    s = set(g)
    sides = 0
    for r, c in sorted(g):
        if (r, c - 1) in s:
            if (r - 1, c) in s:
                if (r - 1, c + 1) in s:
                    tmp = 0
                else:
                    tmp = -2
            elif (r - 1, c - 1) in s:
                tmp = 2
            else:
                tmp = 0
        elif (r - 1, c) in s:
            if (r - 1, c - 1) in s:
                if (r - 1, c + 1) in s:
                    tmp = 4
                else:
                    tmp = 2
            elif (r - 1, c + 1) in s:
                tmp = 2
            else:
                tmp = 0
        else:
            tmp = 4
        sides += tmp
        # print(r, c, tmp, sides)
    cost += len(g) * sides
    # print(sides, g)
    # print(len(g) * sides)
print(cost)

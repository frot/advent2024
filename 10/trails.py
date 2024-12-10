#!/bin/env python3

import fileinput

mm = [[int(c) for c in r.strip()] for r in fileinput.input(encoding="utf-8")]
rm = len(mm)-1
cm = len(mm[0])-1


def find(r, c, h):
    ret = 0
    if mm[r][c] == h:
        if h == 9:
            th.add((r, c))
            ret = 1
        else:
            if r > 0:  ret += find(r - 1, c, h + 1)
            if r < rm: ret += find(r + 1, c, h + 1)
            if c > 0:  ret += find(r, c - 1, h + 1)
            if c < cm: ret += find(r, c + 1, h + 1)
    return ret


total1 = 0
total2 = 0
for r,rr in enumerate(mm):
    for c,cc in enumerate(rr):
        if cc == 0:
            th = set()
            total2 += find(r, c, 0)
            total1 += len(th)

print(total1)
print(total2)

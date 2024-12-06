#!/bin/env python3

import fileinput

DD = ((-1,0), (0,1), (1,0), (0,-1))

mm = [[c for c in ln.strip()] for ln in fileinput.input(encoding="utf-8")]
h0, w0 = len(mm), len(mm[0])
r0, c0 = next((r, c) for r, rr in enumerate(mm) for c, cc in enumerate(rr) if cc == '^')

# Part 1
d, v = 0, set()
r, c = r0, c0
while True:
    v.add((r, c))
    r1, c1 = r + DD[d][0], c + DD[d][1]
    if not ((0 <= r1 < h0) and (0 <= c1 < w0)): break
    if mm[r1][c1] == '#':
        d = (d + 1) % 4
    else:
        r, c = r1, c1
print(len(v))

# Part 2
count = 0
v.remove((r0, c0))
for o in v:
    mm[o[0]][o[1]] = '#'
    d, v2 = 0, set()
    r, c = r0, c0
    while True:
        v2.add((r, c, d))
        r1, c1 = r + DD[d][0], c + DD[d][1]
        if not ((0 <= r1 < h0) and (0 <= c1 < w0)): break
        if mm[r1][c1] == '#':
            d = (d + 1) % 4
        else:
            r, c = r1, c1
        if (r, c, d) in v2:
            count += 1
            break
    mm[o[0]][o[1]] = '.'
print(count)

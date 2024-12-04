#!/bin/env python3

import fileinput

s1 = [line.strip() for line in fileinput.input(encoding="utf-8")]

# Part 1
n = len(s1[0])
ss = (s1 +
      [''.join(row[col] for row in s1) for col in range(n)] +
      [''.join(row[col+off] for off,row in enumerate(s1, start=4-n) if 0<=(col+off)<n) for col in range(len(s1)+n-7)] +
      [''.join(row[col-off] for off,row in enumerate(s1, start=-3) if 0<=(col-off)<n) for col in range(len(s1)+n-7)])
total = sum(s.count("XMAS") + s.count("SAMX") for s in ss)
print(total)

# Part 2
total = 0
ms = [('M', 'S'), ('S', 'M')]
for r,s in enumerate(s1[1:-1], start=1):
    for c,ch in enumerate(s[1:-1], start=1):
        if (ch == 'A' and
            (s1[r-1][c-1], s1[r+1][c+1]) in ms and (s1[r+1][c-1], s1[r-1][c+1]) in ms):
            total += 1
print(total)

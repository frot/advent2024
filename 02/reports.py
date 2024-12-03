#!/bin/env python3

import fileinput

rr = [[int(x) for x in line.strip().split()] for line in fileinput.input(encoding="utf-8")]

# Part 1
count = 0
for r in rr:
    if r[0] < r[1]:
        x = lambda a,b: b-a
    else:
        x = lambda a,b: a-b
    if all(1 <= n <= 3 for n in (x(a,b) for a,b in zip(r[:-1], r[1:]))):
        count += 1
print(count)

# Part 2
count = 0
for r1 in rr:
    r = r1
    for i in range(len(r1)+1):
        if r[0] < r[1]:
            x = lambda a,b: b-a
        else:
            x = lambda a,b: a-b
        if all(1 <= n <= 3 for n in (x(a,b) for a,b in zip(r[:-1], r[1:]))):
            count += 1
            break
        r = r1[:i] + r1[i+1:]
print(count)

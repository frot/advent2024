#!/bin/env python3

import fileinput
from collections import defaultdict

rules = defaultdict(set)
with fileinput.input(encoding="utf-8") as i:
    while((ln:=next(i)) and '|' in ln):
        a,b = ln.strip().split('|')
        rules[a].add(b)
    pages = [[n for n in ln.strip().split(',')] for ln in i]

# Part 1
total = 0
for pp in pages:
    s = set()
    for p in pp:
        if s & rules[p]: break
        s.add(p)
    else:
        total += int(pp[len(pp)//2])
print(total)

# Part 2
total = 0
for pp in pages:
    fix = False
    while True:
        s = set()
        for i,p in enumerate(pp):
            if s & rules[p]:
                fix = True
                pp[i], pp[i-1] = pp[i-1], pp[i]
                break
            s.add(p)
        else:
            if fix: total += int(pp[len(pp)//2])
            break
print(total)

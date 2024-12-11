#!/bin/env python3

import fileinput
from collections import Counter

nn = Counter(int(s) for s in next(fileinput.input(encoding="utf-8")).strip().split())

for i in range(75):
    if i == 25: print(nn.total())  # Part 1

    nn1 = Counter()
    for s, c in nn.items():
        if s == 0:
            nn1[1] += c
        elif (ls := len(ss := str(s))) & 1 == 0:
            nn1[int(ss[:ls//2])] += c
            nn1[int(ss[ls//2:])] += c
        else:
            nn1[s*2024] += c
        nn = nn1

print(nn.total())  # Part 2

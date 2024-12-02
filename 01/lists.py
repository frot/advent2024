#!/bin/env python3

import fileinput
from functools import reduce
from collections import Counter

n1, n2 = zip(*((int(x) for x in line.strip().split()) for line in fileinput.input(encoding="utf-8")))

# Part 1
s = reduce(lambda a, n: a+abs(n[0]-n[1]), zip(sorted(n1), sorted(n2)), 0)
print(s)

# Part 2
d2 = Counter(n2)
s = reduce(lambda a, n: a+(n*d2[n]), n1, 0)
print(s)

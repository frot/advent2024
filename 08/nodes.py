#!/bin/env python3

import fileinput
from collections import defaultdict

nn = defaultdict(list)
for r,rr in enumerate(fileinput.input(encoding="utf-8")):
    for c,cc in enumerate(rr.strip()):
        if cc != '.':
            nn[cc].append((r, c))


# Part 1
nodes = set()
for n in nn.values():
    for i,n1 in enumerate(n[:-1], 1):
        for n2 in n[i:]:
            dr, dc = n2[0] - n1[0], n2[1] - n1[1]
            nodes.add((n1[0] - dr, n1[1] - dc))
            nodes.add((n2[0] + dr, n2[1] + dc))

print(sum(1 for n in nodes if 0 <= n[0] <= r and 0 <= n[1] <= c))


# Part 2
nodes = set()
for n in nn.values():
    for i,n1 in enumerate(n[:-1], 1):
        for n2 in n[i:]:
            dr, dc = n2[0] - n1[0], n2[1] - n1[1]
            nr, nc = n1
            while 0 <= nr and 0 <= nc <= c:
                nodes.add((nr, nc))
                nr, nc = nr - dr, nc - dc
            nr, nc = n2
            while nr <= r and 0 <= nc <= c:
                nodes.add((nr, nc))
                nr, nc = nr + dr, nc + dc

print(len(nodes))

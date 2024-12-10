#!/bin/env python3

import fileinput

dd = next(fileinput.input(encoding="utf-8")).strip()


# Part 1
disk = []
for i,d in enumerate(dd):
    if i&1:
        disk.extend([-1]*int(d))
    else:
        disk.extend([i//2]*int(d))

i, j = 0, len(disk)-1
while j > i:
    while j > i and disk[i] >= 0:
        i += 1
    while j > i and disk[i] < 0 and disk[j] >= 0:
        disk[i] = disk[j]
        i += 1
        j -= 1
    while j > i and disk[j] < 0:
        j -= 1

i = i + i%2
print(sum(a*b for a,b in enumerate(disk[:i])))


# Part 2
dd += "0"
disk = [[n, int(a), int(b)] for n, (a, b) in enumerate(zip(dd[::2], dd[1::2]))]

i = len(disk)-1
while i > 0:
    for j in range(i):
        if disk[j][2] >= disk[i][1]:
            tmp = disk.pop(i)
            disk[i - 1][2] += tmp[1] + tmp[2]
            tmp[2] = disk[j][2] - tmp[1]
            disk[j][2] = 0
            disk.insert(j + 1, tmp)
            break
    else:
        i -= 1

csum = 0
pos = 0
for n,a,b in disk:
    csum += int(n*a*(pos+((a-1)/2)))
    pos += a+b
print(csum)

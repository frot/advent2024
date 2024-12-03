#!/bin/env python3

import fileinput
import re

# Part 1
RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
s = sum(int(a)*int(b) for line in fileinput.input(encoding="utf-8") for a,b in RE.findall(line))
print(s)

# Part 2
RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do(?:n't)?)\(\)")
def f(a, b, c):
    if c:
        f.domul = 1 if c == "do" else 0
        return 0
    else:
        return f.domul*int(a)*int(b)

f.domul = 1
s = sum(f(a,b,c) for line in fileinput.input(encoding="utf-8") for a,b,c in RE.findall(line))
print(s)

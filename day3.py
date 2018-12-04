from collections import Counter
import itertools
import re

rect_re = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', re.I)

with open('input/day3.txt') as f:
    l = f.read().split('\n')[:-1]

rects = [list(map(int, rect_re.match(line).groups())) for line in l]


fabric = [[0]*1000 for i in range(1000)]

for rect in rects:
    for i in range(rect[3]):
        for j in range(rect[4]):
            if fabric[rect[1] + i][rect[2] + j] != 0:
                fabric[rect[1] + i][rect[2] + j] = -1
            else:
                fabric[rect[1] + i][rect[2] + j] = rect[0]

overlap = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] == -1:
            overlap +=1

print('Part 1:', overlap)

no_overlap = -1

for rect in rects:
    has_overlap = False
    for i in range(rect[3]):
        for j in range(rect[4]):
            if fabric[rect[1] + i][rect[2] + j] == -1:
                has_overlap = True
                break
        if has_overlap:
            break
    if not has_overlap:
        print('Part 2:', rect[0])
        break

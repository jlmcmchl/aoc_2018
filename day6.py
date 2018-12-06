from collections import Counter, defaultdict
from functools import reduce


def flatten(l): return [i for subl in l for i in subl]


def dist(p, q): return abs(p[0] - q[0]) + abs(p[1] - q[1])


def closest_point(coord, points):
    options = sorted(points, key=lambda x: dist(x, coord))
    if dist(options[0], coord) == dist(options[1], coord):
        return (0, 0)
    return options[0]


with open('input/day6.txt') as f:
    points = list(map(lambda x: tuple(int(c)
                                      for c in x.split(',')), f.read().split('\n')[:-1]))

min_x = min(points, key=lambda x: x[0])[0]
max_x = max(points, key=lambda x: x[0])[0]
min_y = min(points, key=lambda x: x[1])[1]
max_y = max(points, key=lambda x: x[1])[1]

infinite_areas = set()


for i in range(360):
    update = set([
        closest_point((0, i), points),
        closest_point((400, i), points),
        closest_point((i, 0), points),
        closest_point((i, 400), points)])
    infinite_areas |= update

possible_points = [p for p in points if p not in infinite_areas]
candidates = Counter()

for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        candidates.update([closest_point((x, y), points)])

best = max(possible_points, key=lambda p: candidates[p])


print('Part 1:', candidates[best])

# instead of doing ALL the points this time we just need to use the inifinite area coords!
coords = [[0] * (max_y - min_y) for i in range(min_x, max_x)]

for p in points:
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if coords[x-min_x][y-min_y] >= 10000:
                continue
            coords[x-min_x][y-min_y] += dist((x, y), p)

reduce(lambda acc, x: acc + 1 if x < 10000 else acc, flatten(coords), 0)

area = len([1 for x in range(min_x, max_x) for y in range(min_y, max_y) if sum([dist(p, (x, y)) for p in points]) < 10000])

print('Part 2:', area)

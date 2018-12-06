from collections import Counter, defaultdict
import itertools
import re


def preprocess(polymer): return [(c, ord(c) % 32) for c in polymer]


def flatten(l): return [i for subl in l for i in subl]


def squish(polymer):
    return filter(
        lambda tup: not(tup[0][1] == tup[1][1] and tup[0][0] != tup[1][0]), polymer)


with open('input/day5.txt') as f:
    polymer = f.read().split('\n')[:-1][0]


def react(poly):
    last_len = len(poly) + 1

    while len(poly) < last_len:
        last_len = len(poly)

        pairs = zip(poly[::2], poly[1::2])
        poly = flatten(squish(pairs))

        pairs = zip(poly[1::2], poly[2::2])
        front = [poly[0]]
        end = [poly[-1]]
        poly = front + flatten(squish(pairs)) + end

    return poly


print('Part 1:', len(react(preprocess(polymer))))

keys = set(map(lambda x: x.lower(), set(polymer)))

p2 = min(len(react(preprocess(polymer.replace(key, '').replace(key.upper(), '')))) for key in keys)

print('Part 2:', p2)

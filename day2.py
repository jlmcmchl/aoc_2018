from collections import Counter
import itertools


def xor(arr): return [pair[0] ^ pair[1] for pair in zip(*arr)]


def ords(arr): return [ord(c) for c in arr]


def chrs(arr): return ''.join([chr(c) for c in arr])


with open('input/day2.txt') as f:
    l = f.read().split('\n')[:-1]

twos = 0
threes = 0

for serial in l:
    ctr = Counter(serial)
    best = ctr.most_common(4)
    if any([i[1] == 2 for i in best]):
        twos += 1
    if any([i[1] == 3 for i in best]):
        threes += 1

print('Part 1:', twos*threes)

serials = map(lambda x: [ord(c) for c in x], l)
correct = ('', '')

for combo in itertools.combinations(serials, 2):
    diffs = set(xor(combo))
    if len(diffs) == 2:
        correct = (chrs(combo[0]), chrs(combo[1]))
        break

print('Part 2:', ''.join(
    [a[0] if a[0] == a[1] else '' for a in zip(*correct)]))

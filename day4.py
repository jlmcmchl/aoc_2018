from collections import Counter, defaultdict
import itertools
import re

line_re = re.compile(r'^\[([\d-]+) ([\d\:]+)\] (.*)$', re.I)
guard_re = re.compile(r'#(\d+)')


def time_to_num(t):
    if t[:2] == '23':
        return -60+int(t[3:])
    return int(t[3:])


with open('input/day4.txt') as f:
    l = f.read().split('\n')[:-1]
l = [line_re.match(line).groups() for line in sorted(l)]

guards = defaultdict(dict)
day = ''
guard = -1
messages = []
for line in l:
    if 'Guard' in line[2]:
        if guard != -1:
            guards[guard][day] = messages
        guard = guard_re.search(line[2]).groups()[0]
        messages = []
    else:
        messages.append(((time_to_num(line[1]), line[2])))
    day = line[0]

sleeps = defaultdict(list)

for guard in guards:
    for day in guards[guard]:
        pairs = zip(range(100), zip(
            guards[guard][day], guards[guard][day][1:]))
        pairs = [p[1] for p in pairs if p[0] % 2 == 0]
        sleeps[guard].extend(pairs)

guard_stat = defaultdict(Counter)

for guard in sleeps:
    for sleep in sleeps[guard]:
        guard_stat[guard].update(range(sleep[0][0], sleep[1][0]))

iterable = [(guard, guard_stat[guard]) for guard in guard_stat]

sleepy_guard = max(iterable, key=lambda x: len(list(x[1].elements())))

print('Part 1:', int(sleepy_guard[0]) * sleepy_guard[1].most_common(1)[0][0])

sleepy_guards = [(it[0], it[1].most_common(1)[0]) for it in iterable]

sleepiest = max(sleepy_guards, key=lambda x: x[1][1])

print('Part 2:', int(sleepiest[0]) * sleepiest[1][0])

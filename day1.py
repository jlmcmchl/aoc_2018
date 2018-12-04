from collections import defaultdict

with open('input/day1.txt') as f:
    l = list(map(int, f.read().split('\n')[:-1]))

print('Part 1:', sum(l))

reached = defaultdict(lambda: False)
reached[0] = True
found = False

loc = 0
while(not found):
    for i in l:
        loc += i
        if reached[loc]:
            found = True
            break
        else:
            reached[loc] = True

print('Part 2:', loc)

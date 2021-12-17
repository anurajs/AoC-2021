from collections import defaultdict
import sys
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

x = data[0].strip().split('..')
y = data[1].strip().split('..')

x = [int(v) for v in x]
y = [int(v) for v in y]

yd_god = float('-inf')

valid_step = defaultdict(lambda: set())

for ivx in range(x[1]+1):
    xd = 0
    vx = ivx
    step = 0
    for step in range(300):
        xd += vx
        if vx > 0:
            vx -= 1
        if xd in range(x[0], x[1] + 1):
            valid_step[step].add(ivx)
        if xd > x[1]:
            break
count = 0
for ivy in range(y[0], max(y[1], abs(y[0]))+1):
    yd = 0
    vy = ivy
    max_yd = float('-inf')
    target_hit = False
    step = 0
    ivxs = set()
    for step in range(300):
        yd += vy
        vy -= 1
        if yd > max_yd:
            max_yd = yd
        if yd in range(y[0], y[1]+1) and step in valid_step:
            target_hit = True
            ivxs |= valid_step[step]
        if yd > y[1] and target_hit:
            break
    if target_hit and max_yd > yd_god:
        yd_god = max_yd
        god_speed = (ivxs, ivy)
    count += len(ivxs)

print('Part 1: ', yd_god, god_speed)
print('Part 2: ', count)

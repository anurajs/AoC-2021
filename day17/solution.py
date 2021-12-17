# from collections import defaultdict
import sys
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

x = data[0].strip().split('..')
y = data[1].strip().split('..')

x = [int(v) for v in x]
y = [int(v) for v in y]

yd_god = float('-inf')

count = 0
god_speed = ''
for ivy in range(-150, 150):
    for ivx in range(200 if ivy < 0 else 20):
        xd = 0
        yd = 0
        vx = ivx
        vy = ivy
        max_yd = float('-inf')
        target_hit = False
        mstep = 0
        for step in range(250 if ivx < 20 else 20):
            xd += vx
            yd += vy
            vy -= 1
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 0
            if xd in range(x[0], x[1]+1) and yd in range(y[0], y[1]+1):
                target_hit = True
                mstep = step
            if yd > max_yd:
                max_yd = yd
        if target_hit:
            count += 1
            if max_yd > yd_god:
                yd_god = max_yd
                god_speed = (ivx, ivy)

print('Part 1: ', yd_god)
print('Part 2: ', count)

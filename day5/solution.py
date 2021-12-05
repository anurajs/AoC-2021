from collections import defaultdict

path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readlines()

points = defaultdict(lambda: 0)
for point in input:
    start, end = point.split(' -> ')
    start = [int(x) for x in start.split(',')]
    end = [int(x) for x in end.split(',')]
    if start[0] == end[0]:
        for i in range(start[1], end[1] + (1 if end[1] > start[1] else -1), (1 if end[1] > start[1] else -1)):
            points[(start[0], i)] += 1
    elif start[1] == end[1]:
        for i in range(start[0], end[0] + (1 if end[0] > start[0] else -1), (1 if end[0] > start[0] else -1)):
            points[(i, start[1])] += 1
    # part 2 below
    else:
        for j, i in zip(range(start[1], end[1] + (1 if end[1] > start[1] else -1), (1 if end[1] > start[1] else -1)), range(start[0], end[0] + (1 if end[0] > start[0] else -1), (1 if end[0] > start[0] else -1))):
            points[i, j] += 1

print(len([x for x in filter(lambda x: x >= 2, points.values())]))

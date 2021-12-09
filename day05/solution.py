from collections import defaultdict

path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readlines()


def gen_range(a, b):
    return range(a, b + (1 if a < b else -1), (1 if a < b else -1))


points = defaultdict(lambda: 0)
for point in input:
    start, end = point.split(' -> ')
    start = [int(x) for x in start.split(',')]
    end = [int(x) for x in end.split(',')]
    if start[0] == end[0]:
        for i in gen_range(start[1], end[1]):
            points[(start[0], i)] += 1
    elif start[1] == end[1]:
        for i in gen_range(start[0], end[0]):
            points[(i, start[1])] += 1
    # part 2 below
    else:
        for j, i in zip(gen_range(start[1], end[1]), gen_range(start[0], end[0])):
            points[i, j] += 1

print(len([x for x in filter(lambda x: x >= 2, points.values())]))

import sys
from collections import defaultdict
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

data = [[int(x) for x in line.strip()] for line in data]


def part1(data):
    start = (0, 0)
    end = (len(data[0])-1, len(data)-1)
    current = start

    distances = defaultdict(lambda: float('inf'))
    previous = dict()
    distances[start] = 0
    available = {(0, 0)}
    visited = set()
    while current != end:
        visited.add(current)
        available.remove(current)
        neighbours = [(current[0] + 1, current[1]), (current[0]-1, current[1]),
                      (current[0], current[1] + 1), (current[0], current[1]-1)]
        for (x, y) in neighbours:
            if not(y == len(data) or x == len(data[y]) or x < 0 or y < 0) and (x, y) not in visited:
                available.add((x, y))
                alt = distances[current] + data[y][x]
                if alt < distances[(x, y)]:
                    distances[(x, y)] = alt
                    previous[(x, y)] = current
        current = min(available, key=lambda x: distances[x])

    path = [end]
    nxt = end
    while nxt in previous:
        path.append(previous[nxt])
        nxt = previous[nxt]
    total = 0
    for (x, y) in path[1:]:
        total += data[y][x]
    return total


def manhattan_distance(current, goal):
    return (abs(goal[0] - current[0]) + abs(goal[1] - current[1]))


def part2(data):
    start = (0, 0)
    end = (len(data[0]) * 5 - 1, len(data) * 5 - 1)
    current = start
    distances = defaultdict(lambda: float('inf'))
    previous = dict()
    distances[start] = 0
    available = {(0, 0)}
    visited = set()
    while current != end:
        visited.add(current)
        available.remove(current)
        neighbours = [(current[0] + 1, current[1]), (current[0]-1, current[1]),
                      (current[0], current[1] + 1), (current[0], current[1]-1)]
        for (x, y) in neighbours:
            if not(y == end[1] + 1 or x == end[0] + 1 or x < 0 or y < 0) and (x, y) not in visited:
                available.add((x, y))
                dist = (data[y % len(data)][x % len(data[0])] +
                        (x//len(data[0])) + (y//len(data))) % 9
                dist = 9 if dist == 0 else dist
                alt = distances[current] + dist
                if alt < distances[(x, y)]:
                    distances[(x, y)] = alt
                    previous[(x, y)] = current
        current = min(
            available, key=lambda x: distances[x] + manhattan_distance(x, end))

    path = [end]
    nxt = end
    while nxt in previous:
        path.append(previous[nxt])
        nxt = previous[nxt]
    total = 0
    for (x, y) in path[:-1]:
        dist = (data[y % len(data)][x % len(
            data[0])] + 1*(x//len(data[0])) + 1*(y//len(data))) % 9
        dist = 9 if dist == 0 else dist
        total += dist

    return total


print('Part 1: ', part1(data))
print('Part 2: ', part2(data))

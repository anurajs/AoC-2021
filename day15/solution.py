import sys
import heapq
from collections import defaultdict
path = sys.argv[1] if len(sys.argv) > 1 else 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

data = [[int(x) for x in line.strip()] for line in data]


def get_dist(data, x, y):
    return (data[y % len(data)][x % len(data[0])] + (x//len(data[0])) + (y//len(data)) - 1) % 9 + 1


def solve(data, end):
    start = (0, 0)
    current = start
    distances = defaultdict(lambda: float('inf'))
    previous = dict()
    distances[start] = 0
    available = []
    visited = set()
    while current != end:
        visited.add(current)
        neighbours = [(current[0] + 1, current[1]), (current[0]-1, current[1]),
                      (current[0], current[1] + 1), (current[0], current[1]-1)]
        for (x, y) in neighbours:
            if not(y == end[1] + 1 or x == end[0] + 1 or x < 0 or y < 0) and (x, y) not in visited:
                alt = distances[current] + get_dist(data, x, y)
                if alt < distances[(x, y)]:
                    distances[(x, y)] = alt
                    previous[(x, y)] = current
                    heapq.heappush(available, (alt, (x, y)))
        _, current = heapq.heappop(available)
        while current in visited:
            _, current = heapq.heappop(available)

    return distances[end]


print('Part 1: ', solve(data, (len(data[0]) - 1, len(data) - 1)))
print('Part 2: ', solve(data, (len(data[0]) * 5 - 1, len(data) * 5 - 1)))

import numpy as np
path = 'puzzle.txt'
with open(path, 'r') as file:
    data = file.readlines()

data = np.array([[int(x) for x in line.strip()] for line in data])


def increase_step(data):
    data += 1


def flash_surrounding(data, i, j):
    neighbours = [(i+1, j+1), (i, j+1), (i+1, j),
                  (i-1, j+1), (i-1, j-1), (i-1, j), (i+1, j-1), (i, j-1)]

    for n in neighbours:
        if not(n[0] < 0 or n[1] < 0 or n[0] == len(data) or n[1] == len(data[i])):
            data[n[0], n[1]] += 1


def solve(data):
    count = 0
    step = 0
    while True:
        step += 1
        increase_step(data)
        flash_set = set()
        while True:
            flashed = False
            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][j] > 9 and (i, j) not in flash_set:
                        flash_surrounding(data, i, j)
                        flash_set.add((i, j))
                        flashed = True
                        if step <= 100:
                            count += 1
            if not flashed:
                break
        data[data > 9] = 0
        if(np.all(data == 0)):
            break
    return count, step


part1, part2 = solve(data)

print('Part 1: ', part1)
print('Part 2: ', part2)

import numpy as np
path = 'puzzle.txt'
with open(path) as file:
    data = file.readlines()

seperate = data.index('\n')
points = [[int(x) for x in line.strip().split(',')]
          for line in data[:seperate]]
folds = [fold.strip()[11:] for fold in data[seperate+1:]]

max_x = max(points, key=lambda a: a[0])[0]
max_y = max(points, key=lambda a: a[1])[1]

grid = np.zeros((max_y+1, max_x+1))

for x, y in points:
    grid[y][x] = 1


def fold_vertical(grid, position):
    new_grid = np.array(grid[:position])
    for index, line in enumerate(grid[position+1:min(len(grid), (position*2+1))]):
        for j in range(len(line)):
            new_grid[position-1 - index][j] += line[j]
    return new_grid


def fold_horizontal(grid, position):
    new_grid = fold_vertical(grid.T, position)
    return new_grid.T


d, a = folds[0].split('=')
a = int(a)
part1 = fold_vertical(grid, a) if d == 'y' else fold_horizontal(grid, a)
part1 = len(part1[part1 > 0])

print('Part 1: ', part1)

for fold in folds:
    d, a = fold.split('=')
    a = int(a)
    grid = fold_vertical(grid, a) if d == 'y' else fold_horizontal(grid, a)

grid[grid > 0] = 1
grid[grid == 0] = 0
grid = grid.astype(str)
grid[grid == '0.0'] = ' '
grid[grid == '1.0'] = '#'
print('Part 2: ')
for line in grid:
    s = ''
    for c in line:
        s += c
    print(s)

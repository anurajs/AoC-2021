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
    for index, line in enumerate(grid[position+1:min(len(grid), position*2)+1]):
        for j in range(len(line)):
            new_grid[position-1 - index][j] += line[j]

    return new_grid


def fold_horizontal(grid, position):
    new_grid = np.array(grid.T[:position])
    for index, line in enumerate(grid.T[position+1:min(len(grid.T), position*2)+1]):
        for j in range(len(line)):
            new_grid[position-1 - index][j] += line[j]
    return new_grid.T


direction, amount = folds[0].split('=')
amount = int(amount)
part1 = fold_vertical(
    grid, amount)if direction == 'y' else fold_horizontal(grid, amount)
part1 = len(part1[part1 > 0])

print('Part 1: ', part1)

for fold in folds:
    direction, amount = fold.split('=')
    amount = int(amount)
    grid = fold_vertical(
        grid, amount)if direction == 'y' else fold_horizontal(grid, amount)

grid[grid > 0] = 1
grid[grid == 0] = 0
grid = grid.astype(int)
print(grid)
np.savetxt('output.csv', grid, '%01d', delimiter=',')

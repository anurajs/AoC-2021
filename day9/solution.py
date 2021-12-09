path = 'puzzle.txt'
with open(path, 'r') as file:
    data = file.readlines()

data = [[int(x) for x in line.strip()] for line in data]


def basin(i, j, data, b_map):
    if i == len(data) or j == len(data[i]) or i < 0 or j < 0 or data[i][j] == 9 or (i, j) in b_map:
        return 0
    if (i, j) not in b_map:
        b_map.add((i, j))
        return 1 + basin(i, j+1, data, b_map) + basin(i, j - 1, data, b_map) + basin(i-1, j, data, b_map) + basin(i+1, j, data, b_map)


total = 0
basins = []
for i in range(len(data)):
    for j in range(len(data[i])):
        current = data[i][j]
        if j == 0 and i == 0:
            if current < data[i+1][j] and current < data[i][j+1]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif i == len(data)-1 and j == len(data[i])-1:
            if current < data[i-1][j] and current < data[i][j-1]:
                total += current
                basins.append(basin(i, j, data, set()))
        elif i == 0 and j == len(data[i])-1:
            if current < data[i+1][j] and current < data[i][j-1]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif i == len(data)-1 and j == 0:
            if current < data[i-1][j] and current < data[i][j+1]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif j == 0:
            if current < data[i][j+1] and current < data[i-1][j] and current < data[i+1][j]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif j == len(data[i])-1:
            if current < data[i][j-1] and current < data[i-1][j] and current < data[i+1][j]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif i == 0:
            if current < data[i+1][j] and current < data[i][j+1] and current < data[i][j-1]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif i == len(data)-1:
            if current < data[i-1][j] and current < data[i][j+1] and current < data[i][j-1]:
                total += current + 1
                basins.append(basin(i, j, data, set()))
        elif current < data[i][j+1] and current < data[i][j-1] and current < data[i+1][j] and current < data[i-1][j]:
            total += current + 1
            basins.append(basin(i, j, data, set()))

basins.sort(reverse=True)

print('Part 1: ', total)
print('Part 2: ', basins[0] * basins[1] * basins[2])

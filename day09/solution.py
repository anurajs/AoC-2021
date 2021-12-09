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
        neighbours = [(1+i, j), (i-1, j), (i, j+1), (i, j-1)]
        lowpoint = True
        for n in neighbours:
            if n[0] < 0 or n[1] < 0 or n[0] == len(data) or n[1] == len(data[j]):
                continue
            if current > data[n[0]][n[1]]:
                lowpoint = False
        if lowpoint:
            total += current + 1
            size = basin(i, j, data, set())
            basins.append(size)


basins.sort(reverse=True)

print('Part 1: ', total)
print('Part 2: ', basins[0] * basins[1] * basins[2])

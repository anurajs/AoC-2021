from collections import defaultdict
path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readline()

fishes = defaultdict(lambda: 0)
for key in [int(x) for x in input.split(',')]:
    fishes[key] += 1

for _ in range(256):
    for i in range(9):
        fishes[i-1] += fishes[i]
        fishes[i] = 0
    fishes[6] += fishes[-1]
    fishes[8] += fishes[-1]
    fishes[-1] = 0


print(sum(fishes.values()))

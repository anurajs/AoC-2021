from statistics import median

path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readline()

input = [int(x) for x in input.split(',')]

med = median(input)
total = 0
for crab in input:
    total += abs(crab - med)

print('Part 1: ', round(total))


def consec_num(x):
    return (x/2 * (1+x))


average = sum(input)//len(input)
total = 0
for crab in input:
    total += consec_num(abs(crab - average))

print('Part 2: ', round(total))

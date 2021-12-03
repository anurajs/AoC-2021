from collections import defaultdict
from numpy.core.fromnumeric import argmax
path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readlines()


def get_count(input):
    binary_counter = defaultdict(lambda: 0)
    for str in input:
        for i, value in enumerate(str):
            binary_counter[i] += 1 if value == '1' else -1
    return binary_counter


input = [x.strip() for x in input]

binary_counter = get_count(input)

gamma = ""
epsilon = ""

for i in range(len(input[0])):
    if binary_counter[i] < 0:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print('Part 1: ', gamma * epsilon)

oxygen = input.copy()
co2 = input.copy()

for i in range(len(input[0])):
    co2_counter = get_count(co2)
    oxygen_counter = get_count(oxygen)

    if oxygen_counter[i] >= 0 and len(oxygen) != 1:
        oxygen = list(filter(lambda x: x[i] == '1', oxygen))
    elif len(oxygen) != 1:
        oxygen = list(filter(lambda x: x[i] == '0', oxygen))

    if co2_counter[i] >= 0 and len(co2) != 1:
        co2 = list(filter(lambda x: x[i] == '0', co2))
    elif len(co2) != 1:
        co2 = list(filter(lambda x: x[i] == '1', co2))

    oxygen = [x for x in oxygen]
    co2 = [x for x in co2]

    if len(oxygen) == 1 and len(co2) == 1:
        break

print('Part 2: ', int(oxygen.pop(), 2) * int(co2.pop(), 2))

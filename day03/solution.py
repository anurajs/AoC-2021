path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readlines()


def get_count_at(input, i):
    total = 0
    for str in input:
        total += 1 if str[i] == '1' else -1
    return total


def get_count(input):
    binary_counter = []
    for i in range(len(input[0])):
        binary_counter.append(get_count_at(input, i))
    return binary_counter


def flip_bits(input):
    return ''.join(['1' if x == '0' else '0' for x in input])


input = [x.strip() for x in input]

binary_counter = get_count(input)

gamma = ""

for i in range(len(input[0])):
    if binary_counter[i] < 0:
        gamma += '0'
    else:
        gamma += '1'

epsilon = int(flip_bits(gamma), 2)
gamma = int(gamma, 2)

print('Part 1: ', gamma * epsilon)

oxygen = input.copy()
co2 = input.copy()

for i in range(len(input[0])):
    co2_counter = get_count_at(co2, i)
    oxygen_counter = get_count_at(oxygen, i)

    if oxygen_counter >= 0 and len(oxygen) != 1:
        oxygen = list(filter(lambda x: x[i] == '1', oxygen))
    elif len(oxygen) != 1:
        oxygen = list(filter(lambda x: x[i] == '0', oxygen))

    if co2_counter >= 0 and len(co2) != 1:
        co2 = list(filter(lambda x: x[i] == '0', co2))
    elif len(co2) != 1:
        co2 = list(filter(lambda x: x[i] == '1', co2))

    if len(oxygen) == 1 and len(co2) == 1:
        break

print('Part 2: ', int(oxygen.pop(), 2) * int(co2.pop(), 2))

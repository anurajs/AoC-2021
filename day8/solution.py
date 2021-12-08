path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readlines()


def part1(input):
    total = 0
    for line in input:
        patterns, outputs = line.split(' | ')
        patterns = patterns.split(' ')
        outputs = outputs.split(' ')
        for output in outputs:
            size = len(output.strip())
            if size == 2 or size == 4 or size == 3 or size == 7:
                total += 1
    return total


def part2(input):
    nums = []
    for line in input:
        options = dict()
        for i in range(8):
            options[i] = list()
        patterns, outputs = line.split(' | ')
        patterns = patterns.split(' ')
        outputs = outputs.split(' ')
        for pattern in patterns:
            pattern = pattern.strip()
            size = len(pattern)
            options[size].append(set(pattern))
        numbers = dict()
        numbers[1] = options[2].pop()
        numbers[4] = options[4].pop()
        numbers[7] = options[3].pop()
        numbers[8] = options[7].pop()
        line0 = numbers[7].difference(numbers[1])
        test = numbers[4].union(line0)
        for index, value in enumerate(options[6]):
            diff = value.difference(test)
            if len(diff) == 1:
                line7 = diff
                numbers[9] = value
                popped = index
                break
        options[6].pop(popped)
        test = numbers[1].union(line0).union(line7)
        for index, value in enumerate(options[5]):
            diff = value.difference(test)
            if len(diff) == 1:
                line3 = diff
                numbers[3] = value
                popped = index
                break
        options[5].pop(popped)
        for index, value in enumerate(options[6]):
            if len(line3.difference(value)) == 1:
                numbers[0] = value
                popped = index
                break
        options[6].pop(popped)
        numbers[6] = options[6].pop()
        line2 = numbers[0].difference(numbers[6])
        for value in options[5]:
            if len(line2.difference(value)) == 0:
                numbers[2] = value
            else:
                numbers[5] = value
        options[5].pop()
        options[5].pop()
        num = ''
        for output in outputs:
            output = set(output.strip())
            for number in numbers:
                if numbers[number] == output:
                    num += str(number)
        nums.append(int(num))
    return sum(nums)


print('Part 1: ', part1(input))
print('Part 2: ', part2(input))

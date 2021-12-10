from statistics import median
path = 'puzzle.txt'
with open(path, 'r') as file:
    data = file.readlines()

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

corresponding = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

completion = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

opening = {'(', '[', '{', '<'}

scores = []
total = 0
for line in data:
    stack = []
    broken = False
    for character in line.strip():
        if character in opening:
            stack.append(character)
        elif character == corresponding[stack[-1]]:
            stack.pop(-1)
        else:
            total += points[character]
            broken = True
            break
    if not broken:
        score = 0
        while len(stack) != 0:
            character = stack.pop()
            score *= 5
            score += completion[corresponding[character]]

        scores.append(score)


print('Part 1: ', total)
print('Part 2: ', median(scores))

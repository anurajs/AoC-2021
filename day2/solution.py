path = 'input.txt'
with open(path, 'r') as file:
    input = file.readlines()

location = {'depth': 0, 'horizontal': 0}
location2 = {'depth': 0, 'horizontal': 0, 'aim': 0}
for line in input:
    command, amount = line.split(' ')
    amount = int(amount)
    if command == 'forward':
        # part 1
        location['horizontal'] += amount
        # part 2
        location2['horizontal'] += amount
        location2['depth'] += location2['aim'] * amount
    elif command == 'up':
        # part 1
        location['depth'] -= amount
        # part 2
        location2['aim'] -= amount
    else:
        # part 1
        location['depth'] += amount
        # part 2
        location2['aim'] += amount

print('Part 1:', location['horizontal']*location['depth'])
print('Part 2:', location2['horizontal']*location2['depth'])

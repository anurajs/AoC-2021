# %%
from functools import reduce
# geting input
with open('puzzle.txt') as file:
    input = file.readlines()
input = [int(line) for line in input]

# %%
# scuffed solution part 1


def func(acc, x):
    if x[0] == 0:
        return acc
    else:
        return acc+1 if input[x[0]-1] < x[1] else acc


reduce(func, enumerate(input), 0)

# %%
# not-suffed solution part 1
total = 0
for index, value in enumerate(input):
    if index != 0:
        total += 1 if value > input[index-1] else 0
total
# %%
# part 2
total = 0
for i in range(2, len(input)-1):
    window1 = sum(input[i-3:i])
    window2 = sum(input[i-2:i+1])
    total += 1 if window2 > window1 else 0
total

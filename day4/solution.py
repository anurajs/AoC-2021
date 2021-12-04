import numpy as np
path = 'puzzle.txt'
with open(path, 'r') as file:
    input = file.readlines()


def part1(boards, numbers):
    line_size = len(boards[0][0])
    called = set(numbers[:line_size-1])

    for number in numbers[line_size-1:]:
        called.add(number)
        for board in boards:
            for column in range(line_size):
                col = board[:, column:column+1].flatten()
                if is_winner(col, called):
                    return score(called, board, number)

            for row in range(line_size):
                check_row = board[row:row+1, :].flatten()
                if is_winner(check_row, called):
                    return score(called, board, number)


def part2(boards, numbers):
    line_size = len(boards[0][0])
    called = set(numbers[:line_size-1])
    winning_boards = set()

    for number in numbers[line_size-1:]:
        called.add(number)
        for index, board in enumerate(boards):
            if(index in winning_boards):
                continue
            for column in range(line_size):
                col = board[:, column:column+1].flatten()
                if is_winner(col, called):
                    winning_boards.add(index)

            for row in range(line_size):
                check_row = board[row:row+1, :].flatten()
                if is_winner(check_row, called):
                    winning_boards.add(index)
            if len(winning_boards) == len(boards):
                return score(called, board, number)


def score(called, board, last):
    total = 0
    for row in board:
        for item in row:
            total += item*(item not in called)
    return total * last


def is_winner(items, called):
    for item in items:
        if item not in called:
            return False
    return True


numbers = [int(x) for x in input[0].split(',')]

boards = []
board = []
for line in input[2:]:
    if len(line.strip()) == 0:
        boards.append(board)
        board = []
        continue
    row = line.strip().split(' ')
    row = filter(lambda x: x != "", row)
    row = [int(x) for x in row]
    board.append(row)
boards.append(board)


print(part1(np.array(boards), numbers))
print(part2(np.array(boards), numbers))

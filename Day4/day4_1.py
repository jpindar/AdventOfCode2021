"""
AdventOfCode Day 4
"""


filename = "AdventOfCode/Day4/input.txt"
# filename = "AdventOfCode/Day4/test_input.txt"
data = []
size = 5
num_of_boards = 3
boards = []


def read_file():
    global data
    data = []
    inputFile = open(filename, "r")
    with inputFile as f:
        for s in f:
            s = s.strip("\n\r")
            if s != "":
                data.append(s)
    f.close()


def read_boards():
    global boards
    for line in range(1, len(data), size):
        board = []
        for i in range(size):
            board.append(data[line + i].split())
        boards.append(board)


def mark_board(board, num):
    for i in range(size):
        for j in range(size):
            if board[i][j] == num:
                board[i][j] = "x"
    return board


def test_board(board):
    for i in range(size):
        count = 0
        for j in range(size):
            if board[i][j] == "x":
                count += 1
        if count == size:
            return True

    for j in range(size):
        count = 0
        for i in range(size):
            if board[i][j] == "x":
                count += 1
        if count == size:
            return True

    return False


def score_board(board, num):
    score = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != "x":
                score += int(board[i][j])
    score = score * int(num)
    return score


def main():
    read_file()
    numbers = data[0].split(",")
    num_of_boards = int((len(data) - 1) / size)
    read_boards()
    bingo = False
    for num in numbers:
        for board in boards:
            board = mark_board(board, num)
            if test_board(board):
                bingo = True
                print(f"result {score_board(board, num)}")
        if bingo:
            break


main()

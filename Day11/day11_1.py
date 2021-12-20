"""
Advent of Code 2021 day 11 part 1
"""

data = []


def read_file(filename):
    global data
    data = []
    inputFile = open(filename, "r")
    with inputFile as f:
        for s in f:
            s = s.strip("\r\n")
            if s != "":
                data.append(s)
    f.close()
    for i in range(len(data)):
        data[i] = list(data[i])
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])


def add_border():
    """
    add a border of -99's to the data to make it easier to work with
    """
    global data
    for i in range(len(data)):
        data[i].insert(0, -999)  # left
        data[i].append(-999)  # right

    border = []
    for i in range(len(data[0])):
        border.append(-999)
    data.insert(0, border)  # top
    data.append(border)  # bottom


def simulate_step(data):
    """ simulate one step  """
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            data[y][x] += 1
    total_flashes = 0
    done = False
    while not done:
        flashes = 0
        for y in range(1, len(data) - 1):
            for x in range(1, len(data[0]) - 1):
                if data[y][x] > 9:
                    flashes += 1
                    data[y][x] = -999  # this one flashed and cannot get more energy this round
                    # by setting the one that flashed to a very negative number instead of zero,
                    # we don't have to check before adding to it in these next statements
                    data[y][x - 1] += 1
                    data[y][x + 1] += 1
                    data[y - 1][x] += 1
                    data[y + 1][x] += 1
                    data[y - 1][x - 1] += 1
                    data[y - 1][x + 1] += 1
                    data[y + 1][x - 1] += 1
                    data[y + 1][x + 1] += 1
        total_flashes += flashes
        if flashes == 0:
            done = True

    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if data[y][x] < 0:
                data[y][x] = 0  # the ones that flashed are now 0
    return [data, total_flashes]


def print_data(data):
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            print(data[y][x], end="")
        print("")
    print()


def main(filename):
    global data
    read_file(filename)
    add_border()
    # print_data(data)

    score = 0
    for i in range(100):
        [data, flashes] = simulate_step(data)
        score += flashes
    return score


if __name__ == "__main__":
    # filename = "AdventOfCode/Day11/test_input_1.txt"
    # print(filename)
    # result = main(filename)
    # print()
    filename = "AdventOfCode/Day11/test_input_2.txt"
    print(filename)
    result = main(filename)
    print(f"result {result}")
    print(f"result should be 1656")
    print()
    # filename = "AdventOfCode/Day11/input.txt"
    # print(filename)
    # result = main(filename)
    # print(f"result {result}")
    # print(f"result should be 1613")

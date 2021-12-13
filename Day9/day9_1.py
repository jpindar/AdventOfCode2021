"""
AdventOfCode 2021 Day 9 part 1

Note that a potentially confusing thing is when you display a list of lists,
the first index is the y coordinate and the second index is the x axis,
which is the opposite of the way we normally think of x,y coordinates.

This can be somewhat resolved by always refering to a point as data[y][x] instead of data[x][y].
"""


filename = "AdventOfCode/Day9/input.txt"
# filename = "AdventOfCode/Day9/test_input.txt"
data = []


def read_file():
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


def is_a_low_point(x, y):
    """
    The definition of a low point is:
    "the locations that are lower than any of its adjacent locations"
    so a point with an adjacent point at the same level does not count as a low point.
    Thus the comparisons are <= rather than just <.
    """
    result = True
    if x == 0:
        if data[y][x + 1] <= data[y][x]:
            result = False
    elif x == len(data[y]) - 1:
        if data[y][x - 1] <= data[y][x]:
            result = False
    else:
        if data[y][x + 1] <= data[y][x]:
            result = False
        if data[y][x - 1] <= data[y][x]:
            result = False

    if y == 0:
        if data[y + 1][x] <= data[y][x]:
            result = False
    elif y == len(data) - 1:
        if data[y - 1][x] <= data[y][x]:
            result = False
    else:
        if data[y + 1][x] <= data[y][x]:
            result = False
        if data[y - 1][x] <= data[y][x]:
            result = False
    return result


def main():
    read_file()
    sum = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_a_low_point(x, y):
                risk_level = 1 + data[y][x]
                sum += risk_level
                # print(f"{x},{y} = {risk_level}")

    print(f"Sum = {sum}")


if __name__ == "__main__":
    main()

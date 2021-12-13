"""
AdventOfCode 2021 Day 9 part 2

Note that a potentially confusing thing is when you display a list of lists,
the first index is the y coordinate and the second index is the x axis,
which is the opposite of the way we normally think of x,y coordinates.

This can be somewhat resolved by always refering to a point as data[y][x] instead of data[x][y].
"""


filename = "AdventOfCode/Day9/input.txt"
# filename = "AdventOfCode/Day9/test_input.txt"
data = []
basins = []


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


def add_border():
    """
    add a border of 9's to the data to make it easier to work with
    """
    global data
    for i in range(len(data)):
        data[i].insert(0, 9)
        data[i].append(9)

    border = []
    for i in range(len(data[0])):
        border.append(9)
    data.insert(0, border)
    data.append(border)


def is_a_low_point(x, y):
    """
    The definition of a low point is:
    "the locations that are lower than any of its adjacent locations"
    so a point with an adjacent point at the same level does not count as a low point.
    Thus the comparisons are <= rather than just <.
    """
    result = True
    if data[y][x + 1] <= data[y][x]:
        result = False
    if data[y][x - 1] <= data[y][x]:
        result = False

    if data[y + 1][x] <= data[y][x]:
        result = False
    if data[y - 1][x] <= data[y][x]:
        result = False
    return result


def add_neighbors(basin):
    global basins
    done = True
    for point in basin:
        x = point[1]
        y = point[0]
        if data[y][x + 1] < 9:
            if not [y, x + 1] in basin:
                basin.append([y, x + 1])
                done = False
        if data[y][x - 1] < 9:
            if not [y, x - 1] in basin:
                basin.append([y, x - 1])
                done = False

        if data[y + 1][x] < 9:
            if not [y + 1, x] in basin:
                basin.append([y + 1, x])
                done = False
        if data[y - 1][x] < 9:
            if not [y - 1, x] in basin:
                basin.append([y - 1, x])
                done = False
    return done


def main():
    read_file()
    add_border()

    # avoid 0 and len(data) because they are the border
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            if is_a_low_point(x, y):
                basins.append([[y, x]])

    for basin in basins:
        add_neighbors(basin)

    sizes = []
    for basin in basins:
        sizes.append(len(basin))
    sizes.sort(reverse=True)
    result = sizes[0] * sizes[1] * sizes[2]
    print(f"product of the sizes of the three largest basins {result}")


if __name__ == "__main__":
    main()

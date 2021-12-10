"""
AdventOfCode Day 5

The confusing thing is that when you display a list of lists, the first index is
the y coordinate and the second index is the x axis, which is the opposite of the way
we normally think of x,y coordinates.

This can be somewhat resolved by always refering to a point on the map with map[y][x]
instead of map[x][y], which we have done here.

in a real project, it might be wise to abstract away the list of lists and use a custom data
structure to represent the map.

"""

filename = "AdventOfCode/Day5/input.txt"
# filename = "AdventOfCode/Day5/test_input.txt"
data = []
map = []


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


def parse_data():
    global data
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        data[i].remove(data[i][1])
        for j in range(2):
            point = data[i][j].split(",")
            data[i][j] = {"x": int(point[0]), "y": int(point[1])}


def plot_data():
    global map
    max_x = 0
    max_y = 0
    for i in range(len(data)):
        for a in range(1):
            if data[i][a]["x"] > max_x:
                max_x = data[i][a]["x"]
            if data[i][a]["y"] > max_y:
                max_y = data[i][a]["y"]

    # Here's where we start needing to be careful about the x versus y indexes
    # of the map. Each row has a constant y coordinate.
    for i in range(max_y + 1):
        map.append([])
        for j in range(max_x + 1):
            map[i].append(0)

    for i in range(len(data)):
        x1 = data[i][0]["x"]
        x2 = data[i][1]["x"]
        y1 = data[i][0]["y"]
        y2 = data[i][1]["y"]
        if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for y in range(min_y, max_y + 1):
                map[y][x1] += 1  # y index comes first
        if y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for x in range(min_x, max_x + 1):
                map[y1][x] += 1  # y index comes first


def find_result():
    result = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            # print(map[y][x], end="")  # y index comes first
            if map[y][x] > 1:
                result += 1
        # print()
    print()
    print(result)


def main():
    read_file()
    parse_data()
    plot_data()
    find_result()


main()

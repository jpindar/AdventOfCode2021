"""
AdventOfCode Day 8
"""


filename = "AdventOfCode/Day8/input.txt"
# filename = "AdventOfCode/Day8/test_input2.txt"
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


def parse_input():
    global data
    for i in range(len(data)):
        data[i] = data[i].split("|")
        for j in range(2):
            data[i][j] = data[i][j].strip()
            data[i][j] = data[i][j].split(" ")


if __name__ == "__main__":
    read_file()
    parse_input()
    count = 0
    for i in range(len(data)):
        for j in data[i][1]:
            if len(j) in [2, 4, 3, 7]:
                count += 1

    print(f"digits 1, 4, 7, or 8 appear {count} times ")

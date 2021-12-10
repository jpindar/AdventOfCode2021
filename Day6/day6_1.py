"""
AdventOfCode Day 6
"""

filename = "AdventOfCode/Day6/input.txt"
# filename = "AdventOfCode/Day6/test_input.txt"
# number_of_days = 18
number_of_days = 80
# number_of_days = 256
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


def main():
    global data
    read_file()
    data = data[0].split(",")
    max_data = 8
    max_adult_data = 6
    for i in range(len(data)):
        data[i] = int(data[i])

    for day in range(number_of_days):
        for fish in range(len(data)):
            data[fish] -= 1
            if data[fish] < 0:
                data[fish] = max_adult_data
                data.append(max_data)
    print(f"After {number_of_days} days: {len(data)} fish")


main()


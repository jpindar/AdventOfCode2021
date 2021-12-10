"""
AdventOfCode Day 3
"""

filename = "AdventOfCode/Day3/input.txt"
# filename = "AdventOfCode/Day3/test_input.txt"

data = []
mcb = 0
lcb = 0


def read_file():
    inputFile = open(filename, "r")
    with inputFile as f:
        for s in f:
            s = s.strip("\n\r")
            data.append(s)


def find_bits(bitPos):
    global mcb
    global lcb
    zeros = 0
    ones = 0
    for i in range(len(data)):
        if data[i] is not None:
            if data[i][bitPos] == "0":
                zeros += 1
            else:
                ones += 1
    if ones > zeros:
        lcb = 0
        mcb = 1
    elif ones < zeros:
        lcb = 1
        mcb = 0
    else:
        lcb = 0
        mcb = 0


def main():
    read_file()
    bits = len(data[0])

    gamma = 0
    epsilon = 0
    for j in range(bits):
        find_bits(j)
        gamma = (gamma * 2) + mcb
        epsilon = (epsilon * 2) + lcb
    print(f"gamma {gamma}")
    print(f"epsilon {epsilon}")
    print(f"result {gamma * epsilon}")


main()

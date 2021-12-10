"""
AdventOfCode 2021 Day 1 part 1
"""

filename = "AdventOfCode/Day1/input.txt"
# filename = "AdventOfCode/Day1/test_input.txt"
data = []

def read_file():
    inputFile = open(filename, 'r')
    with inputFile as f:
        for s in f:
            n = int(s.strip('\n\r'))
            data.append(n)


def main():
    read_file()
    count = 0
    for i in range(1, len(data)):  # skip the 0th element
        if data[i] > data[i-1]:
            count+=1
    print(f"{count} increases")


main()



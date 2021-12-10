"""
AdventOfCode 2021 Day 1 part 2
"""

filename = "AdventOfCode/Day1/input.txt"
# filename = "AdventOfCode/Day1/test_input.txt"
data = []
window = 3

def read_file():
    inputFile = open(filename, 'r')
    with inputFile as f:
        for s in f:
            n = int(s.strip('\n\r'))
            data.append(n)


def main():
    read_file()
    count = 0
    for i in range(window, len(data)):  # skip the first elements
        a = 0
        b = 0
        for j in range(window):
            a += data[(i-j)-1]
            b += data[i-j]
        if b > a:
            count+=1
    print(f"{count} increases")


main()



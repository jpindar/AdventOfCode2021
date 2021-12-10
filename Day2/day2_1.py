"""
AdventOfCode 2021 Day 2
"""

filename = "AdventOfCode/Day2/input.txt"
# filename = "AdventOfCode/Day2/test_data.txt"
data = []

def read_file():
    inputFile = open(filename, 'r')
    with inputFile as f:
        for s in f:
            s = s.strip('\n\r')
            data.append(s)


def main():
    x = 0
    y = 0
    read_file()
    for i in range(len(data)):
       d = int(data[i].split(" ")[1])
       if "up" in data[i]:
           y -= d
       elif "down" in data[i]:
            y += d
       elif "forward" in data[i]:
            x += d
    print(f"horizontal position {x}, depth {y}, result {x*y}")


main()



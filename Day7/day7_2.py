"""
AdventOfCode Day 7
"""

filename = "AdventOfCode/Day7/input.txt"
# filename = "AdventOfCode/Day7/test_input.txt"
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


def find_fuel_needed(j, target):
    distance = abs(target - j)
    f = int(distance * (1 + distance) / 2)
    return f


def main():
    global data
    read_file()
    data = data[0].split(",")
    for i in range(len(data)):
        data[i] = int(data[i])
    min_pos = min(data)
    max_pos = max(data)

    buckets = {}
    for i in range(len(data)):
        if data[i] in buckets:  # if key exists
            buckets[data[i]] += 1
        else:
            buckets[data[i]] = 1

    fuel = {}
    for target in range(min_pos, max_pos + 1):
        fuel[target] = 0
        for j in buckets:
            fuel_needed = find_fuel_needed(j, target)
            fuel[target] += fuel_needed * buckets[j]

    min_fuel = min(fuel.values())
    best_target = 0
    for k in fuel:
        if fuel[k] == min_fuel:
            best_target = k

    print(f"minimum fuel {min_fuel} at position {best_target}")


if __name__ == "__main__":
    main()

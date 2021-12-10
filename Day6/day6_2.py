"""
AdventOfCode Day 6
"""

filename = "AdventOfCode/Day6/input.txt"
# filename = "AdventOfCode/Day6/test_input.txt"
# number_of_days = 18
# number_of_days = 80
number_of_days = 256
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
    bucket = []
    max_data = 8
    max_adult_data = 6
    for i in range(max_data + 1):
        bucket.append(0)

    for i in range(len(data)):
        data[i] = int(data[i])
        bucket[data[i]] += 1

    for day in range(number_of_days):
        for i in range(max_data + 1):
            if i == 0:
                temp = bucket[i]
                bucket[i] = bucket[i + 1]
            if i >= 0 and i < max_data:
                bucket[i] = bucket[i + 1]

        bucket[max_adult_data] += temp
        bucket[max_data] = temp

        count = 0
        for i in range(max_data + 1):
            count += bucket[i]

    print(f"After {number_of_days} days: {count} fish")


main()


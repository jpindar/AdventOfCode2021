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


def meetsOGRCriteria(n, j):
    if n is None:
        return False
    if mcb == 0 and lcb == 0:
        if n[j] == "1":
            return True
        else:
            return False
    elif n[j] == str(mcb):
        return True
    else:
        return False


def meetsCSRCriteria(n, j):
    if n is None:
        return False
    if mcb == 0 and lcb == 0:
        if n[j] == "0":
            return True
        else:
            return False
    if n[j] == str(lcb):
        return True
    else:
        return False


def bin2dec(b):
    dec = 0
    for i in range(len(b)):
        dec *= 2
        if b[i] == "1":
            dec += 1
    return dec


def findRating(meetsCriteria):
    global data
    data = []
    read_file()
    bits = len(data[0])
    n = len(data)
    bitPos = 0
    last_good_value = ""
    while bitPos <= (bits - 1):
        find_bits(bitPos)
        count_of_good_values = 0
        for i in range(n):
            if meetsCriteria(data[i], bitPos):
                count_of_good_values += 1
                last_good_value = str(data[i])
            else:
                data[i] = None
        if count_of_good_values <= 1:
            break
        bitPos += 1
    rating = bin2dec(last_good_value)
    return rating


def main():
    read_file()
    bits = len(data[0])

    # find gamma and epsilon
    gamma = 0
    epsilon = 0
    for j in range(bits):
        find_bits(j)
        gamma = (gamma * 2) + mcb
        epsilon = (epsilon * 2) + lcb
    print(f"gamma {gamma}")
    print(f"epsilon {epsilon}")
    print(f"result {gamma * epsilon}")

    ogr = findRating(meetsOGRCriteria)
    print(f"ogr {ogr}")
    csr = findRating(meetsCSRCriteria)
    print(f"csr {csr}")
    print(f"result {ogr * csr}")


main()

"""
AdventOfCode Day 8
"""
import logging

logger = logging.getLogger()
logging.basicConfig(filename="AdventOfCode/Day8/day8.log", filemode="w",
                    format="%(levelname)-8s:%(asctime)s %(name)s: %(message)s")
logger.setLevel(logging.INFO)


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
            for k in range(len(data[i][j])):
                data[i][j][k] = ''.join(sorted(data[i][j][k]))


def populate_codes(more_codes):
    codes = []
    for n in range(0, 8):
        codes.append([])
    for j in more_codes:
        codes[len(j)].append(j)
    return codes


def includes(j, code):
    for letter in code:
        if not letter in j:
            return False
    return True


def includes_one_of(j, codes):
    for i in codes:
        if includes(j, i):
            return [True, i]
    return [False, ""]


def populate_dict(codes):
    d = {}
    d[codes[2][0]] = 1
    d[codes[3][0]] = 7
    d[codes[4][0]] = 4
    d[codes[7][0]] = 8
    # of the 5 letter codes, the one that includes the 3 letter code -> 3
    # because 3 includes the same segments as 7
    for j in codes[5]:
        if includes(j, codes[3][0]):  # only one 3 letter code
            d[j] = 3
            five_letter_code = j
            codes[5].remove(j)
            break
    # of the 6 letter codes, the one that includes the above 5 letter code -> 9
    # because 9 includes the same segments as 3
    for j in codes[6]:
        if includes(j, five_letter_code):
            d[j] = 9
            codes[6].remove(j)
            break
    # of the other 6 letter codes, the one that includes a 5 letter code -> 6
    # because 6 includes the same segments as 5
    for j in codes[6]:
        result = includes_one_of(j, codes[5])
        if result[0]:
            d[j] = 6
            codes[6].remove(j)
            d[result[1]] = 5
            codes[5].remove(result[1])
            break
    # the only 5 letter code left is 2
    d[codes[5][0]] = 2
    # the only 6 letter code left is 0
    d[codes[6][0]] = 0
    return d


if __name__ == "__main__":
    read_file()
    parse_input()
    count = 0
    for i in range(len(data)):
        codes = populate_codes(data[i][0])
        dic = populate_dict(codes)
        value = ""
        for j in data[i][1]:
            value += str(dic[j])
        print(value)
        count += int(value)

    print(f"total count {count}")

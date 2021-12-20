"""
Advent of Code 2021 day 10 part 1
"""
import re
import sys
filename = "AdventOfCode/Day10/input.txt"
# filename = "AdventOfCode/Day10/test_input.txt"
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


def simplify(s):
    """ Remove pairs """
    same = False
    while not same:
        saved = s
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('<>', '')
        s = s.replace('{}', '')
        if saved == s:
            same = True
    return s


def is_incomplete(s):
    return (len(s) > 0)


def is_corrupt(line):
    """ Check if line is corrupt """
    bad_pairs = ['(]', '(}', '(>', '[)', '[}', '[>', '{)', '{]', '{>', '<)', '<]', '<}']
    for pair in bad_pairs:
        if pair in line:
            if pair[1] == ')':
                score = 3
            elif pair[1] == ']':
                score = 57
            elif pair[1] == '}':
                score = 1197
            elif pair[1] == '>':
                score = 25137
            else:
                score = 0
            return [True, score]
    return [False, 0]


def main():
    read_file()
    n = 0
    total_score = 0
    for line in data:
        n += 1
        s = simplify(line)
        # print(f"{n}        {line}  {s}")
        # if is_incomplete(s):
        #     print("incomplete")
        # else:
        #     print("complete")
        [corrupt, score] = is_corrupt(s)
        if corrupt:
            print(f"corrupt score {score}")
            total_score += score
        else:
            # print("not corrupt")
            pass
    print(f"total score {total_score}")


if __name__ == "__main__":
    main()

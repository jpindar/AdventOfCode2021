"""
Advent of Code 2021 day 10 part 1
"""

data = []


def read_file(filename):
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
    """ A complete line will have been simplified to nothing """
    return (len(s) > 0)


def is_corrupt(line):
    """ a line is corrupt if it contains a pair of characters that don't match """
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


def find_score(line):
    s = simplify(line)
    [corrupt, score] = is_corrupt(s)
    # print(f"{line}        {s}        {corrupt}        {score}")
    return [corrupt, score]


def main(filename):
    read_file(filename)
    total_score = 0
    for line in data:
        [corrupt, score] = find_score(line)
        if corrupt:
            total_score += score
    return total_score


if __name__ == "__main__":
    filename = "AdventOfCode/Day10/test_input.txt"
    print(filename)
    total_score = main(filename)
    print(f"total score {total_score}")
    print(f"total score should be 26397")
    print()
    filename = "AdventOfCode/Day10/input.txt"
    print(filename)
    total_score = main(filename)
    print(f"total score {total_score}")
    print(f"total score should be 462693")

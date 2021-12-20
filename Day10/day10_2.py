"""
Advent of Code 2021 day 10 part 2
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


def is_corrupt(line):
    """ a line is corrupt if it contains a pair of characters that don't match """
    s = simplify(line)
    bad_pairs = ['(]', '(}', '(>', '[)', '[}', '[>', '{)', '{]', '{>', '<)', '<]', '<}']
    for pair in bad_pairs:
        if pair in s:
            return True
    return False


def complete(s):
    """ to complete a simplified string, reverse it and substitute opening characters with closing ones """
    s = s[::-1]
    s = s.replace('(', ')')
    s = s.replace('[', ']')
    s = s.replace('{', '}')
    s = s.replace('<', '>')
    return s


def find_score(line):
    """ find the score of a line """
    s = complete(simplify(line))
    score = 0
    for c in s:
        score *= 5
        if c == ')':
            score += 1
        elif c == ']':
            score += 2
        elif c == '}':
            score += 3
        elif c == '>':
            score += 4
    return score


def main(filename):
    read_file(filename)
    scores = []
    for line in data:
        if not is_corrupt(line):
            score = find_score(line)
            # print(f"score {score}")
            scores.append(score)
    scores.sort()
    middle_score = scores[(len(scores) - 1) // 2]
    return middle_score


if __name__ == "__main__":
    filename = "AdventOfCode/Day10/test_input.txt"
    print(filename)
    score = main(filename)
    print(f"final score {score}")
    print(f"score should be 288957")
    print()
    filename = "AdventOfCode/Day10/input.txt"
    print(filename)
    score = main(filename)
    print(f"final score {score}")
    print(f"total score should be 3094671161")

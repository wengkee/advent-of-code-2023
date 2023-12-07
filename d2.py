from data_file import DataFile
import re

CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_game(line):
    return int(re.search(r'Game (\d+):.*', line).group(1))


def check_color(line, color):
    ls = [m.start() for m in re.finditer(color, line)]
    # print(ls)
    possible = True
    for idx in ls:

        if line[idx-3].isdigit():
            num = int(line[idx - 3: idx -1])
            # print(f"num: {num}")
            if num > CUBES[color]:
                possible = False
        elif int(line[idx-2]) > CUBES[color]:
            possible = False

    # print(f"{color}, {possible}")
    return possible

def get_result_part_1(filename):
    data_file = DataFile(filename)

    total = 0
    for line in data_file.lines:
        game = get_game(line)
        if check_color(line, "blue") and check_color(line, "red") and check_color(line, "green"):
            print(f"game: {game}")
            total += game

        print(total)


get_result_part_1("data/d2_p1_test.txt")
get_result_part_1("data/d2_p1.txt")
# get_result_part_2("data/d2_p2.txt")

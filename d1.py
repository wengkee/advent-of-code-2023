from data_file import DataFile
import re


def get_first_and_last_num(line):
    return int(re.search(r'\d{1}', line).group() + re.search(r'(\d{1})(?!.*\d)', line).group())

def get_result_part_1(filename):
    data_file = DataFile(filename)
    total = 0
    for line in data_file.lines:
        number = get_first_and_last_num(line)
        total += number

    print(f"total: {total}")


def get_result_part_2(filename):
    # this is to workaround overlapping number words
    # e.g. oneight is treated as 18
    NUM = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    data_file = DataFile(filename)
    total = 0

    a = 0
    for line in data_file.lines:

        for b in range(len(line)+1):
            tmp = line[:b]

            for num in NUM.keys():
                if num in tmp:
                    tmp = re.sub(num, NUM[num], tmp)
                    line = tmp + line[b:]

        number = get_first_and_last_num(line)
        total += number

    print(f"total: {total}")


# get_result_part_1("data/d1_p1_test.txt")
get_result_part_1("data/d1_p1.txt")
# get_result_part_2("data/d1_p2_test.txt")
get_result_part_2("data/d1_p2.txt")

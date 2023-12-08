from data_file import DataFile
import re

gear_dic = {}


def is_part_num(lines, line_num, start, end):
    for x in range(start - 1, end + 2):

        for y in range(line_num - 1, line_num + 2):
            if 0 <= x <= len(lines[0]) - 1 and 0 <= y <= len(lines) - 1:
                # print(f"xy = [{x}][{y}]")
                v = lines[y][x]
                if v.isdigit():
                    continue
                if v != "." and not v.isdigit():
                    # print(f"{v}, True")
                    return True

    return False


def may_be_gear(lines, line_num, start, end):
    xy = None
    for x in range(start - 1, end + 2):
        for y in range(line_num - 1, line_num + 2):
            if 0 <= x <= len(lines[0]) - 1 and 0 <= y <= len(lines) - 1:
                v = lines[y][x]
                if v == "*":
                    k = str(x) + "," + str(y)
                    if k not in gear_dic:
                        gear_dic[k] = []
                    xy = k
    return xy


def get_result_part_1(filename):
    data_file = DataFile(filename)
    lines = data_file.lines

    total = 0
    start, end = None, None

    for l in range(len(lines)):

        line = lines[l]

        for idx in range(len(line)):

            if line[idx].isdigit():
                if start is None:
                    start = idx
                else:
                    end = idx
            else:
                if start is not None:
                    end = start

            if start is not None and end is not None:
                # print(f"end: {end}, len(line): {len(line)}")
                end_of_num = False

                # check if it is end of line
                if end == len(line) - 1:
                    end_of_num = True
                else:
                    # if it's not EOL
                    # check if next char is a digit
                    if not line[end + 1].isdigit():
                        end_of_num = True

                if end_of_num:
                    num = line[start:end + 1]

                    if is_part_num(lines, l, start, end):
                        total += int(num)

                        k = may_be_gear(lines, l, start, end)
                        if k is not None:
                            ls = gear_dic[k]
                            ls.append(int(num))
                            gear_dic[k] = ls

                    # print(f"result = num: {num}, {start}, {end}, {l}\n")

                    start, end = None, None

    print(f"Result 1: {total}")
    # print(gear_dic)

    gear_total = 0
    for k in gear_dic:
        if len(gear_dic[k]) > 1:
            gear_ratio = 0
            for part in gear_dic[k]:
                if gear_ratio == 0:
                    gear_ratio = part
                else:
                    gear_ratio *= part
            gear_total += gear_ratio
    print(f"Result 2: {gear_total}")
    gear_dic.clear()


get_result_part_1("data/d3_p1_test.txt")
get_result_part_1("data/d3_p1.txt")

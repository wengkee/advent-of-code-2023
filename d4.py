from data_file import DataFile


def get_winning_points(filename):
    data_file = DataFile(filename)

    total = 0
    for line in data_file.lines:
        parts = line.split()

        winning_num = []
        start_check_num = False
        point = 0
        for part in parts:

            if start_check_num and part in winning_num:
                if point == 0:
                    point = 1
                else:
                    point *= 2
            else:
                if part == "|":
                    start_check_num = True
                    continue
                elif part != "Card" and not part.endswith(":"):
                    winning_num.append(part)

        total += point

    print(total)


def get_num_of_scratch_cards(filename):
    data_file = DataFile(filename)

    card_dic = {}
    for l_num in range(len(data_file.lines)):
        line = data_file.lines[l_num]
        parts = line.split()

        winning_num = []
        start_check_num = False
        point = 0
        card_num = 0
        for part in parts:

            if start_check_num and part in winning_num:
                point += 1
            else:
                if part == "|":
                    start_check_num = True
                    continue
                elif part != "Card" and not part.endswith(":"):
                    winning_num.append(part)
                elif part.endswith(":"):
                    card_num = part.replace(":", "")
                    update_dic(card_dic, card_num, 1)
                    # print(card_num)

        # print(f"card_num: {card_num}, point: {point}")
        for p in range(point):
            k = str(l_num + p + 2)
            for q in range(card_dic[card_num]):
                update_dic(card_dic, k, 1)

    total = 0
    for num in card_dic:
        total += card_dic[num]
    print(total)


def update_dic(dic, k, step):
    if k in dic:
        dic[k] += step
    else:
        dic[k] = step


get_winning_points("data/d4_p1_test.txt")
get_winning_points("data/d4_p1.txt")
get_num_of_scratch_cards("data/d4_p1_test.txt")
get_num_of_scratch_cards("data/d4_p1.txt")

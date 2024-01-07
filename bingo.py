from random import randint
D_SEED = 15
D_MIN = 1
D_MAX = 15


def generate_bingo_card():
    b_list = ['b', 'i', 'n', 'g', 'o']
    b_card = {}


    for letter in b_list:

        exit = False
        counter = 0
        tmp_list = []
        multipler = b_list.index(letter)

        while not exit:
            b_number = randint(D_MIN+(D_SEED * multipler), D_MAX+(D_SEED*multipler))
            if b_number not in tmp_list:
                tmp_list.append(b_number)
                counter += 1
                if counter == 5:
                    exit = True

        b_card[letter] = tmp_list

    return b_card

def print_bingo_card(b_card: dict):
    last_key = list((b_card.keys()))[-1]
    for key in b_card:
        if key != last_key:
            print(f'\t{key}\t', end='')
        else:
            print(f'\t{key}\t')

    for i in range(0, 5):
        for key in b_card:
            if key != last_key:
                print(f'\t{b_card[key][i]}\t', end='')
            else:
                print(f'\t{b_card[key][i]}\t')


print_bingo_card(generate_bingo_card())
from pprint import pprint

from netaddr import P

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day4/day4-input.txt'

with open(file, "r") as f:
    games = f.read().splitlines()

def str_to_list(ls):
    num_list = []
    num_str = ''

    for c,char in enumerate(ls):
        if char.isdigit():
            num_str = num_str + char
            #ensure the last item is added to list
            if c+1 == len(ls):
                num_list.append(num_str.replace(" ", ""))
        elif char.isdigit() == False:
            num_list.append(num_str.replace(" ", ""))
            num_str = ' '
    return num_list

ls_card_wins = []
for card_num, card in enumerate(games):
    win_nums_str = card.split(":")[1].split("|")[0].strip()
    elf_nums_str = card.split(":")[1].split("|")[1].strip()

    win_nums_int = str_to_list(win_nums_str)
    elf_nums_int = str_to_list(elf_nums_str)

    temp_ls= []
    for win_num in win_nums_int:
        for el_num in elf_nums_int:
            if win_num == el_num and win_num != "":
                temp_ls.append(win_num)
    ls_card_wins.append(temp_ls)

#pprint(ls_card_wins)

total = 0   
for i in ls_card_wins:
    double = 1
    #print(len(i))
    if len(i) > 0:
        for j in range(len(i)-1):
            double *= 2
        total += double
print(total)

#Part 2 (NOT CORRECT)

#create list with each index contains the number of wins per card
p2_list = []
for i in ls_card_wins:
    p2_list.append(len(i))

tmp_ls = []
for i in range(len(p2_list)):
     tmp_ls.insert(i, 1)

# pprint(tmp_ls)
# pprint(p2_list)

for counter, value in enumerate(p2_list, start = 1):
    for j in range(value):
        tmp_ls[counter]+=2
        counter+=1
    # pprint(tmp_ls)
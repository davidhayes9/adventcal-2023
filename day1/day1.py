from audioop import reverse
from pprint import pprint
import copy

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day1/day1-input.txt'

with open(file, "r") as f:
    lines = f.read().splitlines()

def get_total(*args):

    if len(args) == 2:
        lines = args[0]
        reverse_lines = args[1]
    else:
        lines = args[0]
        reverse_lines = args[0]

    list_nums= []
    list_reverse_nums =[]

    for i in range(len(lines)):
        for j in lines[i]:
            if j.isdigit():
                list_nums.insert(i,j)
                break
        for j in list(reversed(reverse_lines[i])):
            if j.isdigit():
                list_reverse_nums.insert(i,j)
                break

    total = 0
    for f, b in zip(list_nums, list_reverse_nums):
        num = f + b
        total += int(num)
    return total

print(get_total(lines))

#Part 2
valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

copy_lines = copy.deepcopy(lines)
copy_lines_rev = copy.deepcopy(lines)

reverse_flag = 0

def word_to_digit(copy_lines, reverse_flag):
    # replace words with digits 
    for i in range(len(copy_lines)):
        flag = 0
        for ii in range(len(copy_lines[i])+1):
            for j in range(len(valid_digits)):
                if reverse_flag == 0:
                    if valid_digits[j] in copy_lines[i][:ii] and flag == 0:
                        flag = 1
                        copy_lines[i] = copy_lines[i].replace(valid_digits[j], str(j+1))
                if reverse_flag == 1:
                    if ii != 0:
                        if valid_digits[j] in copy_lines[i][-ii:] and flag == 0:
                            flag = 1
                            copy_lines[i] = copy_lines[i].replace(valid_digits[j], str(j+1))

word_to_digit(copy_lines, 0)
word_to_digit(copy_lines_rev, 1)
print(get_total(copy_lines, copy_lines_rev))
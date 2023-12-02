from pprint import pprint
import copy

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day1/day1-input.txt'

with open(file, "r") as f:
    lines = f.read().splitlines()


def get_total(lines):

    list_nums= []
    list_reverse_nums =[]

    for i in range(len(lines)):
        for j in lines[i]:
            if j.isdigit():
                list_nums.insert(i,j)
                break
        for j in list(reversed(lines[i])):
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

# replace words with digits 
for i in range(len(copy_lines)):
    string = copy_lines[i]
    for ii in range(len(copy_lines[i])+1):
        #print(lines[i][:ii])
        for j in range(len(valid_digits)):
            if valid_digits[j] in copy_lines[i][:ii]:
                #print(valid_digits[j])
                copy_lines[i] = copy_lines[i].replace(valid_digits[j], str(j+1)) 

#pprint(copy_lines)
print(get_total(copy_lines))
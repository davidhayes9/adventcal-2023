from pprint import pprint
from re import S

from netaddr import P

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day8/day8-input.txt'

with open(file, "r") as f:
    lines = list(filter(None, f.read().splitlines()))

instructions = lines[0]

map_dict = {}

for line in lines[1:]:
    temp_ls = []
    node = line.split("=")[0].strip()
    temp_ls = [(line.split("=")[1].split(",")[0].strip().replace("(", "")), (line.split("=")[1].split(",")[1].strip().replace(")", "")) ]
    map_dict[node] = temp_ls

zzz = 0
pos = 0
node = "AAA"
steps = 0

while(True):
    char = instructions[pos]
    if char == 'L':
        node = map_dict[node][0]
        steps += 1

    if char == 'R':
        node = map_dict[node][1]
        steps += 1

    if pos == len(lines[0])-1:
        pos = 0
    else:
        pos +=1
    
    if node == "ZZZ":
        zzz = 1
        break

print(steps)      


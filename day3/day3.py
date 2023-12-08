from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day3/day3-input.txt'

with open(file, "r") as f:
    lines = f.read().splitlines()

w = len(lines[0])
h = len(lines)

coord = []

for x, v in enumerate(lines):
    for y, j in enumerate(lines[x]):
        if j not in "0123456789.":
            #print(j, "at ", x, y)
            coord.append(tuple((x, y)))

pprint(coord)

for x,y in coord:
    print(lines[x][y])
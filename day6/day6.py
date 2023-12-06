from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day6/day6-input.txt'

with open(file, "r") as f:
    race = f.read().splitlines()

ls_times = race[0].split(":")[1].strip()
ls_dist = race[1].split(":")[1].strip()

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
    
    return list(filter(None, num_list))

def win_race(t, d):
    wins = 0
    for i in range(t+1):
        if part2 == 0:
            speed = (i * 1)
            distance = (speed * (t - i))
            if distance > d:
                wins += 1

        if part2 == 1:
            if i >= 14:
                speed = (i * 1)
                distance = (speed * (t - i))
                if distance > d:
                    wins += 1
    return wins

def get_wins(time, dist):
    mult_wins = 1

    for t, d in zip(time, dist):
        num_wins = win_race(int(t), int(d))

        if num_wins != 0:
            mult_wins *= num_wins

    return print(mult_wins)

time = str_to_list(ls_times)
dist = str_to_list(ls_dist)

part2 = 0
get_wins(time, dist)

#part 2
race_time = ls_times.replace( " ", "")
race_distance = ls_dist.replace( " ", "")

part2 = 1
print(win_race(int(race_time), int(race_distance)))

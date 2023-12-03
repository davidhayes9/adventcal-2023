from pprint import pprint

file = '/Users/dhayes/Documents/scripts/adventCal-2023/day2/day2-input.txt'

with open(file, "r") as f:
    lines = f.read().splitlines()

colour_scores = {"red":12, "green":13, "blue":14}

impossible_games = set()

sum_ids = 0
sum_impossible_ids = 0

#part 2
sum_powers = 0

for line in lines:
    id = line.split(':')[0].replace("Game ", "")
    games = line.split(":")[1].split(";")
    
    sum_ids += int(id)

    # dict for part2
    highest_cube_scores = {"red":0, "green":0, "blue":0}

    for key in colour_scores.keys():
        for i in range(len(games)):
            if key in games[i]:
                #print(key)
                color_index = games[i].index(key)
                score = int(games[i][color_index-3:color_index].replace(" ", ""))
                if score > colour_scores[key]:
                    #print(f"In game {id} we had an impossible score of {score} for colour {key}")
                    impossible_games.add(int(id))
                
                #Part 2
                if score > highest_cube_scores[key]:
                    highest_cube_scores[key] = score
                    #print(score)
    
    sum_powers += (highest_cube_scores["red"] * highest_cube_scores["green"] * highest_cube_scores["blue"])
    
for x in impossible_games:
  sum_impossible_ids += x

print(sum_ids-sum_impossible_ids)

#part 2
print(sum_powers)
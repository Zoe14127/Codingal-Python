team_1 = 58
team_2 = 120
team_3 = 98
team_4 = 105
team_5 = 75
 
total = team_1 + team_2 + team_3 + team_4 + team_5
avg = total / 5
print("Points: ", total)
print("Average per team: ", avg)
 
stars_per_point = 2
reward = total * stars_per_point
print("Reward stars: ", reward)
 
boxes = reward // 25
leftover = reward % 25
print("Boxes packed: ", boxes)
print("Stars leftover: ", leftover)
 
last_week = 500
print("Better than last week?: ", total > last_week)
print("Same as last week?: ", total == last_week)
print("At least as good?: ", total >= last_week)
 
total += 30
print("After bonus points: ", total)
total -= 15
print("After missed tasks: ", total)
 
reward = total * stars_per_point
boxes = reward // 25
print("Total boxes packed: ", boxes)
import random
l = ["Barca","Real","Valencia","Sevilla","Atl","Deportivo"]
home_fixtures = []
away_fixtures = []
rounds = []
'''
for x in range(len(l)):
    home_fixtures.append([])
    away_fixtures.append([])

temp = 0
for x in l:
    for y in l:
        if x != y:
            home_fixtures[temp].append(x + "-" + y)
            away_fixtures[temp].append(y + "-" + x)
    temp += 1
'''

team1 = None
team2 = None
while(len(rounds) != len(l)/2):
    team1 = random.randint(0,len(l)-1)
    team2 = random.randint(0,len(l)-1)
    if team1 == team2:
        continue
    if [for x in kutya]
        continue
    rounds.append([l[team1],l[team2]])

print(rounds)

import getch, random, os, time, football_league_table


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def match():
    home = []
    home_goals = 0
    away = []
    away_goals = 0
    picked_home = input("Pick a home team: ")
    picked_away = input("Pick an away team: ")
    for x in range(10):
        n = random.randint(1,10)
        if x < 5:
            home.append(float(n) * (football_dict[picked_home] / 100))
        else:
            away.append(float(n) * (football_dict[picked_away] / 100))
    #home = sorted(home,reverse=True)
    #away = sorted(away,reverse=True)
    n = 0
    s = ""
    while(s != "s"):
        print("Push\'s\' to start the match!" )
        s = getch.getch()
    for x in range(5):
        if home[x] - 2 >= away[x]:
            time.sleep(2)
            home_goals += 1
            n = random.randint(n + 1,(x + 1)*19)
            print(f"{picked_home} {home_goals}-{away_goals} {picked_away} {n}'")
        elif away[x] - 3 >= home[x]:
            time.sleep(2)
            away_goals += 1
            n = random.randint(n + 1,(x + 1)*19)
            print(f"{picked_home} {home_goals}-{away_goals} {picked_away} {n}'")
    time.sleep(2)
    print(f"{picked_home} {home_goals}-{away_goals} {picked_away} FT")


football_league_table.main()
cls()
match()
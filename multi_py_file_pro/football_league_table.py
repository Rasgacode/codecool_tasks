import getch, random, os, time, csv

def main():
    break_var = ""
    text1 = "first.txt"
    text2 = "second.txt"
    text3 = "table.txt"
    text4 = "players.txt"
    text5 = "top_scorers.txt"
    table = {}
    players = {}
    fixtures = []
    main_dict = {}
    top_scorers = {}
    fixture_list = []
    load_rating_dict(main_dict, text1)
    load_schedule(fixture_list, text2)
    load_table(table, text3)
    load_players(players, text4)
    load_top_scorers(top_scorers, text5)
    cls()
    while(break_var != "exit"):
        print("\033[91m[0] Add a team (with rating)\n[1] Remove a team\n[2] Remove all team\n[3] Display the added teams \
        \n[4] Create schedule from added teams\n[5] Play the next fixtures\n[6] Display league table \
        \n[7] Display TOP scorers\n[8] Exit\033[00m")
        data_input = getch.getch()
        if data_input == "1":
            cls()
            sort_n_list(main_dict)
            picked_team = input("Write a team name to remove: ")
            if picked_team not in main_dict.keys():
                print(f"\"{picked_team}\" was not in your leauge table!")
                continue
            else:
                remove_team(main_dict, picked_team)
                save(main_dict, text1)
                cls()
                sort_n_list(main_dict)
        elif data_input == "4":
            cls()
            print("\033[91mAre you sure? Your last saved progress will be lost.\n[y] Yes\n[n] No\033[00m")
            ask = getch.getch()
            if ask == "y":
                cls()
                create_schedule(main_dict, fixture_list)
                save_schedule(fixture_list, text2)
                create_table(main_dict, table)
                save_table(table, text3)
                delete_top_scorers(top_scorers, text5)
            else:
                cls()
        elif data_input == "7":
            cls()
            display_top_scorers(top_scorers)
        elif data_input == "5":
            cls()
            rounds(fixture_list, fixtures)
            match(main_dict, fixtures, table, players, top_scorers)
            save_schedule(fixture_list, text2)
            save_table(table, text3)
            load_table(table, text3)
            save_top_scorers(top_scorers, text5)
            load_top_scorers(top_scorers, text5)
            if all(x.count("played") == 2 for x in fixture_list):
                print("No more fixtures! The league has finished!")
        elif data_input == "8":
            cls()
            print("\033[91mAre you sure? Do you want to quit?\n[y] Yes\n[n] Continue the game\033[00m")
            ask = getch.getch()
            if ask == "y":
                save(main_dict,text1)
                save_schedule(fixture_list, text2)
                save_table(table, text3)
                save_top_scorers(top_scorers, text5)
            elif ask == "n":
                cls()
                continue
            break_var = "exit"
        elif data_input == "3":
            cls()
            sort_n_list(main_dict)
        elif data_input == "2":
            cls()
            print("\033[91mAre you sure, you want to clear the all team from the table?\n[y] Yes\n[n] No\033[00m")
            ask = getch.getch()
            if ask == "y":
                clear_all(main_dict, text1)
                create_table(main_dict, table)
                save(main_dict, text1)
                save_table(table, text3)
                create_schedule(main_dict,fixture_list)
                save_schedule(fixture_list,text2)
                cls()
                sort_n_list(main_dict)
                print("Your table has cleared!")
            else:
                cls()
        elif data_input == "6":
            cls()
            display_table(table)
        elif data_input == "0":
            added_team = input("Add a team name with a rating(split with comma (\",\")): ").split(",")
            if len(added_team) != 2:
                cls()
                print("Invalid adding format!")
                continue
            elif not any(x.isdigit() for x in added_team[1]):
                cls()
                print("Invalid rating!")
                continue
            else:
                update_dict(main_dict, added_team)
                save(main_dict, text1)
                cls()
                sort_n_list(main_dict)
        else:
            cls()
            print("Invalid button!")
#parancsok bekérése, kontroll            

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
#Terminál clear

def update_dict(football_dict, team_and_point):
    football_dict.update({team_and_point[0] : int(team_and_point[1])})
#csapat bevitele a táblába

def sort_n_list(football_dict):
    name = "Team"
    pts = "Ratings"
    max_len_name = max([len(key) for key in football_dict.keys()] + [len(str(name))])
    max_len_pts = max([len(str(value)) for value in football_dict.values()] + [len(str(pts))])
    dash = "+" + ("-" * (max_len_name + 3)) + "+" + ("-" * max_len_pts) + "+"
    separator = "|"
    placing = 1
    head_n_foot = "-" * (max_len_name + max_len_pts + 6)

    print_list = sorted(football_dict.items(), key=lambda x: x[1], reverse=True)
    print(head_n_foot)
    print(f"{separator}{name:^{max_len_name + 3}}{separator}{pts:^{max_len_pts}}{separator}")
    for key, value in print_list:
        placing_str = str(placing) + "."
        print(dash)
        print(f"{separator}{placing_str:<3}{key:<{max_len_name}}{separator}{value:>{max_len_pts}}{separator}")
        placing += 1
    print(head_n_foot)
#tábla kiírása csökkenőben

def save(football_dict,text_name):
    sort_list = sorted(football_dict.items(), key=lambda x: x[1], reverse=True)
    open(text_name, 'w').close()
    with open(text_name, "a") as f:
        for key, value in sort_list:
            f.write(f"{key},{value}\n")
        f.close()
#felvitt csapatok lementése txt-be

def load_rating_dict(football_dict,text_name):
    with open(text_name, "r") as f:
        for x in f:
            (key, val) = x.split(",")
            football_dict [key] = int(val)
        f.close()
#felvitt csapatok betöltése txt-ből        

def clear_all(football_dict,text_name):
    football_dict.clear()
    open(text_name, 'w').close()
#benti lista és a txt teljes kitörlése

def remove_team(football_dict, team):
    del football_dict[team]
#megadott csapat kitörlése a táblából

def match(football_dict, fixtures, table_dict, players, top_scorers_dict):
    separator = "\033[91m----------------------------------------------\033[00m"
    s = ""
    while(s != "s"):
        print("\033[91mPush \'s\' to start the matches!\033[00m")
        s = getch.getch()
        print(separator)
    for team in range(0,len(fixtures),2):
        home = fixtures[team]
        away = fixtures[team + 1]
        home_rnd = []
        home_goals = 0
        home_players = []
        away_players = []
        away_rnd = []
        away_goals = 0
        for x in range(10):
            n = random.randint(1,10)
            if x < 5:
                home_rnd.append(float(n) * (football_dict[home] / 100))
            else:
                away_rnd.append(float(n) * (football_dict[away] / 100))
        n = 0
        for x in range(5):
            if home_rnd[x] - 2 >= away_rnd[x]:
                time.sleep(2)
                home_goals += 1
                rnd_player = random.randint(0,2)
                home_players.append(players[home][rnd_player])
                n = random.randint(n + 1,(x + 1)*19)
                print(f"{home} \033[91m{home_goals}\033[00m-{away_goals} {away} {n}' \033[34m{players[home][rnd_player]}\033[00m")
            elif away_rnd[x] - 3 >= home_rnd[x]:
                time.sleep(2)
                away_goals += 1
                rnd_player = random.randint(0,2)
                away_players.append(players[away][rnd_player])
                n = random.randint(n + 1,(x + 1)*19)
                print(f"{home} {home_goals}-\033[91m{away_goals}\033[00m {away} {n}' \033[34m{players[away][rnd_player]}\033[00m")
        time.sleep(2)
        print(f"{home} {home_goals}-{away_goals} {away} FT")
        print(separator)
        upload_to_table(home_goals, away_goals, home, away, table_dict)
        upload_to_top_scorers(home_players, away_players, top_scorers_dict)
#meccsek lejátszása sorsolás alapján

def save_schedule(fixture_list, text_name):
    open(text_name, 'w').close()
    with open(text_name, 'a') as f:
        for x in fixture_list:
            f.write(f"{x[0]},{x[1]},\n")
#lementi az aktuális menetrendet

def create_schedule(football_dict, fixture_list):
    if len(football_dict) % 2 != 0:
        print("The number of your teams is odd, pls correct this number to even")
    else:
        team_list = []
        fixture_list.clear()
        for x in football_dict.keys():
            team_list.append(x)
        for home in team_list:
            for away in team_list:       
                if home != away:
                    fixture_list.append([home, away])
        print("Your schedule has created!")
#megkreál egy új menetrendet txt-be(hogy betölthető legyen)

def create_table(football_dict, table_dict):
    table_dict.clear()
    for team in football_dict.keys():
        table_dict.update({team: [0, 0, 0, 0, 0, 0, 0, 0]})
#megkreál egy új tabellát

def load_table(table_dict, text_file):
    table_dict.clear()
    with open(text_file, "r") as f:
        r = csv.reader(f, delimiter=",")
        d = dict((row[0], list(map(int,row[1:]))) for row in r)
        for key, value in d.items():
            table_dict.update({key: []})
            for x in value:
                table_dict[key].append(x)
# betölti a tabellát egy txt-ből

def save_table(table_dict, text_file):
    save_list = sorted(table_dict.items(), key=lambda x: (x[1][7], x[1][6], x[1][4]), reverse=True)
    open(text_file, "w").close()
    with open(text_file, "a") as f:
        for key, value in save_list:
            f.write(f"{key}")
            for x in value:
                f.write(f",{x}")
            f.write("\n")
#lementi txt be a tabellát

def load_schedule(fixture_list, text_name):
    fixture_list.clear()
    with open(text_name, "r") as f:
        for x in f:            
            fixture_list.append(x.split(','))
#betölti az elmentett menetrendet

def rounds(fixture_list,fixtures):
    fixtures.clear()
    from random import shuffle
    shuffle(fixture_list)
    for x in range(len(fixture_list)):
        if fixture_list[x][0] not in fixtures and fixture_list[x][1] not in fixtures and not any(y == "played" for y in fixture_list[x]):
            fixtures.append(fixture_list[x][0])
            fixtures.append(fixture_list[x][1])
            print(f"{fixture_list[x][0]} - {fixture_list[x][1]}")
            fixture_list[x][0] = "played"
            fixture_list[x][1] = "played"
#kisorsolja a fordulókat

def display_table(table_dict):
    if len(table_dict) == 0:
        print("Your league contains 0 team!")
    else:
        header = ["Pos", "Team", "Pld", "W", "D", "L", "GF", "GA", "GD", "Pts"]
        separator = "|"
        max_lenght_team = max([len(key) for key in table_dict.keys()]) + 1
        head_n_foot = "-" * (56 + max_lenght_team)
        index = 1
        for key, value in table_dict.items():
            if index == 1:
                print(head_n_foot)
                print(separator, end="")
                for x in header:
                    if x == "Team":
                        print(f"{x:^{max_lenght_team}}{separator}", end="")
                    else:
                        print(f"{x:^5}{separator}", end="")
                print()
                print(head_n_foot)
            print(separator, end="")
            print(f"{index:^5}{separator}{key:<{max_lenght_team}}{separator}", end="")
            for x in value:
                print(f"{x:>5}{separator}", end="")
            print()
            print(head_n_foot)
            index += 1
#league table kiírása

def upload_to_table(home_goal, away_goal, home_team, away_team, table_dict):
    table_dict[home_team][0] += 1
    if home_goal > away_goal:
        table_dict[home_team][1] += 1
        table_dict[home_team][7] += 3
    elif home_goal == away_goal:
        table_dict[home_team][2] += 1
        table_dict[home_team][7] += 1
    else:
        table_dict[home_team][3] += 1
    table_dict[home_team][4] += home_goal
    table_dict[home_team][5] += away_goal
    table_dict[home_team][6] = table_dict[home_team][4] - table_dict[home_team][5]

    table_dict[away_team][0] += 1
    if away_goal > home_goal:
        table_dict[away_team][1] += 1
        table_dict[away_team][7] += 3
    elif home_goal == away_goal:
        table_dict[away_team][2] += 1
        table_dict[away_team][7] += 1
    else:
        table_dict[away_team][3] += 1
    table_dict[away_team][4] += away_goal
    table_dict[away_team][5] += home_goal
    table_dict[away_team][6] = table_dict[away_team][4] - table_dict[away_team][5]
#league table feltöltése a meccsek adataival

def load_players(players_dict, text_file):
    with open(text_file, "r") as f:
        r = csv.reader(f, delimiter=",")
        d = dict((row[0], list(map(str,row[1:]))) for row in r)
        for key, value in d.items():
            players_dict.update({key: []})
            for x in value:
                players_dict[key].append(x)
#játékosok, csapatokhoz rendelve

def upload_to_top_scorers(home_players, away_players, top_scorers_dict):
    for x in home_players:
        if x in top_scorers_dict:
            top_scorers_dict[x] += 1
        else:
            top_scorers_dict[x] = 1
    for x in away_players:
        if x in top_scorers_dict:
            top_scorers_dict[x] += 1
        else:
            top_scorers_dict[x] = 1
#góllövő lista feltöltése a meccsek adataival
    
def delete_top_scorers(top_scorers_dict, text_file):
    top_scorers_dict.clear()
    open(text_file, "w").close()
#törli a legutóbbi góllövő listát

def save_top_scorers(top_scorers_dict, text_file):
    open(text_file, "w").close()
    sorted_list = sorted(top_scorers_dict.items(), key=lambda x: x[1], reverse=True)
    with open(text_file, "a") as f:
        for key, value in sorted_list:
            f.write(key + "," + str(value) + "\n")
#lementi a góllövő listát a txt-be

def load_top_scorers(top_scorers_dict, text_file):
    top_scorers_dict.clear()
    with open(text_file, "r") as f:
        for x in f:
            (key, val) = x.split(",")
            top_scorers_dict [key] = int(val)
#betölti a góllövő listát a txt-ből

def display_top_scorers(top_scorer_dict):
    name = "Player"
    pts = "Scores"
    max_len_name = max([len(key) for key in top_scorer_dict.keys()] + [len(str(name))])
    max_len_pts = max([len(str(value)) for value in top_scorer_dict.values()] + [len(str(pts))])
    dash = "+" + ("-" * (max_len_name + 3)) + "+" + ("-" * max_len_pts) + "+"
    separator = "|"
    placing = 1
    head_n_foot = "-" * (max_len_name + max_len_pts + 6)
    print(head_n_foot)
    print(f"{separator}{name:^{max_len_name + 3}}{separator}{pts:^{max_len_pts}}{separator}")
    for key, value in top_scorer_dict.items():
        if placing == 11:
            break
        placing_str = str(placing) + "."
        print(dash)
        print(f"{separator}{placing_str:<3}{key:<{max_len_name}}{separator}{value:>{max_len_pts}}{separator}")
        placing += 1
    print(head_n_foot)
#góllövő lista kírása

if __name__ == "__main__":
    main()

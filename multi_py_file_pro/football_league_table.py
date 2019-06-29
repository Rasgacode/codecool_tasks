import getch, random, os, time, csv


def main():
    break_var = ""
    text1 = "first.txt"
    text2 = "second.txt"
    fixtures = []
    main_dict = {}
    fixture_dict = {}
    load_rating_dict(main_dict, text1)
    load_schedule(fixture_dict, text2)
    cls()
    while(break_var != "exit"):
        print("\033[91mYou can use exit,list,save,clear(delete all data),\nmatch(simulate a team vs team match) and remove(remove only one team)\ncommands on the command line.\033[00m")
        data_input = input("Enter a team and their points(split with comma): ").split(",")
        if data_input[0] == "remove":
            if data_input[1] not in main_dict.keys():
                print(f"\"{data_input[1]}\" was not in your leauge table!")
                continue
            else:
                remove_team(main_dict, data_input)
        elif data_input[0] == "cs":
            creat_schedule(main_dict, fixture_dict, text2)
        elif data_input[0] == "fixture":
            rounds(fixture_dict, fixtures)
            match(main_dict, fixtures)
        elif data_input[0] == "exit":
            ask = input("Do you want to save your project?(y/n): ")
            if ask == "y":
                save(main_dict,text1)
                save_schedule(fixture_dict, text2)
            break_var = "exit"
        elif data_input[0] == "list":
            cls()
            sort_n_list(main_dict)
        elif data_input[0] == "save":
            save(main_dict, text1)
            save_schedule(fixture_dict, text2)
            load_schedule(fixture_dict, text2)
        elif data_input[0] == "clear":
            clear_all(main_dict, text1)
        elif len(data_input) > 2 or len(data_input) > 1 and not all(x.isdigit() for x in data_input[1]):
            print("You did something wrong!")
            continue 
        elif len(data_input) < 2:
            print("You did something wrong!")
            continue
        else:
            update_dict(main_dict, data_input)
#parancsok bekérése, kontroll            

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def update_dict(football_dict, team_and_point):
    team_and_point[1] = int(team_and_point[1])
    football_dict.update({team_and_point[0] : team_and_point[1]})
#csapat bevitele a táblába

def sort_n_list(football_dict):
    name = "Team name"
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
            f.write(key + "," + str(value) + "\n")
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
    del football_dict[team[1]]
#megadott csapat kitörlése a táblából

def match(football_dict, fixtures):
    for team in range(0,len(fixtures),2):
        home = fixtures[team]
        away = fixtures[team + 1]
        home_rnd = []
        home_goals = 0
        away_rnd = []
        away_goals = 0
        for x in range(10):
            n = random.randint(1,10)
            if x < 5:
                home_rnd.append(float(n) * (football_dict[home] / 100))
            else:
                away_rnd.append(float(n) * (football_dict[away] / 100))
        n = 0
        s = ""
        while(s != "s"):
            print("Push \'s\' to start the match!" )
            s = getch.getch()
        for x in range(5):
            if home_rnd[x] - 2 >= away_rnd[x]:
                time.sleep(2)
                home_goals += 1
                n = random.randint(n + 1,(x + 1)*19)
                print(f"{home} {home_goals}-{away_goals} {away} {n}'")
            elif away_rnd[x] - 3 >= home_rnd[x]:
                time.sleep(2)
                away_goals += 1
                n = random.randint(n + 1,(x + 1)*19)
                print(f"{home} {home_goals}-{away_goals} {away} {n}'")
        time.sleep(2)
        print(f"{home} {home_goals}-{away_goals} {away} FT")
#match lejátszása 2 kiválaszott csapattal

def save_schedule(fixture_dict, text_name):
    open(text_name, 'w').close()
    with open(text_name, 'a') as f:
        for key, value in fixture_dict.items():
            f.write(f"{key}")
            for item in value:
                f.write(f",{item}")
            f.write("\n")
#lementi az aktuális menetrendet

def creat_schedule(football_dict, fixture_dict, text_name):
    team_list = []
    fixture_dict.clear()
    for key, value in football_dict.items():
        team_list.append(key)
    for key, value in football_dict.items():
        fixture_dict.update({key: []})        
        for x in team_list:
            if key != x:
                fixture_dict[key].append(x)
    open(text_name, 'w').close()
    with open(text_name, 'a') as f:
        for key, value in fixture_dict.items():
            f.write(f"{key}")
            for item in value:
                f.write(f",{item}")
            f.write("\n")
#megkreál egy új menetrendet txt-be(hogy betölthető legyen)

def load_schedule(fixture_dict, text_name):
    with open(text_name, "r") as f:
        r = csv.reader(f, delimiter=",")
        d = dict((item[0], list(map(str, item[1:]))) for item in r)
        f.close()
        for key, value in d.items():
            fixture_dict.update({key: value})
#betölti az elmentett menetrendet

def rounds(fixture_dict,fixtures):
    index_list = []
    fixtures.clear()
    for key, value in fixture_dict.items():
        index_list.append(key)
    while(len(fixtures) != len(index_list)):
        while(True):
            random_team = random.randint(0, len(index_list) -1)
            if index_list[random_team] not in fixtures and not all(x == "played" for x in fixture_dict[index_list[random_team]]):
                fixtures.append(index_list[random_team])
                break
        while(True):
            random_team = random.randint(0, len(index_list) - 2)
            if fixture_dict[fixtures[-1]][random_team] not in fixtures and fixture_dict[fixtures[-1]][random_team] != "played" :
                fixtures.append(fixture_dict[fixtures[-1]][random_team])
                fixture_dict[fixtures[-2]][random_team] = "played"
                break
    print(fixtures)
    print(fixture_dict)
#kisorsolja a fordulókat

if __name__ == "__main__":
    main()

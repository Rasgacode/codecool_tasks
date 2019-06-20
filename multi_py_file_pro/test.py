import os

def main():
    text = "first.txt"
    main_dict = {}
    load_dict(main_dict,text)
    cls()
    while(True):
        print("\033[91mYou can use exit,list,save,clear(delete all data)\nand remove commands on the command line.\033[00m")
        data_input = input("Enter a team and their points(split with comma): ").split(",")
        commands(main_dict, data_input, text)


def commands(main_dict, data_input, text):
    n = data_input[0]
    d = {
    "remove": remove_team,
    "list": sort_n_list,
    "save": save,
    "clear": clear_all,
    "add": update_dict
    }
    return d[n](main_dict)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def update_dict(football_dict, team_and_point):
    if len(team_and_point) == 3 and all(x.isdigit() for x in team_and_point[2]):
        team_and_point[2] = int(team_and_point[2])
        football_dict.update({team_and_point[1] : team_and_point[2]})
    else:
        print("You did something wrong!")


def sort_n_list(football_dict):
    cls()
    name = "Team name"
    pts = "Pts"
    max_len_name = max([len(key) for key in football_dict.keys()] + [len(str(name))])
    max_len_pts = max([len(str(value)) for value in football_dict.values()] + [len(str(pts))])
    dash = "+" + ("-" * (max_len_name + 3)) + "+" + ("-" * max_len_pts) + "+"
    separator = "|"
    placing = 1
    head_n_foot = "-" * (max_len_name + max_len_pts + 6)

    print_list = sorted(football_dict.items(), key=lambda x: x[1], reverse=True)
    print(head_n_foot)
    print(f"{separator}   {name:^{max_len_name}}{separator}{pts:^{max_len_pts}}{separator}")
    for key, value in print_list:
        placing_str = str(placing) + "."
        print(dash)
        print(f"{separator}{placing_str:<3}{key:<{max_len_name}}{separator}{value:>{max_len_pts}}{separator}")
        placing += 1
    print(head_n_foot)


def save(football_dict,text_name):
    sort_list = sorted(football_dict.items(), key=lambda x: x[1], reverse=True)
    open(text_name, 'w').close()
    with open(text_name, "a") as f:
        for key, value in sort_list:
            f.write(key + "," + str(value) + "\n")
        f.close()


def load_dict(football_dict,text_name):
    with open(text_name, "r") as f:
        for x in f:
            (key, val) = x.split(",")
            football_dict [key] = int(val)
        f.close()
        

def clear_all(football_dict,text_name):
    football_dict.clear()
    open(text_name, 'w').close()


def remove_team(football_dict, team):
    if team[1] not in football_dict.keys():
        print(f"\"{team[1]}\" was not in your leauge table!")
    else:
        del football_dict[team[1]]


if __name__ == "__main__":
    main()

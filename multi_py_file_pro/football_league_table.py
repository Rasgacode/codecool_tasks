import os


def main():
    text = "first.txt"
    main_dict = {}
    load_dict(main_dict,text)
    cls()
    while(True):
        print("\033[91mYou can use exit,list,save,clear(delete all data)\nand remove commands on the command line.\033[00m")
        data_input = input("Enter a team and their points(split with comma): ").split(",")
        if data_input[0] == "remove":
            if data_input[1] not in main_dict.keys():
                print(f"\"{data_input[1]}\" was not in your leauge table!")
                continue
            else:
                remove_team(main_dict, data_input)
        elif data_input[0] == "exit":
            temp = input("Do you want to save your project?(y/n): ")
            if temp == "y":
                save(main_dict,text)
            break
        elif data_input[0] == "list":
            cls()
            sort_n_list(main_dict)
        elif data_input[0] == "save":
            save(main_dict, text)
        elif data_input[0] == "clear":
            clear_all(main_dict, text)
        elif len(data_input) > 2 or len(data_input) > 1 and not all(x.isdigit() for x in data_input[1]):
            print("You did something wrong!")
            continue 
        elif len(data_input) < 2:
            print("You did something wrong!")
            continue
        else:
            update_dict(main_dict, data_input)
            

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def update_dict(football_dict, team_and_point):
    team_and_point[1] = int(team_and_point[1])
    football_dict.update({team_and_point[0] : team_and_point[1]})


def sort_n_list(football_dict):
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
    del football_dict[team[1]]


if __name__ == "__main__":
    main()

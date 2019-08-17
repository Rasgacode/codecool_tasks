def calc_box_lenght(table, title_list, int_var):
    return max([len(str(inner_list[int_var])) for inner_list in table] + [len(title_list[int_var])])


def calc_head_n_foot(table, title_list): 
    all_calc_box_lenght = [calc_box_lenght(table, title_list, i) for i in range(len(title_list))]
    sum_all_calc_box = 0
    for item in all_calc_box_lenght:
        sum_all_calc_box += item
    return sum_all_calc_box  + len(title_list) - 1

    
def print_table(table, title_list):
    head = "/" + "-" * calc_head_n_foot(table, title_list) + "\\"
    foot = "\\" + "-" * calc_head_n_foot(table, title_list) + "/" 
    row_length = len(title_list)
    for i in range(len(table)):
        if i == 0:
            print(f"{head}\n|", end = "")
            for k in range(len(title_list)):
                box_lenght = calc_box_lenght(table, title_list, k)
                print(f"{title_list[k]:^{box_lenght}}|", end = "")
            for l in range(len(title_list)):
                box_lenght = calc_box_lenght(table, title_list, l)
                if l == 0:
                    print("\n|" + "-" * box_lenght + "|", end = "")
                else:
                    print("-" * box_lenght + "|", end = "")
            print()
            for j in range(len(table[i])):
                box_lenght = calc_box_lenght(table, title_list, j)
                if j == 0:
                    print("|", end = "")
                print(f"{table[i][j]:^{box_lenght}}|", end = "")
            for k_1 in range(len(title_list)):
                box_lenght = calc_box_lenght(table, title_list, k_1)
                if k_1 == 0 and i != len(table) - 1:
                    print("\n|" + "-" * box_lenght + "|", end = "")
                else:
                    if i == len(table) - 1:
                        print("\n" + foot)
                        break
                    else:
                        print("-" * box_lenght + "|", end = "")
        print()    


def print_table_2():
    head = "/" + "-" * calc_head_n_foot(table, title_list) + "\\"
    foot = "\\" + "-" * calc_head_n_foot(table, title_list) + "/" 
    row_length = len(title_list)


print_table()
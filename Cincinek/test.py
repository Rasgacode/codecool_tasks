import random


def random_list_item(metal_list):
    return random.choice(metal_list)


def replace_letters(metal_str):
    return metal_str.replace("u", "ü").replace("o", "ö")


def main():
    first_name_list = ["Obscure", "Sober", "Vengeful", "Profane", "Bestial", "Undead"]
    second_name_list = ["Angel", "Burial", "Funeral", "Chaos", "Slyme", "Lobotomy", "Deamon"]
    print(f"Your metal band name is {replace_letters(random_list_item(first_name_list))}\
 {replace_letters(random_list_item(second_name_list))}.")


if __name__ == '__main__':
    main()
    
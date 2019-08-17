def get_input(instruction):
    while(True):
        input_ = input(instruction)
        if len(input_) != 1 or any(character.isdigit() for character in input_):
            print("Wrong input!")
        else:
            return input_


def get_matching_words(data_list, input_):
    return [item for item in data_list if item[0].lower() == input_.lower()]


def print_result(matching_list):
    if len(matching_list) > 0:
        print(f"Your input match with these words first letter --> {matching_list}")
    else:
        print("Your input match with 0 word")


def main():
    data_list = ["postreme", "Verminology", "Palaeophile", "zegedine", "flammulated", "keckle", "Individualism",
    "viaggiatory", "Dashpot", "Mecometer", "Zug", "orismology", "beatus", "Unicorn", "Latitudinous"]
    print_result(get_matching_words(data_list, get_input("Enter a letter: ")))


if __name__ == '__main__':
    main()
    
    
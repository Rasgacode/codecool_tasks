import random


def choose_random_word(list_of_words):
    return random.choice(list_of_words)


def get_input(instruction):
    while(True):
        input_ = input(instruction)
        if len(input_) != 1 or any(character.isdigit() for character in input_):
            print("Wrong input!")
        else:
            return input_


def make_guessed_letter_list(randomed_word):
    return ["_" for i in range(len(randomed_word))]


def make_corresponding_characters_list(input_, randomed_word, guessed_letters, incorrect_letters):
    if input_ in randomed_word:
        for i, letter in enumerate(randomed_word):
            if input_ == letter:
                guessed_letters[i] = letter
    elif input_ not in incorrect_letters:
        incorrect_letters.append(input_)


def display_founded_letters(guessed_letters, incorrect_letters):
    letters_in_str = "".join(guessed_letters)
    print(f"There are your found letters: {letters_in_str}\nThere are your missed letters: {incorrect_letters}")


def check_win_n_exit(guessed_letters):
    if "_" not in guessed_letters:
        print("You have guessed the word!")
        return "off"
    return "on"


def main():
    words = ["experience", "honor", "justice", "sacrefice", "scar", "wisdom", "might", "dragon", "knight"]
    random_word = choose_random_word(words)
    guessed_letters = make_guessed_letter_list(random_word)
    incorrect_letters = []
    exit_var = "on"
    while(exit_var != "off"):
        letter = get_input("Enter a letter: ")
        make_corresponding_characters_list(letter, random_word, guessed_letters, incorrect_letters)
        display_founded_letters(guessed_letters, incorrect_letters)
        exit_var = check_win_n_exit(guessed_letters)


if __name__ == '__main__':
    main()
    


    
            
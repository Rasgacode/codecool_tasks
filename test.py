import os
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def Print():
    dash = "-"*7
    divider = "|"

    for x in range(len(board)):
        if x == 0:
            print(dash)
        print(divider + str(board[x]), end="")
        if x == 2 or x == 5 or x == 8:
            print("|")
            print(dash)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def userInput(board):
    while(True):
        try:
            enterNum = int(input("Please enter the number: "))
        except ValueError:
            print("Use only numbers please!")
            continue
        if enterNum not in board:
            print("Invalid position!")
            continue
        elif board[enterNum] == "x" or board[enterNum] == "o":
            print("That position is already taken!")
            continue
        else:
            board[enterNum] = "x"
            break

cls()
Print()
userInput(board)
cls()
Print()
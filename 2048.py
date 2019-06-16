import os, getch, random, sys


def main():
    board = []
    load_board(board)
    random_2(board)
    random_2(board)
    while(True):
        cls()
        print_board(board)
        control(board)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_board(board):
    for x in range(4):
        board.append([])
        for y in range(4):
            board[x].append(0)


def print_board(board):
    separator = "|"
    dash = "+----" * 4 + "+"
    colors = {
    2: "\033[88m   2\033[00m",
    4: "\033[91m   4\033[00m",
    8: "\033[92m   8\033[00m", 
    16: "\033[93m  16\033[00m", 
    32: "\033[94m  32\033[00m", 
    64: "\033[96m  64\033[00m", 
    128: "\033[97m 128\033[00m", 
    256: "\033[33m 256\033[00m", 
    512: "\033[34m 512\033[00m", 
    1024: "\033[95m1024\033[00m",
    2048: "\033[90m2048\033[00m"
    }
    for x in range(len(board)):
        if x == 0:
            print(dash)
        for y in range(len(board)):
            if board[x][y] == 0:
                print(separator + "{:>4}".format(""), end = "")
            else:
                print(separator + colors[board[x][y]], end = "")
        print(separator)
        print(dash)
    print("Use w,a,s,d to control the board!")


def random_2(board):
    while(True):
        x = random.randint(0,3)
        y = random.randint(0,3)
        if board[x][y] == 0:
            board[x][y] = 2
            break


def control(board):
    can_random = False
    rotated = []
    pressed_b = getch.getch()
    if pressed_b == "w":
        temp = list(zip(*board))
        for x in temp:
            rotated.append(list(x))
        can_random = moves(rotated)
        board.clear()
        temp = list(zip(*rotated))
        for x in temp:
            board.append(list(x))
    elif pressed_b == "a":
        for x in board:
            rotated.append(x)
        can_random = moves(rotated)
        board.clear()
        for x in rotated:
            board.append(x)
    elif pressed_b == "s":
        temp = list(zip(*board[::-1]))
        for x in temp:
            rotated.append(list(x))
        can_random = moves(rotated)
        board.clear()
        temp = list(zip(*rotated))
        temp = temp[::-1]
        for x in temp:
            board.append(list(x))
    elif pressed_b == "d":
        for x in board:
            rotated.append(x[::-1])
        can_random = moves(rotated)
        board.clear()
        for x in rotated:
            board.append(x[::-1])
    y = 0
    for x in board:
        if any(y == 2048 for y in x):
            print("\033[91mYOU REACHED 2048! GGWP!\033[00m")
            sys.exit()
        if any(y == 0 for y in x):
            break
        elif y == 3:
            print("\033[91mGAME OVER\033[00m")
            sys.exit()
        y += 1
    if can_random == True:
        random_2(board)


def moves(rotated):
    can_random = False
    for x in range(4):
        observer = [True, True]
        for y in range(1,4):
            if rotated[x][y] == 0:
                continue
            if rotated[x][0] == 0 or rotated[x][0] == rotated[x][y] and observer[0] == True:
                if rotated[x][0] == 0:
                    rotated[x][0] += rotated[x][y]
                    rotated[x][y] = 0
                    can_random = True
                else:
                    rotated[x][0] += rotated[x][y]
                    rotated[x][y] = 0
                    observer[0] = False
                    can_random = True
            elif y > 1 and rotated[x][1] == 0 or rotated[x][1] == rotated[x][y] and observer[1] == True and y > 1:
                if rotated[x][1] == 0:
                    rotated[x][1] += rotated[x][y]
                    rotated[x][y] = 0
                    can_random = True
                else:
                    rotated[x][1] += rotated[x][y]
                    rotated[x][y] = 0
                    observer[1] = False
                    can_random = True
            elif y > 2 and rotated[x][2] == 0 or rotated[x][2] == rotated[x][y] and y > 2:
                rotated[x][2] += rotated[x][y]
                rotated[x][y] = 0
                can_random = True
    return  can_random


if __name__ == "__main__":
    main()
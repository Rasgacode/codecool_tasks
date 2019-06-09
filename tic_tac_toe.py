import os
import time
import random
tablePosition = [1, 2, 3, 4, 5, 6, 7, 8, 9]
winCondition = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 5, 8], [1, 4, 7], [0, 3, 6]]
endList = []
redX = "\033[91mx\033[00m"
greenO = "\033[92mo\033[00m"
pointsList = [0, 0, 0]


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def table(position):
    points = "Player:{} Tie:{} Computer:{}".format(pointsList[0], pointsList[1], pointsList[2])
    firstLine = "|{}|{}|{}|".format(position[0], position[1], position[2])
    secondLine = "|{}|{}|{}|".format(position[3], position[4], position[5])
    thirdLine = "|{}|{}|{}|".format(position[6], position[7], position[8])
    dash = "-"*7

    print(points)
    print(dash)
    print(firstLine)
    print(dash)
    print(secondLine)
    print(dash)
    print(thirdLine)
    print(dash)


def selection(position):
    while(True):
        try:
            select = int(input("Enter a number for your x position: "))
        except ValueError:
            print("Use only numbers (1-9)!")
            continue
        if select not in position:
            print("Use unused numbers (1-9)!")
            continue
        else:
            break

    for x in range(len(position)):
        if position[x] == select:
            position[x] = redX


def aiSelection(winCondition, position):
    time.sleep(1)
    marker = 0
    for x in range(len(winCondition)):
        temp = winCondition[x]
        if position[temp[0]] == position[temp[1]] and position[temp[0]] == greenO and position[temp[2]] != redX:
            position[temp[2]] = greenO
            marker = 1
            break
        elif position[temp[0]] == position[temp[2]] and position[temp[0]] == greenO and position[temp[1]] != redX:
            position[temp[1]] = greenO
            marker = 1
            break
        elif position[temp[1]] == position[temp[2]] and position[temp[1]] == greenO and position[temp[0]] != redX:
            position[temp[0]] = greenO
            marker = 1
            break
    if marker == 0:
        for x in range(len(winCondition)):
            temp = winCondition[x]
            if position[temp[0]] == position[temp[1]] and position[temp[0]] == redX and position[temp[2]] != greenO:
                position[temp[2]] = greenO
                marker = 1
                break
            elif position[temp[0]] == position[temp[2]] and position[temp[0]] == redX and position[temp[1]] != greenO:
                position[temp[1]] = greenO
                marker = 1
                break
            elif position[temp[1]] == position[temp[2]] and position[temp[1]] == redX and position[temp[0]] != greenO:
                position[temp[0]] = greenO
                marker = 1
                break
    if marker == 0:
        while(True):
            temp = random.randint(0, 8)
            if position[temp] == redX or position[temp] == greenO:
                continue
            else:
                position[temp] = greenO
                break


def winOrDraw(winCondition, position, endList):
    for x in range(len(winCondition)):
        temp = winCondition[x]
        if position[temp[0]] == redX and position[temp[1]] == redX and position[temp[2]] == redX:
            endList.append(1)
            break
        if position[temp[0]] == greenO and position[temp[1]] == greenO and position[temp[2]] == greenO:
            endList.append(1)
            break


def main():
    retry = "y"

    while(retry == "y"):
        tablePosition = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        winCondition = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [2, 5, 8], [1, 4, 7], [0, 3, 6]]
        endList = []
        rounds = 0

        while(True):
            cls()
            table(tablePosition)
            selection(tablePosition)
            cls()
            table(tablePosition)
            winOrDraw(winCondition, tablePosition, endList)
            if len(endList) == 1:
                print("You won!")
                pointsList[0] += 1
                break
            if rounds > 3:
                print("It's a tie!")
                pointsList[1] += 1
                break
            aiSelection(winCondition, tablePosition)
            cls()
            table(tablePosition)
            winOrDraw(winCondition, tablePosition, endList)
            if len(endList) == 1:
                print("Computer won!")
                pointsList[2] += 1
                break
            rounds += 1

        retry = input("Do you want to retry?(y/n): ")


main()

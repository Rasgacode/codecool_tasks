import random, os

canRandom = False
firstLine = []
secondLine = []
thirdLine = []
fourthLine = []
newTableList = []
tableList = []
for x in range(16):
    tableList.append(0)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def table(tableList):
    separator = "|"
    dash = "-" * 21
    colors = {
    4: "\033[91m   4\033[00m",
    8: "\033[92m   8\033[00m", 
    16: "\033[93m  16\033[00m", 
    32: "\033[94m  32\033[00m", 
    64: "\033[96m  64\033[00m", 
    128: "\033[97m 128\033[00m", 
    256: "\033[33m 256\033[00m", 
    512: "\033[34m 512\033[00m", 
    1024: "\033[95m1024\033[00m"
    }
    print(dash)
    for x in range(16):
        if tableList[x] == 0:
            print("|{:>4}".format(''), end="") 
        elif tableList[x] == 2 or tableList[x] == 2048:
            print("|{:>4}".format(tableList[x]), end="")
        else:
            for key, value in colors.items():
                if key == tableList[x]:
                    print(separator+value, end="")
                    break
        if x == 3 or x == 7 or x == 11 or x == 15:
            print(separator)
            print(dash)


def randomPosition(tableList):
    while(True):
        randomNum = random.randint(0, 15)
        if tableList[randomNum] == 0:
            tableList[randomNum] = 2
            break
        else:
            continue


def control(tableList):
    commands = ["w", "a", "s", "d"]
    while(True):
        Input = input("Enter a command(w,a,s,d): ")
        if Input not in commands:
            print("Use w,a,s,d!")
            continue
        else:
            break
            
    if Input == commands[0]:
        upCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine)
    elif Input == commands[1]:
        leftCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine)
    elif Input == commands[2]:
        downCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine)
    elif Input == commands[3]:
        rightCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine)


def commandBody(newTableList):
    global canRandom
    for x in range(4):
        firstIndex = newTableList[x][0]
        secondIndex = newTableList[x][1]
        thirdIndex = newTableList[x][2]
        fourthIndex = newTableList[x][3]
        observer = [True, True]
        for y in range(1, 4):
            if newTableList[x][y] == 0:
                continue
            else:
                if y == 1 and firstIndex == 0:
                    firstIndex += secondIndex
                    secondIndex = 0
                    canRandom = True
                elif y == 1 and firstIndex == secondIndex:
                    firstIndex += secondIndex
                    secondIndex = 0
                    observer[0] = False
                    canRandom = True
                elif y == 2 and secondIndex == 0 and firstIndex == 0:
                    firstIndex += thirdIndex
                    thirdIndex = 0
                    canRandom = True
                elif y == 2 and secondIndex == 0 and firstIndex == thirdIndex and observer[0] == True:
                    firstIndex += thirdIndex
                    thirdIndex = 0
                    observer[0] = False
                    canRandom = True
                elif y == 2 and secondIndex == 0:
                    secondIndex += thirdIndex
                    thirdIndex = 0
                    canRandom = True
                elif y == 2 and secondIndex == thirdIndex:
                    secondIndex += thirdIndex
                    thirdIndex = 0
                    observer[1] = False
                    canRandom = True
                elif y == 3 and thirdIndex == 0 and secondIndex == 0 and firstIndex == 0:
                    firstIndex += fourthIndex
                    fourthIndex = 0
                    canRandom = True
                elif y == 3 and thirdIndex == 0 and secondIndex == 0 and firstIndex == fourthIndex and observer[0] == True:
                    firstIndex += fourthIndex
                    fourthIndex = 0
                    canRandom = True
                elif y == 3 and thirdIndex == 0 and secondIndex == 0:
                    secondIndex += fourthIndex
                    fourthIndex = 0
                    canRandom = True
                elif y == 3 and thirdIndex == 0 and secondIndex == fourthIndex and observer[1] == True:
                    secondIndex += fourthIndex
                    fourthIndex = 0
                    canRandom = True
                elif y == 3 and thirdIndex == 0:
                    thirdIndex += fourthIndex
                    fourthIndex = 0
                    canRandom = True
                elif y == 3 and thirdIndex == fourthIndex:
                    thirdIndex += fourthIndex
                    fourthIndex = 0
                    canRandom = True
        newTableList[x][0] = firstIndex 
        newTableList[x][1] = secondIndex 
        newTableList[x][2] = thirdIndex
        newTableList[x][3] = fourthIndex


def upCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine):
    firstLine = [tableList[0], tableList[4],
                tableList[8], tableList[12]]
    secondLine = [tableList[1], tableList[5],
                tableList[9], tableList[13]]
    thirdLine = [tableList[2], tableList[6],
                tableList[10], tableList[14]]
    fourthLine = [tableList[3], tableList[7],
                tableList[11], tableList[15]]
    newTableList = [firstLine, secondLine, thirdLine, fourthLine]

    commandBody(newTableList)

    temp = 0
    for x in range(4):
        for y in range(4):
            tableList[temp] = newTableList[y][x]
            temp += 1


def leftCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine):
    firstLine = [tableList[0], tableList[1],
                tableList[2], tableList[3]]
    secondLine = [tableList[4], tableList[5],
                tableList[6], tableList[7]]
    thirdLine = [tableList[8], tableList[9],
                tableList[10], tableList[11]]
    fourthLine = [tableList[12], tableList[13],
                tableList[14], tableList[15]]
    newTableList = [firstLine, secondLine, thirdLine, fourthLine]

    commandBody(newTableList)

    temp = 0
    for x in range(4):
        for y in range(4):
            tableList[temp] = newTableList[x][y]
            temp += 1


def downCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine):
    firstLine = [tableList[12], tableList[8],
                tableList[4], tableList[0]]
    secondLine = [tableList[13], tableList[9],
                tableList[5], tableList[1]]
    thirdLine = [tableList[14], tableList[10],
                tableList[6], tableList[2]]
    fourthLine = [tableList[15], tableList[11],
                tableList[7], tableList[3]]
    newTableList = [firstLine, secondLine, thirdLine, fourthLine]

    commandBody(newTableList)

    temp = 0
    for x in range(3,-1,-1):
        for y in range(4):
            tableList[temp] = newTableList[y][x]
            temp += 1


def rightCommand(tableList, newTableList, firstLine, secondLine, thirdLine, fourthLine):
    firstLine = [tableList[3], tableList[2],
                tableList[1], tableList[0]]
    secondLine = [tableList[7], tableList[6],
                tableList[5], tableList[4]]
    thirdLine = [tableList[11], tableList[10],
                tableList[9], tableList[8]]
    fourthLine = [tableList[15], tableList[14],
                tableList[13], tableList[12]]
    newTableList = [firstLine, secondLine, thirdLine, fourthLine]

    commandBody(newTableList)

    temp = 0
    for x in range(4):
        for y in range(3,-1,-1):
            tableList[temp] = newTableList[x][y]
            temp += 1


def main(tableList):
    global canRandom
    randomPosition(tableList)
    randomPosition(tableList)
    while(True):
        if 0 not in tableList:
            print("GAME OVER!")
            break
        cls()
        if canRandom == True:
            randomPosition(tableList)
            canRandom = False
        table(tableList)
        if 2048 in tableList:
            print("You reached 2048! GGWP!")
            break
        control(tableList)
        

if __name__ == "__main__":
    main(tableList)
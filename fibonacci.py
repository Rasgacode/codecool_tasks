
howMany = int(input("How many numbers you want to print out?: "))
countListIndex = 0
nextNumber = 0
fibonacci = []

while(countListIndex < howMany):
    if countListIndex < 2:
        fibonacci.append(countListIndex)
    else:
        nextNumber = fibonacci[countListIndex - 1] + \
            fibonacci[countListIndex - 2]
        fibonacci.append(nextNumber)
    countListIndex += 1


def Print():
    onespace = str(len(str(howMany)) + 1)
    twospace = str(len(str(fibonacci[howMany - 1])) + 1)
    space = "{:<" + onespace + "s} {:>" + twospace + "d}"

    for x in range(howMany):
        print(space.format(str(x + 1) + ":", fibonacci[x]))


Print()

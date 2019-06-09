import sys
innerList = []


def Print():
    innerList = [line.strip() for line in open('output.txt')]
    for x in range(len(innerList)):
        print(str(x + 1) + ". " + innerList[x])


if len(sys.argv) == 2 and sys.argv[1] == "--list":
    Print()
    sys.exit()
elif len(sys.argv) == 3 and sys.argv[1] == "--delete":
    innerList = [line.strip() for line in open('output.txt')]
    index = int(sys.argv[2]) - 1
    innerList.pop(index)
    for x in range(len(innerList)):
        print(str(x + 1) + ". " + innerList[x])
    open('output.txt', 'w').close()
    f = open('output.txt', 'a')
    for x in range(len(innerList)):
        f.write(innerList[x] + "\n")
    f.close()
    sys.exit()


idea = input("What is your new idea: ")
f = open('output.txt', 'a')
f.write(idea + "\n")
f.close()
Print()

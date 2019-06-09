import sys


def isAnagram(x, y):
    listX = sorted(x)
    listY = sorted(y)
    return listX == listY


text = sys.argv[1]
anagramList = []
textList = []

read = open(text, 'r')
for x in read:
    textList.append(x.strip())

for x in range(len(textList)):
    for y in range(len(textList)):
        if x != y and isAnagram(textList[x], textList[y]):
            # fordított x és y kizárja a duplikációt
            temp = textList[y] + " " + textList[x]
            if any(x in temp for x in anagramList):
                continue
            else:
                anagramList.append(textList[x] + " " + textList[y])

for x in anagramList:
    print(x)

import sys

wordList = []
step = 1
while step < len(sys.argv):
    if len(str(sys.argv[step])) < 2 or any(x.isdigit() for x in str(sys.argv[step])):
        print("Use only verbs!")
        sys.exit()
    else:
        wordList.append(sys.argv[step])
        step += 1


def ppl(verb):
    verbList = list(verb)
    last = len(verbList) - 1
    secondLast = len(verbList) - 2
    vowels = ['a', 'e', 'i', 'o', 'u']
    if verbList[last] == "e":
        if verbList[secondLast] == "i":
            verbList.pop(last)
            verbList.pop(secondLast)
            verbList.append("ying")
        elif secondLast == 0 or verbList[secondLast] == "e":
            verbList.append("ing")
        else:
            verbList.pop(last)
            verbList.append("ing")
    elif len(verbList) > 2 and not any(x in verbList[last] for x in vowels) and any(x in verbList[secondLast] for x in vowels) and not any(x in verbList[secondLast - 1] for x in vowels):
        verbList.append(verbList[last])
        verbList.append("ing")
    else:
        verbList.append("ing")
    return verbList


for y in range(len(wordList)):
    for x in ppl(wordList[y]):
        print(x, end="")
    print()

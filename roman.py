oneDigit = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
twoDigit = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
threeDigit = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
fourDigit = ["M", "MM", "MMM"]
numberList = input("Enter arabic numbers(1-3999): ").split(" ")

for x in numberList:
    number = str(x)
    romanNumber = []
    for x in range(len(number)):
        if len(number) == 4 and int(number[x]) > 0:
            if x == 3:
                romanNumber.append(oneDigit[int(number[x]) - 1])
            elif x == 2:
                romanNumber.append(twoDigit[int(number[x]) - 1])
            elif x == 1:
                romanNumber.append(threeDigit[int(number[x]) - 1])
            elif x == 0:
                romanNumber.append(fourDigit[int(number[x]) - 1])
        elif len(number) == 3 and int(number[x]) > 0:
            if x == 2:
                romanNumber.append(oneDigit[int(number[x]) - 1])
            elif x == 1:
                romanNumber.append(twoDigit[int(number[x]) - 1])
            elif x == 0:
                romanNumber.append(threeDigit[int(number[x]) - 1])
        elif len(number) == 2 and int(number[x]) > 0:
            if x == 1:
                romanNumber.append(oneDigit[int(number[x]) - 1])
            elif x == 0:
                romanNumber.append(twoDigit[int(number[x]) - 1])
        elif len(number) == 1 and int(number[x]) > 0:
            romanNumber.append(oneDigit[int(number[x]) - 1])

    for x in romanNumber:
        print(x, end="")
    print()

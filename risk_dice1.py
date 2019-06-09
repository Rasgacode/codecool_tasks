import random
Atk = 0
Def = 0

while Atk <= 0 or Def <= 0 or Atk > 3 or Def > 2:
    try:
        Atk = int(input("Enter the number of the attacker units(1-3): "))
        Def = int(input("Enter the number of the deffender units(1-2): "))
    except ValueError:
        continue

atkList = []
defList = []

for item in range(Atk):
    atkList.append(random.randint(1, 6))

for item in range(Def):
    defList.append(random.randint(1, 6))

atkList.sort(reverse=True)
defList.sort(reverse=True)


def Print():
    print("Dice:")
    print("Attacker: ", end="")

    for item in range(Atk):
        if item == Atk - 1:
            print(atkList[item])
        else:
            print(str(atkList[item]) + "-", end="")

    print("Defender: ", end="")

    for item in range(Def):
        if item == Def - 1:
            print(defList[item])
        else:
            print(str(defList[item]) + "-", end="")

    forRange = 0
    atkLost = 0
    defLost = 0

    if len(defList) <= len(atkList):
        forRange = len(defList)
    else:
        forRange = len(atkList)

    for item in range(forRange):
        if atkList[item] > defList[item]:
            defLost += 1
        else:
            atkLost += 1

    print("")
    print("Outcome:")
    print("Attacker: Lost " + str(atkLost) + " unit(s)")
    print("Defender: Lost " + str(defLost) + " unit(s)")


Print()

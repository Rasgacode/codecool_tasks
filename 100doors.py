hundredDoors = []
for x in range(100):
    hundredDoors.append("closed")

for x in range(1,101,1):
    for y in range(1,101,x):
        if hundredDoors[y-1] == "closed":
            hundredDoors[y-1] = "open"
        else:
            hundredDoors[y-1] = "closed"

print("The following doors are open: ", end = "")
for x in range(len(hundredDoors)):
    if hundredDoors[x] == "open":
        print(x, end = ", ")
    if x == 99:
        print()
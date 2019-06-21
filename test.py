foo = 0
lol = [[1 for i in range(4)] for j in range(4)]
if any([[x == 0 for x in y] for y in lol]):
    print(lol)
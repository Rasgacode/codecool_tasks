step = 0
for x in range(999, 100, -1):
    if x % 7 == 0 and x % 9 == 0 and step < 25:
        print(x)
        step += 1

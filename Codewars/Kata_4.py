lol = 667
def binaris(n):
    return sum(int(x) for x in list(format(n, "b")))

print(binaris(lol))
import random

def match():
    home = []
    away = []
    for x in range(6):
        n = random.randint(1,6)
        if x < 3:
            home.append(n)
        else:
            away.append(n)
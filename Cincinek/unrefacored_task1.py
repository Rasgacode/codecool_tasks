import random

w = ["experience", "honor", "justice", "sacrefice", "scar", "wisdom", "might", "dragon", "knight"]
i_c = []
g = []
r_n = random.randint(0, len(w) - 1)
picked = w[r_n]
for x in range(len(picked)):
    g.append("_")
while(True):
    while(True):
        in_ = input("Enter a letter: ")
        if len(in_) != 1 or any(c.isdigit() for c in in_):
            print("Wrong input!")
            continue
        if len(in_) == 1:
            break
    if in_ in picked:
        for i, letter in enumerate(picked):
            if in_ == letter:
                g[i] = letter
    elif in_ not in i_c:
        i_c.append(in_)
    s = ""
    for x in g:
        s += x
    print(f"There are your found letters: {s}\nThere are your missed letters: {i_c}")
    if "_" not in g:
        print("You have guessed the word!")
        break

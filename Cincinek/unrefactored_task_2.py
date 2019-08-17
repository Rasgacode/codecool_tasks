import string
import random


l= ["postreme", "Verminology", "Palaeophile", "zegedine", "flammulated", "keckle", "Individualism",
"viaggiatory", "Dashpot", "Mecometer", "Zug", "orismology", "beatus", "Unicorn", "Latitudinous"]


while(True):
    try:
        i = input("Enter a letter: ")
        if len(i) > 1:
            print("Wrong input!")
            raise ValueError
        if len(i) < 1:
            print("Wrong input!")
            raise ValueError
        if any(x.isdigit() for x in i):
            print("Wrong input!")
            raise ValueError
    except ValueError:
        
        continue
    else:
        break
n_l = []
n_l_2 = []
for y in l:
    i = i.lower()
    f_letter = y[0].lower()
    if i!=f_letter:
        n_l_2.append(y)
    if i == f_letter:
        n_l.append(y)
if len(n_l) > 0 and len(n_l)!= 0:
    print("Your input match with these words first letter --> ", end="") 
    print(n_l)
elif len(n_l) == 0 or len(n_l) < 0:
    print("Your input match with 0 word")
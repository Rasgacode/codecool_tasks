print("Enter 6 integer(3 coordinates x,y), use only numbers(-100 - 100)!")

while True:
    try:
        ax = int(input("Enter a=>x[value]: "))
        ay = int(input("Enter a=>y[value]: "))
        bx = int(input("Enter b=>x[value]: "))
        by = int(input("Enter b=>y[value]: "))
        cx = int(input("Enter c=>x[value]: "))
        cy = int(input("Enter c=>y[value]: "))
    except ValueError:
        print("Please use only numbers!")
        continue
    if ax < -100 or ay < -100 or bx < -100 or by < -100 or cx < -100 or cy < -100 \
            or ax > 100 or ay > 100 or bx > 100 or by > 100 or cx > 100 or cy > 100: # min(ax, ay, bx, by) < -100
        print("One of your numbers was out of range!")
        continue
    break


def area():
    import math
    A = math.sqrt(((bx - ax)**2) + ((by - ay)**2))
    B = math.sqrt(((bx - cx)**2) + ((by - cy)**2))
    C = math.sqrt(((cx - ax)**2) + ((cy - ay)**2))
    S = 0.5 * (A + B + C)
    Area = math.sqrt(S * (S - A) * (S - B) * (S - C))
    print("Area of the triangle:", round(Area, 1))


area()

import sys


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


if len(sys.argv) == 3:
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except BaseException:
        print("You did something wrong!")
        sys.exit()
    print("The gcd of " + str(x) + " and " +
          str(y) + " is : " + str(gcd(x, y)))
else:
    print("You did something wrong!")

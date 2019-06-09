import sys

for arg in sys.argv:
    if len(sys.argv) == 1:
        print("Hello World!")
    else:
        print("Hello "+sys.argv[1]+"!")
        break

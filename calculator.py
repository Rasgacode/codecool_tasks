while True:
    try:
        num1 = int(input("Enter a number: "))
        op = str(input("Enter an operation: "))
        num2 = int(input("Enter a number: "))
    except ValueError:
        continue
    break
if op == "+":
    print("Result: {}".format(num1 + num2))
if op == "-":
    print("Result: {}".format(num1 - num2))
if op == "*":
    print("Result: {}".format(num1 * num2))
if op == "/":
    print("Result: {}".format(num1 / num2))
else:
    SystemExit

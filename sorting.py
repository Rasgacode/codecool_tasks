while True:
    numbers = input(
        "Enter the elements of the list, split the NUMBERS with space: ").split(" ")
    if all(item.isdigit() for item in numbers):
        print("Numbers in the list:")
        for x in numbers:
            print(x, end=" ")
        print()
        break
    else:
        print("Use only numbers pls!")
        continue

for y in range(len(numbers) - 1):
    for x in range(len(numbers) - 1):
        if int(numbers[x]) > int(numbers[x + 1]):
            temp = numbers[x + 1]
            numbers[x + 1] = numbers[x]
            numbers[x] = temp

print("Numbers in order:")
for x in numbers:
    print(x, end=" ")
print()

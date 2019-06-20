import test
numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

for x in range(len(numbers)):
    for y in range(len(numbers)):
        if numbers[x] > numbers[y]:
            temp = numbers[x]
            numbers[x] = numbers[y]
            numbers[y] = temp
print(numbers[0])
print(numbers[len(numbers)-1])

test.test()

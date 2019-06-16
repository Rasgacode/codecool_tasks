board = [[1, 2, 3, 4], 
         [5, 6, 7 ,8], 
         [9, 10, 11, 12],
         [13, 14, 15, 16]
         ]
print(board)
rotated = []
temp = list(zip(*board[::-1]))
for x in temp:
    rotated.append(list(x))
board.clear()
print(rotated)
temp.clear()
temp = list(zip(*rotated))
temp = temp[::-1]
for x in temp:
    board.append(list(x))
print(board)


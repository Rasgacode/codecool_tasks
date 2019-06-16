import random
boarBlocks = []
board = []
for x in range(9):
    board.append([])
    for y in range(9):
        board[x].append(True)

def randomBoardGen(board):

    randomX = random.randint(0,8)
    randomY = random.randint(0,8)


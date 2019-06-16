import os, time, random

redX = "\033[91mx\033[00m"
greenO = "\033[92mo\033[00m"

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]  #list(range(9))
winnerPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
gameOver = 0


def Print():
    dash = "-"*7
    divider = "|"

    for x in range(len(board)):
        if x == 0:
            print(dash)
        print(divider + str(board[x]), end="")
        if x == 2 or x == 5 or x == 8:
            print("|")
            print(dash)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')  

def userInput(board):
    while(True):
        try:
            enterNum = int(input("Please enter the number: "))
        except ValueError:
            print("Use only numbers please!")
            continue
        if enterNum not in board:
            print("Invalid position!")
            continue
        elif board[enterNum] == redX or board[enterNum] == greenO:
            print("That position is already taken!")
            continue
        else:
            board[enterNum] = redX
            break

def winnerPosition(board, winnerPositions): 
    global gameOver 
    for x in range(len(winnerPositions)):
        listInList = winnerPositions[x] 
#    for listInList in winnerPositions:
        if board[listInList[0]] == redX and board[listInList[1]] == redX and board[listInList[2]] == redX:
            gameOver = 1
            break
        if board[listInList[0]] == greenO and board[listInList[1]] == greenO and board[listInList[2]] == greenO:
            gameOver = 2
            break
    if gameOver == 1: 
        print("Congratulations, you won!")       
    elif gameOver == 2: 
        print("Game Over! The computer won!")
    elif board.count(redX) == 5:
        gameOver = 3
        print("It's a tie!")

# 1. Could the next move be a winner position for AI? 
# 2. Could the AI prevent us from winning? 
# 3. AI should be able to beat the user (to recognize the possibility of a second O)

def AI(board, winnerPositions):
    time.sleep(.500)
    marker = 0
    #1
    for x in range(len(winnerPositions)): 
        temp = winnerPositions[x]
        if board[temp[0]] == board[temp[1]] and board[temp[0]] == greenO and board[temp[2]] != redX: 
            board[temp[2]] = greenO 
            marker = 1
            break
        elif board[temp[0]] == board[temp[2]] and board[temp[0]] == greenO and board[temp[1]] != redX: 
            board[temp[1]] = greenO
            marker = 1
            break
        elif board[temp[1]] == board[temp[2]] and board[temp[1]] == greenO and board[temp[0]] != redX: 
            board[temp[0]] = greenO
            marker = 1
            break
        #2 
    if marker == 0:   
        for x in range(len(winnerPositions)): 
            temp = winnerPositions[x]
            if board[temp[0]] == board[temp[1]] and board[temp[0]] == redX and board[temp[2]] != greenO: 
                board[temp[2]] = greenO
                marker = 1 
                break
            elif board[temp[0]] == board[temp[2]] and board[temp[0]] == redX and board[temp[1]] != greenO: 
                board[temp[1]] = greenO
                marker = 1
                break
            elif board[temp[1]] == board[temp[2]] and board[temp[1]] == redX and board[temp[0]] != greenO: 
                board[temp[0]] = greenO
                marker = 1
                break
    
    #3 findOs 
    if marker == 0: 
        for x in range(len(winnerPositions)): 
            temp = winnerPositions[x] 
            if board[temp[0]] == greenO and board[temp[1]] != redX and board[temp[2]] != redX:
                board[temp[1]] = greenO
                marker = 1
                break
            elif board[temp[1]] == greenO and board[temp[0]] != redX and board[temp[2]] != redX: 
                board[temp[2]] = greenO
                marker = 1
                break
            elif board[temp[2]] == greenO and board[temp[0]] != redX and board[temp[1]] != redX: 
                board[temp[0]] = greenO
                marker = 1
                break

        #random
    if marker == 0: 
        while(True):
            randomNum = random.randint(0, 8)
            if board[randomNum] == redX or board[randomNum] == greenO: 
                continue
            else: 
                board[randomNum] = greenO
                break

def replay(): 
    dash = "-"*7
    divider = "|"

    for x in range(len(board)):
        if x == 0:
            print(dash)
        print(divider + str(board[x]), end="")
        if x == 2 or x == 5 or x == 8:
            print("|")
            print(dash)   

def main(board): 
    global gameOver
    while(True): 
        cls()
        Print()
        userInput(board)
        cls()
        Print()
        winnerPosition(board, winnerPositions)
        if gameOver == 1 or gameOver == 3:
            break
        AI(board, winnerPositions)
        cls()
        Print()
        winnerPosition(board, winnerPositions)
        if gameOver == 2 or gameOver == 3:
            break

    replayRequest = input("Do you want to play another round? (y/n):")
    
    if replayRequest == "y": 
        for x in range(len(board)): 
            board[x] = x 
        gameOver = 0
        return main(board)
    

if __name__ == "__main__":
    main(board)

    

    
    
         


    
    
    
      



  


board = ['-' for _ in range(9)]

def showBoard():
    print(f"\n | {board[0]} | {board[1]} | {board[2]} |\n")
    print(f" | {board[3]} | {board[4]} | {board[5]} |\n")
    print(f" | {board[6]} | {board[7]} | {board[8]} |\n")

def move(position,symbol):
   if board[position - 1] == "-":
       board[position - 1] = symbol
       showBoard()
       return True
   elif board[position - 1] == "O" or board[position - 1] ==  "X":
       print("Invalid move\n")
       return False
def checkResult():
    if ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or
        (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or
        (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or
        (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or
        (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or
        (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or
        (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or
        (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        print("Player X win")
        return True
    elif ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or
          (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or
          (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or
          (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or
          (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or
          (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or
          (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or
          (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        print("Player O win")
        return True
    elif (board[0] != '-' and board[1] != '-' and board[2] != '-' and
          board[3] != '-' and board[4] != '-' and board[5] != '-' and
          board[6] != '-' and board[7] != '-' and board[8] != '-'):
        print("Draw")
        return True
    else:
        return False
def ticTacToeGame():
    showBoard()
    symbol = "X"
    while not checkResult():
        try:
            position = int(input(f"Player {symbol}, enter position 1-9: "))
            while position < 1 or position > 9:
                print("Invalid position. Enter a number between 1 and 9.")
                position = int(input(f"Player {symbol}, enter position 1-9: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if move(position, symbol):
            symbol = "O" if symbol == "X" else "X"

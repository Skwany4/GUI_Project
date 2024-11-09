import numpy as np
import tkinter
import customtkinter

class Connect4(tkinter.Frame):
    def __init__(self, app):
        super().__init__(app.tk)
        self.app = app


def createBoard():
    return np.full((6,7),"-")

def playerMove(board,row, col, symbol):
    board[row][col] = symbol

def checkMove(board,col):
    if 6 >= col >= 0  and board[0][col] == "-":
        return True
    else:
        return False
def move(board,col,symbol):
    if checkMove(board,col):
        for row in range(len(board)-1,-1,-1):
            if board[row][col] == '-':
                playerMove(board,row,col,symbol)
                return row

    return None

def checkWin(board, row, col, symbol):
    return (checkDirection(board, row, col, symbol, 1, 0) or  # Poziomo
            checkDirection(board, row, col, symbol, 0, 1) or  # Pionowo
            checkDirection(board, row, col, symbol, 1, 1) or  # Ukośnie w dół
            checkDirection(board, row, col, symbol, 1, -1))   # Ukośnie w górę

def checkDirection(board, row, col, symbol, delta_row, delta_col):
    count = 0
    for i in range(-3, 4):
        r = row + i * delta_row
        c = col + i * delta_col
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == symbol:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


def connect4Game():
    board = createBoard()
    game_over = False
    current_player = "X"

    while not game_over:
        print(board)
        col = int(input(f"Player {current_player}, choose a column (0-6): "))

        if not checkMove(board, col):
            print("Invalid move. Try again.")
            continue

        row = move(board, col, current_player)
        if row is not None:
            if checkWin(board, row, col, current_player):
                print(board)
                print(f"Player {current_player} wins!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Column is full. Try a different column.")

        if "-" not in board:
            print("It's a draw!")
            game_over = True


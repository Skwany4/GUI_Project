import numpy as np

def createBoard():
    return np.full((6,7),"-")

def playerMove(board,row, col, symbol):
    board[row][col] = symbol

def checkMove(board,col):
    if 6 >= col >= 0:
        return True
    else:
        return False

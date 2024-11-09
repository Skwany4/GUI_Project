import random

board = ["Rock", "Scissors", "Paper"]

def pMove():
    while True:
        try:
            playerMove = int(input("Rock - 1, Scissors - 2, Paper - 3: ")) - 1
            if playerMove in [0, 1, 2]:
                return playerMove  # Return the index instead of the string
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def cMove():
    computerMove = random.randint(0, 2)
    return computerMove  # Return the index

def results(playerMove, computerMove):
    if playerMove == computerMove:
        print("Draw")
        return 0, 0
    elif (playerMove == 0 and computerMove == 1) or \
         (playerMove == 1 and computerMove == 2) or \
         (playerMove == 2 and computerMove == 0):
        print("Player wins this round!")
        return 1, 0
    else:
        print("Computer wins this round!")
        return 0, 1

def win(playerScore, computerScore):
    if playerScore == 3:
        print("Player wins the game!")
        return True
    elif computerScore == 3:
        print("Computer wins the game!")
        return True
    return False

def rockScissorsPaperGame():
    playerScore = 0
    computerScore = 0
    while not win(playerScore, computerScore):
        playerMove = pMove()
        computerMove = cMove()
        print(f"Player chose: {board[playerMove]}, Computer chose: {board[computerMove]}")

        playerPoint, computerPoint = results(playerMove, computerMove)
        playerScore += playerPoint
        computerScore += computerPoint
        print(f"Score -> Player: {playerScore}, Computer: {computerScore}\n")

rockScissorsPaperGame()

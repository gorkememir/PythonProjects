#Create an empty game board
plane = ["  " for i in range(0,9)]

#Print the current state of the game board
def printBoard():

    row1list = [plane[x] for x in range(0,3)]
    row2list = [plane[x] for x in range(3,6)]
    row3list = [plane[x] for x in range(6,9)]

    row1 = ("| {} | {} | {} |").format(*row1list)
    row2 = ("| {} | {} | {} |").format(*row2list)
    row3 = ("| {} | {} | {} |").format(*row3list)

    print(" ")
    print(row1)
    print(row2)
    print(row3)
    print(" ")

#Take input from the player who has the turn, update the board. If player wants to play on a filled spot,
# get angry and waste his turn.
def playerMove(icon):

    if icon == "X":
        playerNumber = 1
    elif icon == "O":
        playerNumber = 2

    playerTurn = "Player {}'s Turn!".format(playerNumber)
    print(playerTurn)

    playerChoice = int(input("Where would you like to put your thingy? (1-9): ").strip())
    if plane[playerChoice - 1] == "  ":
        plane[playerChoice - 1] = icon
    else:
        print()
        print("Are you kidding me?")

#Check if we have a winner, if yes, print who won the game and end.
def winnerCheck(icon):
    if (plane[0] == icon and plane[1] == icon and plane[2] == icon) or \
        (plane[3] == icon and plane[4] == icon and plane[5] == icon) or \
        (plane[6] == icon and plane[7] == icon and plane[8] == icon) or \
        (plane[0] == icon and plane[3] == icon and plane[6] == icon) or \
        (plane[1] == icon and plane[4] == icon and plane[7] == icon) or \
        (plane[2] == icon and plane[5] == icon and plane[8] == icon) or \
        (plane[0] == icon and plane[4] == icon and plane[8] == icon) or \
        (plane[2] == icon and plane[4] == icon and plane[6] == icon):
        return True
    else:
        return False

#Check if we have a draw, if yes, print it and end the game.
def drawCheck():
    if "  " not in plane:
        return True
    else:
        return False

#Game loop starts here
while True:
    #Print the current board
    printBoard()

    #Take input from player 1, check if the game is over.
    playerMove("X")
    if winnerCheck("X"):
        print("Player 1 WINS!")
        break
    elif drawCheck():
        print("It is a draw!")
        break
    printBoard()

    #Take input from player 2, check if the game is over.
    playerMove("O")
    if winnerCheck("O"):
        print("Player 2 WINS!")
        break
    elif drawCheck():
        print("It is a draw!")
        break



from random import randint 
from GameBoard import GameBoard

board = GameBoard()

def drawGame():
	print("   1   2   3 ")
	print("a  " + board.get(0, 0) + " | " + board.get(0, 1) + " | " + board.get(0, 2))
	print("  -----------")
	print("b  " + board.get(1, 0) + " | " + board.get(1, 1) + " | " + board.get(1, 2))
	print("  -----------")
	print("c  " + board.get(2, 0) + " | " + board.get(2, 1) + " | " + board.get(2, 2))

def getAndValidateMove():
	move = input("Where would you like to play? (eg. a1)\n>")

	if len(move) != 2:
		print("Invalid Move!")
		return getAndValidateMove()

	row = 0
	if move[0] == 'a':
		row = 0
	elif move[0] == 'b':
		row = 1
	elif move[0] == 'c':
		row = 2
	else:
		print("Invalid Move!")
		return getAndValidateMove()

	if move[1] != '1' and move[1] != '2' and move[1] != '3':
		print("Invalid Move!")
		return getAndValidateMove()

	col = int(move[1]) - 1
	if board.get(row, col) != ' ':
		print("That spot is taken!")
		return getAndValidateMove()

	return (row, col)


def getWinningSpots(symbol):	
	winningSpots = []

	for i in range(3):
		for j in range(3):
			if board.get(i, j) != ' ':
				continue

			#Check if horizontal
			if board.get(i, j-1) == symbol and board.get(i, j-2) == symbol:
				winningSpots.append((i, j))

			if board.get(i, j-1) == symbol and board.get(i, j+1) == symbol:
				winningSpots.append((i, j))

			if board.get(i, j+1) == symbol and board.get(i, j+2) == symbol:
				winningSpots.append((i, j))

			#check if vertical
			if board.get(i-1, j) == symbol and board.get(i-2, j) == symbol:
				winningSpots.append((i, j))

			if board.get(i-1, j) == symbol and board.get(i+1, j) == symbol:
				winningSpots.append((i, j))

			if board.get(i+1, j) == symbol and board.get(i+2, j) == symbol:
				winningSpots.append((i, j))

			#Check if diagonal topLeft-BottomRight
			if board.get(i-1, j-1) == symbol and board.get(i-2, j-2) == symbol:
				winningSpots.append((i, j))

			if board.get(i-1, j-1) == symbol and board.get(i+1, j+1) == symbol:
				winningSpots.append((i, j))

			if board.get(i+1, j+1) == symbol and board.get(i+2, j+2) == symbol:
				winningSpots.append((i, j))

			#Check if Diagonal bottomLeft-TopRight
			if board.get(i-1, j+1) == symbol and board.get(i-2, j+2) == symbol:
				winningSpots.append((i, j))

			if board.get(i+1, j-1) == symbol and board.get(i-1, j+1) == symbol:
				winningSpots.append((i, j))

			if board.get(i+1, j-1) == symbol and board.get(i+2, j-2) == symbol:
				winningSpots.append((i, j))

	return winningSpots;

def mainLoop():

	print("Welcome to tictactoe!\n")

	xo = ""
	while xo != 'x' and xo != 'o':
		xo = input("Would you like to be X's (x) or O's (o)?\n>")

	if xo == 'x':
		compSymb = 'o'
	else:
		compSymb = 'x'

	drawGame()

	playerWinningSpots = []
	for i in range(5):

		move = getAndValidateMove()
		board.set(move[0], move[1], xo)

		drawGame()

		for spot in playerWinningSpots:
			if spot == move:
				print("You Win!")
				return

		playerWinningSpots = getWinningSpots(xo)
		computerWinningSpots = getWinningSpots(compSymb)
		if len(computerWinningSpots) > 0:
			board.set(computerWinningSpots[0][0], computerWinningSpots[0][1], compSymb)
			drawGame()
			print("You Lose!")
			return
		elif len(playerWinningSpots) > 0:
			board.set(playerWinningSpots[0][0], playerWinningSpots[0][1], compSymb)
			drawGame()
		elif i != 4:
			while True:
				rand = randint(0, 8)
				x = int(rand/3)
				y = rand%3
				if board.get(x, y) == ' ':
					board.set(x, y, compSymb)
					break

			drawGame()

	print("Tie Game!")
	return

mainLoop()

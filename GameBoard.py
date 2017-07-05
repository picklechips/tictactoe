class GameBoard:
	__board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

	def get(self, x, y):
		if x < 0 or x > 2 or y < 0 or y > 2:
			return "null"
		else:
			return self.__board[x][y]

	def set(self, x, y, val):
		if x < 0 or x > 2 or y < 0 or y > 2:
			print("ERROR: Board index setting out of range")
		else:
			self.__board[x][y] = val


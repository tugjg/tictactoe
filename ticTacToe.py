theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '} # dictionary of the tic tac toe board

def printBoard(board): # draws the tic tac toe board on the screen
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def moveMaker(turn): # fills in the space selected by the user whose turn it is
	move = input("Enter a space on the grid for your " +turn+ " mark to be placed.")
	theBoard[move] = turn
	return move

def moveChecker(move): # checks to see if the space is already filled by another piece
	if theBoard.get(move) == 'X':
		print("This space is filled with an X. Please pick a different space!")
		return False
	elif theBoard.get(move) == 'O':
		print("This space is already filled with an O. Please try a different space!")
		return False
	else:
		print("Move is a success!")
		return True

def winningCombos(): # deteremines if either user X or user Y has achieved a winning combination
	# X possibilities vertical
	if (((theBoard['top-L'] == 'X') and (theBoard['mid-L'] == 'X') and (theBoard['low-L'] == 'X')) or ((theBoard['top-M'] == 'X') and (theBoard['mid-M'] == 'X') and (theBoard['low-M'] == 'X')) or ((theBoard['top-M'] == 'X') and (theBoard['mid-R'] == 'X') and (theBoard['low-R'] == 'X'))):
		return True
	# Y possibilities vertical'
	if (((theBoard['top-L'] == 'Y') and (theBoard['mid-L'] == 'Y') and (theBoard['low-L'] == 'Y')) or ((theBoard['top-M'] == 'Y') and (theBoard['mid-M'] == 'Y') and (theBoard['low-M'] == 'Y')) or ((theBoard['top-M'] == 'Y') and (theBoard['mid-R'] == 'Y') and (theBoard['low-R'] == 'Y'))):
		return True
	# X possibilities horizontal
	if (((theBoard['top-L'] == 'X') and (theBoard['top-M']== 'X') and (theBoard['top-R'] == 'X')) or ((theBoard['mid-L'] == 'X') and (theBoard['mid-M']== 'X') and (theBoard['mid-R'] == 'X')) or ((theBoard['low-L'] == 'X') and (theBoard['low-M'] == 'X') and (theBoard['low-R'] == 'X'))):
		return True
	# Y possibilities  horizontal
	if (((theBoard['top-L'] == 'Y') and (theBoard['top-M']== 'Y') and (theBoard['top-R'] == 'Y')) or ((theBoard['mid-L'] == 'Y') and (theBoard['mid-M']== 'Y') and (theBoard['mid-R'] == 'Y')) or ((theBoard['low-L'] == 'Y') and (theBoard['low-M'] =='Y') and (theBoard['low-R'] == 'Y'))):
		return True
	# X possibilities diagonal
	if (((theBoard['top-L'] == 'X') and (theBoard['mid-M'] == 'X') and (theBoard['low-R'] == 'X')) or ((theBoard['top-R'] == 'X') and (theBoard['mid-M'] == 'X') and (theBoard['low-L'] == 'X'))):
		return True
	# Y possibilities diagonal
	if (((theBoard['top-L'] == 'Y') and (theBoard['mid-M'] == 'Y') and (theBoard['low-R'] == 'Y')) or ((theBoard['top-R'] == 'Y') and (theBoard['mid-M'] == 'Y') and (theBoard['low-L'] == 'Y'))):
		return True
	else:
		return False

def turnSwitcher(turn):
	if turn == 'X':
		turn =  'O'
	else:
		turn  = 'X'
	return turn


def main():
	print("Welcome to Tic Tac Toe")
	printBoard(theBoard)
	turn = 'X'
	winner = ''
	move = ''
	while winningCombos() is False:
		print('It is ' +turn+ ' \'s turn. Enter a place to move. Options: top-L, mid-M, low-R, etc..') # instructions
		while moveChecker(move) is True:
			winningCombos()
			moveMaker(turn) # calls the function to place the appropriate marker
			moveChecker(move)
			printBoard(theBoard) # prints the newly marked board
			turn = turnSwitcher(turn)
		else:
			winningCombos()
			moveMaker(turn)
			moveChecker(move)
			printBoard(theBoard)




main()




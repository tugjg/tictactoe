theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '} # dictionary of the tic tac toe board

def printBoard(board): # draws the tic tac toe board on the screen
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])





def moveSelector(turn): # fills in the space selected by the user whose turn it is
	move = input("Enter a space on the grid to place your " +turn+ " mark.")
	if theBoard.get(move) == 'X' or theBoard.get(move) == 'O':
		print("This space is filled, please pick a different space!")
	else:
		theBoard[move] = turn    




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
	"""
	1. Print an empty board to show the user how it looks. Brief printed introduction.
	2. while winningCombos is not X or not O...
		a: Let the player whose turn it is choose where to place their symbol.
		b: Ensure that the space is not already filled. If it is, let them place it again.
		c: Print the board showing where the X or O has been successfully filled in.
	3. Print a message declaring who the winner is from threeInARow!
	"""

	print("Welcome to Tic Tac Toe")
	printBoard(theBoard)
	turn = ''
	winner = ''
	while winningCombos() is False:
		winningCombos()
		turn = turnSwitcher(turn)
		print('It is ' +turn+ ' \'s turn. Enter a place to move. Options: top-L, mid-M, low-R, etc..')
		moveSelector(turn)
		printBoard(theBoard)







main()





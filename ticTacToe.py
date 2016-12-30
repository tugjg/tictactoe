theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '} # dictionary of the tic tac toe board

def printBoard(board): # draws the tic tac toe board on the screen
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def mover(turn, move):
	move = input("Enter a space on the grid for your " +turn+ " mark to be placed. \n")
	print("")
	if not (theBoard.get(move) == 'X' or theBoard.get(move) == 'O'):
		theBoard[move] = turn
		printBoard(theBoard)
		turnSwitcher(turn)
	else:
		print("The space" +move+ " is filled with a " +turn+ " already. Please try again!")
		mover(turn, move)

def winningCombos(): # deteremines if either user X or user Y has achieved a winning combination
	# X possibilities vertical
	if (((theBoard['top-L'] == 'X') and (theBoard['mid-L'] == 'X') and (theBoard['low-L'] == 'X')) or ((theBoard['top-M'] == 'X') and (theBoard['mid-M'] == 'X') and (theBoard['low-M'] == 'X')) or ((theBoard['top-M'] == 'X') and (theBoard['mid-R'] == 'X') and (theBoard['low-R'] == 'X'))):
		print('The winner is X!')
		return True
	# Y possibilities vertical'
	if (((theBoard['top-L'] == 'Y') and (theBoard['mid-L'] == 'Y') and (theBoard['low-L'] == 'Y')) or ((theBoard['top-M'] == 'Y') and (theBoard['mid-M'] == 'Y') and (theBoard['low-M'] == 'Y')) or ((theBoard['top-M'] == 'Y') and (theBoard['mid-R'] == 'Y') and (theBoard['low-R'] == 'Y'))):
		print('The winner is O!')
		return True
	# X possibilities horizontal
	if (((theBoard['top-L'] == 'X') and (theBoard['top-M']== 'X') and (theBoard['top-R'] == 'X')) or ((theBoard['mid-L'] == 'X') and (theBoard['mid-M']== 'X') and (theBoard['mid-R'] == 'X')) or ((theBoard['low-L'] == 'X') and (theBoard['low-M'] == 'X') and (theBoard['low-R'] == 'X'))):
		print('The winner is X!')
		return True
	# Y possibilities  horizontal
	if (((theBoard['top-L'] == 'Y') and (theBoard['top-M']== 'Y') and (theBoard['top-R'] == 'Y')) or ((theBoard['mid-L'] == 'Y') and (theBoard['mid-M']== 'Y') and (theBoard['mid-R'] == 'Y')) or ((theBoard['low-L'] == 'Y') and (theBoard['low-M'] =='Y') and (theBoard['low-R'] == 'Y'))):
		print('The winner is O!')
		return True
	# X possibilities diagonal
	if (((theBoard['top-L'] == 'X') and (theBoard['mid-M'] == 'X') and (theBoard['low-R'] == 'X')) or ((theBoard['top-R'] == 'X') and (theBoard['mid-M'] == 'X') and (theBoard['low-L'] == 'X'))):
		print('The winner is X!')
		return True
	# Y possibilities diagonal
	if (((theBoard['top-L'] == 'Y') and (theBoard['mid-M'] == 'Y') and (theBoard['low-R'] == 'Y')) or ((theBoard['top-R'] == 'Y') and (theBoard['mid-M'] == 'Y') and (theBoard['low-L'] == 'Y'))):
		print('The winner is O!')
		return True
	else:
		return False

def turnSwitcher(turn):
	if turn == 'X':
		turn =  'O'
	else:
		turn  = 'X'
	return turn

def switchTheTurn(switchIt, turn):
	if switchIt is True:
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
			
	if switchIt is False:
		turn = turn
	return turn
		
							
def main():
	print("Welcome to TIc Tac Toe!")
	printBoard(theBoard)
	turn = 'X'
	while not winningCombos() is True:
		move = ''
		move = input("Enter a space on the grid for your " +turn+ " mark to be placed. \n")
		print("")

		if not (theBoard.get(move) == 'X' or theBoard.get(move) == 'O'):
			theBoard[move] = turn
			printBoard(theBoard)
			switchIt = True
			
		else:
			print("The space " +move+ " is filled with a " +turn+ " already. Please try again!")
			switchIt = False

		turn = switchTheTurn(switchIt, turn)
			

main()




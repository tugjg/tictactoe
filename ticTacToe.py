theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def turnSwitcher():
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'


"""def moveSelector():
	printBoard(theBoard)
	print('Turn for ' +turn+ '. Move on which space?')
	move = input()
	if theBoard.get(move) == 'X' or theBoard.get(move) == 'O':
		print("This space is filled, please pick a different space!")
	theBoard[move] = turn    
	printBoard(theBoard)
	turnSwitcher()"""

def winningCombos():
	winner = False
	while winner not True:
		#X possibilities vertical
		if (((theBoard(top-L) == X) and (theBoard(mid-L) == X) and (theBoard(low-L) == X)) or ((theBoard(top-M) == X) and (theBoard(mid-M) == X) and (theBoard(low-M) == X)) or ((theBoard(top-M) == X) and (theBoard(mid-R) == X) and (theBoard(low-R) == X))):
			winner = True
		#Y possibilities vertical
		if (((theBoard(top-L) == Y) and (theBoard(mid-L) == Y) and (theBoard(low-L) == Y)) or ((theBoard(top-M) == Y) and (theBoard(mid-M) == Y) and (theBoard(low-M) == Y)) or ((theBoard(top-M) == Y) and (theBoard(mid-R) == Y) and (theBoard(low-R) == Y))):
			winner = True
		#X possibilities horizontal
		if (theBoard(top-L) == X and theBoard(top-M)==X and theBoard(top-R) == X) or (theBoard(mid-L) == X and theBoard(mid-M)==X and theBoard(mid-R) == X) or (theBoard(low-L) == X and theBoard(low-M)==X and theBoard(low-R) == X):
			winner = True
		#Y possibilities  horizontal
		if (theBoard(top-L) == Y and theBoard(top-M)==Y and theBoard(top-R) == Y) or (theBoard(mid-L) == Y and theBoard(mid-M)==Y and theBoard(mid-R) == Y) or (theBoard(low-L) == Y and theBoard(low-M)==Y and theBoard(low-R) == Y):
			winner = True
		#X possibilities 

		

def main():
	printBoard(theBoard)
	turn = 'X'
	for i in range(9):
		move = input('Turn for' +turn+ '. Move on which space?')
		if theBoard.get(move) == 'X' or theBoard.get(move) == 'O':
			print("This space is filled, please pick a different space!")
		else:
			theBoard[move] = turn #fills in the "move" tic tac toe space with the appropriate turn character
			turnSwitcher()
		printBoard(theBoard)
		

	

main()





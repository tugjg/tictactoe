This project originated with some code from a small excercise in Automate the Boring Stuff.
 -------------------------
Original Code:
 theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '
   ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

   def printBoard(board):
       print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
       print('-+-+-')
       print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
       print('-+-+-')
       print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
   turn = 'X'
   for i in range(9):
	printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
   printBoard(theBoard)
 -------------------------

I wanted to attempt to make a full and complete working Tic Tac Toe game using some knowledge from 
a Python class I had taken the Fall of 2016.

Some help through Python IRC's was acquired for understanding the way subfunctions and their input parameters can be called into main function, and examples were provided to further my understanding in that area. Other than that, I wanted to challenge myself to see how much I could get done on my own. This is what I have so far, and I plan to work on this further in the future using more skills I acquire.

12/30/2016

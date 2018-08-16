import random
import numpy as np
import nn as nn

#draw the board in a 3x3 grid
def draw(b):
	i = 0
	for x in b:
		if  i%3 == 0 and i != 0:
			print()
			
		print("[" + str(x) + "]", end = "")
		i += 1
	print()
			
board = [" "] * 9
counter = 0
inx = True
won = False	
draw(board)
				   
while not won:
	try:
		#alternate x and o players and recieve user input
		if inx == True:
			position = int(input(">>>:X "))
			if board[position-1] != ' ':
				print("Invalid input")
				continue
			board[position-1] = "X" 
			draw(board)
			inx = not inx
			counter = counter + 1
		else:
			position = nn.process(board) #random.randint(1,9) #random number generator for player o
			print(">>>:O ")
			if board[position-1] != ' ':
				print("Invalid position") 
				# if we've got to here, the AI is styupid and gonna keep picking the same invalid value
				# the following code sets the output to the first index 
				# and keeps adding 1 until a valid move is played (h4cky af)
				position = 0 
				while board[position-1] != ' ':
					position = position + 1
					if counter == 9:
						break
				# the code above is hacky and a temporary fix - remove later and uncomment the below line
				#continue
			board[position-1] = "O" 
			draw(board)
			inx = not inx
			counter = counter + 1
			
		
		#win conditions
		if (board[0] == board[4] == board[8] != " ") or \
		   (board[2] == board[4] == board[6] != " ") or \
		   (board[0] == board[1] == board[2] != " ") or \
		   (board[3] == board[4] == board[5] != " ") or \
		   (board[6] == board[7] == board[8] != " ") or \
		   (board[0] == board[3] == board[6] != " ") or \
		   (board[1] == board[4] == board[7] != " ") or \
		   (board[2] == board[5] == board[8] != " "):
			print('Game over')
			won = True
			continue
	except:
		print("Invalid input")
		continue


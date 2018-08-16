import random

def draw(b):
	i = 0
	for x in b:
		if  i%3 == 0 and i != 0:
			print()
			
		print("[" + str(x) + "]", end = "")
		i += 1
	print()
			
board = [" "] * 9
inx = True
won = False	
draw(board)
				   
while not won:
	try:
		if inx == True:
			position = int(input(">>>:X "))
			if board[position-1] != ' ':
				print("Invalid input")
				continue
			board[position-1] = "X" 
			draw(board)
			inx = not inx
		else:
			position = random.randint(1,9)
			print(">>>:O ")
			if board[position-1] != ' ':
				print("Invalid input")
				continue
			board[position-1] = "O" 
			draw(board)
			inx = not inx
		
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



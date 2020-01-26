def response():
	ans=input("do u want to play again? yes or no")
	return ans=="yes"

def space_check(board,position):
	return( board[position]==" ")
	
def entry(board):
	position =0
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(myboard,position):
		position =int(input("enter the position u want to choose from 1-9:  "))
	
	return position
		
		
		
import os		
def table(board):
    os.system('cls')# doubt in thiss step have to heck which term can be used in place of clear_output for cmd
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("------")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("------")
    print(board[7]+"|"+board[8]+"|"+board[9])
	
def player_input():
	marker=" "
	while marker!="x" and marker!="0":
		player_input2=input(" what do you want to choose x or 0?:   ").lower()
		if player_input2=="x":
			marker="x"	
			player1_marker ="x"
			player2_marker= "0"
			return(player1_marker,player2_marker)
			
		elif player_input2=="0":
			marker="0"
			player1_marker = "0"
			player2_marker = "x"
			return(player1_marker,player2_marker)
			

import random			
def choose_first():
	ans= random.randint(0,1)
	if ans==1:
		return("player 1")
	else :
		return("player 2")
def place_marker(board,marker,position):
	board[position]=marker
	
def wincheck(board, marker):
	
		return((board[1]== board[2]==board[3]== marker) or (board[4]==board[5]== board[6]== marker )or( board[7]== board[8]== board[9]== marker) or 
		( board[1]== board[4]== board[7]== marker) or ( board[2]== board[5]== board[8]== marker)or( board[3]== board[6]== board[9]== marker) or 
		( board[1]== board[5]== board[9]== marker) or ( board[7]== board[5]== board[3]== marker))
		

		
		
		

def fill_check(board):
		for i in range(0,9):
			if space_check(myboard,i):
				return False
		return True	
print("welcome to the game: ")
while True:
	
	myboard=[" "]*10
	player1_marker,player2_marker= player_input()
	turn = choose_first()
	print(turn+"  will go first")
	start =input("ready to play? yes or no:  ")
	if start== "yes":
		game_on= True
	else:
		game_on=False
		
		
	while game_on:
		
		if turn=="player 1":
			table(myboard)
			position=entry(myboard)
			place_marker(myboard,player1_marker,position)
			if wincheck(myboard,player1_marker):
				table(myboard)
				print("winner is player 1")
				game_on=False
			else:
				if fill_check(myboard):
					table(myboard)
					print("There is a tie")
					game_on=False
				else:
					turn= "player 2"
		
		elif turn=="player 2":
		
			table(myboard)
			position=entry(myboard)
			place_marker(myboard,player2_marker,position)
			if wincheck(myboard,player2_marker):
				table(myboard)
				print("winner is player 2")
				game_on=False
			else:
				if fill_check(myboard):
					table(myboard)
					print("There is a tie")
					game_on=False
				else:
					turn= "player 1"
		
		
	
	if  not response():
		break

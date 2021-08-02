
row1 = ['1','2','3']
row2 = ['4','5','6']
row3 = ['7','8','9']  #cross - reference values from each list to replace value from user(X or O)

disp_row1 = [' ',' ',' ']
disp_row2 = [' ',' ',' ']
disp_row3 = [' ',' ',' ']


def display(r1,r2,r3,dr1,dr2,dr3):
	print(r1)
	print(r2)
	print(r3)
	

def display2(dr1,dr2,dr3):
	
	print(dr1)
	print(dr2)
	print(dr3)




display(row1,row2,row3,disp_row1,disp_row2,disp_row3)




def user_choice(temp,cnt = 1):
	player = temp
	
	
	display2(disp_row1,disp_row2,disp_row3)
	choice_check = input(f"Choose enter a number (1-9) :player {player} ")

	check = range(1,10)

	if choice_check.isdigit():

		if int(choice_check) in check:
			
			
			update(choice_check,player,cnt)
			#return int(choice_check)-1 #update
		else:
			print("That is not within the given range! ")
			user_choice(player)
	else:
		print("That is not a digit!")
		user_choice(player)
	
	

#choice = user_choice()

#print(choice)


def update(cho,play,count):

	if int(cho)<=3:
		

		for i in range(3):
			if row1[i] == str(cho):
				if play == 1:
					if disp_row1[i] != ' ':
						print("Position filled")
						play = 1
						check(play,count)
					else:
						disp_row1[i] = 'X'
						count = count+1
						play = 2
						check(play,count)
					
				else:
					if disp_row1[i] != ' ':
						print("Position filled")
						play = 2
						check(play,count)
					else:
						disp_row1[i] = 'O'
						count = count+1
						play = 1
						check(play,count)
					

	elif int(cho)>3 and int(cho)<=6:
	

		for i in range(3):
			if row2[i] == str(cho):
				if play == 1:
					if disp_row2[i] != ' ':
						print("Position filled")
						play = 1
						check(play,count)
					else:
						disp_row2[i] = 'X'
						count = count+1
						play = 2
						check(play,count)

				else:
					if disp_row2[i] != ' ':
						print("Position filled")
						play = 2
						check(play,count)
					else:
						disp_row2[i] = 'O'
						count = count+1
						play = 1
						check(play,count)

	else:
	
		for i in range(3):
			if row3[i] == str(cho):
				if play == 1:
					if disp_row3[i] != ' ':
						print("Position filled")
						play = 1
						check(play,count)
					else:
						disp_row3[i] = 'X'
						play = 2
						count = count+1
						check(play,count)
					
				else:
					if disp_row3[i] != ' ':
						print("Position filled")
						play = 2
						check(play,count)
					else:
						disp_row3[i] = 'O'
						play = 1
						count = count+1
						check(play,count)
					



def check(p,c):#win conditions
	
	rep = ' '
	if disp_row1[0] == disp_row1[1] == disp_row1[2] != ' ':

		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

	elif disp_row2[0] == disp_row2[1] == disp_row2[2] != ' ': 		#row check
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

	elif disp_row3[0] == disp_row3[1] == disp_row3[2] != ' ':
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)

			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")




	elif disp_row1[0] == disp_row2[0] == disp_row3[0] != ' ':
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")
		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")


	elif disp_row1[1] == disp_row2[1] == disp_row3[1] != ' ': 		#col check
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")
		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

	elif disp_row1[2] == disp_row2[2] == disp_row3[2] != ' ':
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")
		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

	elif disp_row1[0] == disp_row2[1] == disp_row3[2] != ' ':
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)

			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")
		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)

			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

	elif disp_row1[2] == disp_row2[1] == disp_row3[0] != ' ':		#diagonal check
		if p == 1:
			print(f"Game over!! Player 2 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)

			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")
		else:
			print(f"Game over!! Player 1 Wins!!!")
			display2(disp_row1,disp_row2,disp_row3)
			while rep not in ['y','n']:

				rep = input("Do you want to play again ? [y,n] :")

			if rep == 'y':
				play(rep)
			else:
				print("Thank you for playing!!")

	elif c>9:
		print("Its a draw!!")
		display2(disp_row1,disp_row2,disp_row3)

		while rep not in ['y','n']:

			rep = input("Do you want to play again ? [y,n] :")

		if rep == 'y':
			play(rep)
		else:
			print("Thank you for playing!!")

	else:
		print(c)
		user_choice(p,c)





def play(replay):

	if replay == 'y':

		for i in range(3):
			disp_row1[i] = ' '
			disp_row2[i] = ' '
			disp_row3[i] = ' '

		user_choice(1)
	

user_choice(1)


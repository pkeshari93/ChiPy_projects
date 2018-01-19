from random import randint

def roomquit():
	print('\nYou Lost, would you like to play again\n\n')
	v = raw_input('Choose Y or N\n--> ').upper()
	if v=='Y':
		return room1
	elif v=='N':
		exit(0)
	else:
		print('Not sure what you meant')
		roomquit()

def room1(): #enter braintree
	print("Would you like to enter BrainTree?")
	v = raw_input('Choose Y or N\n--> ').upper()
	if v=='Y':
		return room2
	elif v=='N':
		return roomquit
	else:
		print('Not sure what you meant')
		room1()

def room2(): #do you have id?
	print("Do you have id?")
	v = raw_input('Choose yes, flee or fight\n--> ')
	if v=='yes':
		return room6
	elif v=='flee':
		return room8
	elif v=='fight':
		print('Good thing you lifted today. Roll up your sleeves')
		x = randomnum()
		if (x == 0):
			print('he blasts you in the face. Ouch you think as you black out')
			return roomquit
		else:
			return room6
	else:
		print('Not sure what you meant')
		room2()

def room3(): #flee
	print("You ran out of merch mart and made it to the street!")
	exit(0)

def room4(): #sit
	print("Someone is asking if you want to be on a team or ride solo?")
	v = raw_input('Choose team or solo\n--> ')
	if v=='team':
		return room5
	elif v=='solo':
		print('teams rule. wrong choice')
		return roomquit
	else:
		return room4


def room5(): #team
	print("Do you want to go to conference room 1, 2, or 3?")
	v = raw_input('1, 2, or 3?\n--> ')
	if '2' in v:
		print("you choose correct, YOU WIN!")
		exit(0)
	else:
		print('wrong choice, you lose')
		return roomquit



def room6(): #go to conference room
	print("You made it to the confrence room!\nDo you want to eat pizza, sit down, or mingle?")
	v = raw_input('choose eat, mingle or sit\n--> ')
	if v=='eat':
		print('you had a snack how fun')

		return room6
	elif v=='mingle':
		print('you mingled how fun')

		return room6
	elif v=='sit':

		return room4
	else:
		print('Not sure what you meant')
		return room6


def room8(): #catch the L go home
	print("you tripped, you loose!!!!")
	return roomquit


def randomnum():
	return randint(0,1)



# start of game
current_room = room1

while(1):
	next_room = current_room()
	current_room = next_room

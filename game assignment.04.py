import time


#displays the message when you start the game
def displayIntro():
	print ('You are trapped in a maze, each passageway has a set of doors')
	print ('you need to find a way out')
	print ('if you choose the wrong path')
	print ('you fall into a trap door, and can never come out.')
	print

#check to
def chooseDoor():
	door = ''
 	while door != '1' and door != '2':  
		print ('Which Door will you Pick? (1 or 2)')
		door = raw_input()
	return door

def chooseDoor2():
	door2 = ''
 	while door2 != '3' and door2 != '4':  
		print ('Which Door will you Pick? (3 or 4)')
		door2 = raw_input()
	return door2
def chooseDoor3():
	door3 = ''
 	while door3 != '4' and door3 != '5':  
		print ('Which Door will you Pick? (4 or 5)')
		door3 = raw_input()
	return door3
def chooseDoor4():
	door4 = ''
 	while door4 != '6' and door4 != '7':  
		print ('Which Door will you Pick? (6 or 7)')
		door4 = raw_input()
	return door4

def checkDoor(chosenDoor):
	print ('You approach the Door...')
	time.sleep(2)
	print ('The Exitment Growing...')
	time.sleep(2)
	print ('You Open The door and...')
	print
	time.sleep(2)
	
	if chosenDoor == '1':	 
		print("You find a empty room")
		print(checkOne())
		door2 = raw_input()
	elif chosenDoor =='2': 
		print("You Find $5,000 and more doors")
		print(checkOne())
		door2 = raw_input()	
	
	door2 = chosenDoor
	if door2 == '3':
		print("You lose a hand and you find and more doors ")
		print(checkTwo())
		door3 = raw_input()
		
	elif door2 == '4':
		print("You find $600 and more doors")
		print(checkTwo())
		door3 = raw_input()
	door3 = door2
	if door3 == '4':
		print("You lose another foot, and find one last set of doors")
		print(checkThree())
		door4 = raw_input()
		
	elif door3 == '5':
		print("You find $200, And one last set of doors")
		print(checkThree())
		door4 = raw_input()
	door4 = str(door3)
	if door4 == '6':
		print("You fell into the trap door, and starve to death")
		playAgain()
	elif door4 =='7':
		print("You have found the exit, you got out of the maze alive Yay!")
		playAgain()
		
	else:
		print("The Data you have provided was invalid, Please try again")
		

def main():
	
	#main check
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		doorNumber = chooseDoor()
		checkDoor(doorNumber) 
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()
		

def playAgain():
	
	#Check at the end to see if they want to start over
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()
		checkDoor(chooseDoor())
		
		
		
		
		
#functions to print out the check messages		
def checkOne():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		doorNumber = chooseDoor2()
		checkDoor(doorNumber) 
		playAgain = raw_input()
def checkTwo():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		doorNumber = chooseDoor3()
		checkDoor(doorNumber) 
		playAgain = raw_input()
def checkThree():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		doorNumber = chooseDoor4()
		checkDoor(doorNumber) 
		playAgain = raw_input()


if __name__ == "__main__": main()


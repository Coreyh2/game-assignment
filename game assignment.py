import time



def displayIntro():
	print ('You are trapped in a maze, each passageway has a set of doors')
	print ('you need to find a way out')
	print ('if you choose the wrong path')
	print ('you fall into a trap door, and can never come out.')
	print
	
def chooseDoor():
	door = ''
 	while door != '1' and door != '2':  
		print ('Which Door will you Pick? (1 or 2)')
		door = raw_input()
	return door

def chooseDoor2():
	door = ''
 	while door != 'A' and door != 'B':  
		print ('Which Door will you Pick? (A or B)')
		door = raw_input()
	return door

def chooseDoor3():
	door = ''
 	while door != 'C' and door != 'D':  
		print ('Which Door will you Pick? (D or C)')
		door = raw_input()
	return door

def checkDoor(chooseDoor):
	print ('You approach the Door...')
	time.sleep(2)
	print ('The Exitment Growing...')
	time.sleep(2)
	print ('You Open The door and...')
	print
	time.sleep(2)
	def option1():
		door = '1'
		if chooseDoor == str(door):
			print("You find a empty room")
			print("Please select one of the doors")
			chooseDoor2()
			doorA = raw_input()
		else: 
			print("You Find $5,000 and more doors")
			print("Now please select door A or B")
			chooseDoor2()
			doorA = raw_input()
 		if chooseDoor == str(doorA):
 			print("You find $10,000 ")
 			print("Please select another door")
 		else:
 			print("You find another empty room")
 			print("Now please select another door")
 	
	if __name__ == "__option1__": option1()
	
	option1()
	
def main():
	
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		doorNumber = chooseDoor()
		checkDoor(doorNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()

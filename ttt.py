import time

class Set:

	def __init__(self):
		self.numX = 0
		self.numO = 0

	def incX(self):
		self.numX = self.numX + 1

	def incO(self):
		self.numO = self.numO + 1

	def inc(self,markType):
		if markType == 0:
			self.incX()
		if markType == 1:
			self.incO()

	def check(self):
		if self.numX == 3:
			return 0
		if self.numO == 3:
			return 1
		return -1


class Board:

	def __init__(self):
		self.boardmarks = [[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]
		self.setlist = [Set(),Set(),Set(),Set(),Set(),Set(),Set(),Set()]
		self.markcount = 0
		# [row0, row1, row2, col0, col1, col2, diagForwardSlash, diagBackSlash]

	def checkLocation(self,x,y):
		if self.boardmarks[x][y] == -1:
			return True
		else:
			return False

	def setBoardmark(self,x,y,markType):
		if markType == 0:
			self.boardmarks[x][y] = 0

		if markType == 1:
			self.boardmarks[x][y] = 1
			
	def checkWin(self):
		if self.markcount == 9:
			print "It's a tie!"
			self.displayBoard()
			return True
		for i in range(0,8):
			
			status = self.setlist[i].check()
			if status == 0:
				print "X's win!"
				self.displayBoard()
				return True
			if status == 1:
				print "O's win!"
				self.displayBoard()
				return True
		return False


	def addMark(self,x,y,markType):
		if self.checkLocation(x,y):

			self.setBoardmark(x,y,markType)
			self.markcount = self.markcount + 1
			if x==0 and y==0:
				self.setlist[0].inc(markType)
				self.setlist[3].inc(markType)
				self.setlist[6].inc(markType)
			if x==0 and y==1:
				self.setlist[0].inc(markType)
				self.setlist[4].inc(markType)
			if x==0 and y==2:
				self.setlist[0].inc(markType)
				self.setlist[5].inc(markType)
				self.setlist[7].inc(markType)
			if x==1 and y==0:
				self.setlist[1].inc(markType)
				self.setlist[3].inc(markType)
			if x==1 and y==1:
				self.setlist[1].inc(markType)
				self.setlist[4].inc(markType)
				self.setlist[6].inc(markType)
				self.setlist[7].inc(markType)
			if x==1 and y==2:
				self.setlist[1].inc(markType)
				self.setlist[5].inc(markType)
			if x==2 and y==0:
				self.setlist[2].inc(markType)
				self.setlist[3].inc(markType)
				self.setlist[7].inc(markType)
			if x==2 and y==1:
				self.setlist[2].inc(markType)
				self.setlist[4].inc(markType)
			if x==2 and y==2:
				self.setlist[2].inc(markType)
				self.setlist[5].inc(markType)
				self.setlist[6].inc(markType)
			return True
		else:
			return False

		#else some sort of exception?

	def displayBoard(self):
		trackingList = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
		listToPrint = [" "," "," "," "," "," "," "," "," "]
		counter0 = 0
		counter1 = 0
		counter2 = 0
		while counter1<3:
			while counter2<3:
				trackingList[counter0] = self.boardmarks[counter1][counter2]
				counter0 = counter0 + 1
				counter2 = counter2 + 1
			counter1 = counter1 + 1
			counter2 = 0

		for i in range(0,9):
			if trackingList[i] == -1:
				listToPrint[i] = " "
			if trackingList[i] == 0:
				listToPrint[i] = "X"
			if trackingList[i] == 1:
				listToPrint[i] = "O"

		print " "+listToPrint[0]+" | "+listToPrint[1]+" | "+listToPrint[2]+" "
		print "-----------"
		print " "+listToPrint[3]+" | "+listToPrint[4]+" | "+listToPrint[5]+" "
		print "-----------"
		print " "+listToPrint[6]+" | "+listToPrint[7]+" | "+listToPrint[8]+" "

def play():

	gamemenu = True
	turnbit = 0
	myboard = Board()

	while gamemenu:

		print
		myboard.displayBoard()
		print

		selection = raw_input("Press 1 to add a mark\nPress 0 to quit\nInput: ")
		selection = int(selection)

		if selection == 1:

			invalid = True
			while invalid: 
				rowSelect = raw_input("Enter the row you want to place (0-2)\nInput: ")
				rowSelect = int(rowSelect)
				colSelect = raw_input("Enter the column you want to place (0-2)\nInput: ")
				colSelect = int(colSelect)

				if rowSelect<=2 and rowSelect>=0 and colSelect<=2 and colSelect>=0:
					invalid = False
				else:
					print "\n--- INVALID SPOT, TRY AGAIN ---"
					time.sleep(1)

			if myboard.addMark(rowSelect,colSelect,turnbit):
				if myboard.checkWin():
					gamemenu = False
				else:
					turnbit = getflippedbit(turnbit)
			else:
				print "\n--- INVALID SPOT, TRY AGAIN ---"
				time.sleep(1)

		if selection == 0:
			gamemenu = False

		if selection != 0 and selection != 1:
			print "--- PLEASE SELECT A VALID NUMBER ---"
			time.sleep(1)


def getflippedbit(bit):
	print "\n --- PASS TO THE NEXT PLAYER ---"
	time.sleep(1)
	if bit==0:
		return 1
	else:
		return 0

## start of main script
menu = True
print "\n--- WELCOME TO TIC-TAC-TOE ---"
while menu:

	selection = raw_input("\n\nPress 1 to play\nPress 0 to quit\nInput: ")
	selection = int(selection)

	if selection == 1:
		play()

	if selection == 0:
		menu = False











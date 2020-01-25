from random import randint 

MAX_x = 16
MAX_y = 16
MaxMines = 40
MineLoc = [[0 for x in range(2)] for y in range(MaxMines)]

#A new location cannot match a previous location
def VerMineLoc (Mine):
	check = MaxMines - Mine
	while (check != 0):
		if(MineLoc[Mine] == MineLoc[MaxMines - check]):
			break
			return(Mine)
		else:
			check = check - 1
	return (Mine - 1)

#create a number of mines and their coordinates
def SetMineLoc (NumMines):
	Mines = int(NumMines) - 1
	while(Mines > 0 or Mines == 0):
		x = randint(0,MAX_x)
		y = randint(0,MAX_y)
		MineLoc[Mines][0] = x
		MineLoc[Mines][1] = y
		Mines = VerMineLoc(Mines)
		#Mines = Mines - 1


SetMineLoc(MaxMines)
print(sorted(MineLoc))

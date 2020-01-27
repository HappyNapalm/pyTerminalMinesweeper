from random import randint 

MAX_x = 16
MAX_y = 16
MaxMines = 40
MineLoc = [[0 for x in range(2)] for y in range(MaxMines)]
MineLoc_sorted = [[0 for x in range(2)] for y in range(MaxMines)]

#A new location cannot match a previous location
def VerMineLoc ():
	MineLoc_sorted = sorted(MineLoc)
	for a in range(0,len(MineLoc)):
		for b in range(0,len(MineLoc)):
			if(MineLoc_sorted[a] == MineLoc_sorted[b] and a is not b):
				MineLoc_sorted[a][1] = MineLoc_sorted[a][1] + 1
				if(MineLoc_sorted[a][1] >= MAX_y):
					MineLoc_sorted[a][1] = 0
	print("woot")
	print(MineLoc_sorted)
	print("woot")
	return(sorted(MineLoc_sorted))

#create a number of mines and their coordinates
def SetMineLoc (NumMines):
	Mines = int(NumMines) - 1
	while(Mines > 0 or Mines == 0):
		x = randint(0,MAX_x - 1)
		y = randint(0,MAX_y - 1)
		MineLoc[Mines][0] = x
		MineLoc[Mines][1] = y
		#Mines = VerMineLoc(Mines)
		Mines = Mines - 1
	MineLoc_sorted = sorted(MineLoc)
	print(MineLoc_sorted)
	return(VerMineLoc ())
	#MineLoc = sorted(MineLoc_sorted)

MineLoc_sorted = SetMineLoc(MaxMines)
print(sorted(MineLoc))
print(MineLoc_sorted)

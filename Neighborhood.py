from random import *
from Observable import *
from Home import *

class Neighborhood(Observable):
	'''Neighborhood is the class the holds, and observes the houses.
	What is being observed is the monsters in a given house, and
	keeps track of the total monsters in the entire neighborhood.
	The neighborhhod itself is a grid of houses.'''

	def __init__(self, size):
		Observable.__init__(self)
		self.monstersInHouses = 0
		self.gridLength = size
		self.gridSize = size*size
		self.houses = self.genHouses(self.gridLength)
	
	#generater
	def genHouses(self, size):
		neighborhood = []
		for x in range(0, size):
			streetHomes = []
			for y in range(0, size):
				tempHome = Home()
				self.monstersInHouses = self.monstersInHouses + tempHome.numMonster()
				streetHomes.append(tempHome)
				tempHome.add_observer(self)
			neighborhood.append(streetHomes)
		return neighborhood

	#Getters
	def getMonstersInHouses(self):
		return self.monstersInHouses

	def getGridSize(self):
		return self.gridSize

	def getHouses(self):
		return self.houses

	def getGridLength(self):
		return self.gridLength

	#Setters
	def setMonstersInHouses(self, h):
		self.monstersInHouses = h

	def setGridSize(self, s):
		self.gridSize = s

	def setHouse(self, b):
		self.houses = b

	def setGridLength(self, l):
		self.gridLength = l

	def update(self):
		self.monstersInHouses = self.monstersInHouses - 1

		


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
	
	'''genHouses(self, size) is the method that genorates the
	homes that go inside of the list of houses.
	- Returns the neighborhood of houses.'''
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

	'''getMonstersInHouses(self) returns the total amount of
	monsters in the neighborhood.'''
	def getMonstersInHouses(self):
		return self.monstersInHouses

	'''getGridSize(self) returns the size of the grid.'''
	def getGridSize(self):
		return self.gridSize

	'''getHouses(self) returns the list of homes.'''
	def getHouses(self):
		return self.houses

	'''getGridLength(self) returns the length of the grid.'''
	def getGridLength(self):
		return self.gridLength

	'''setMonstersInHouses(self, h) sets the monstersInHouses value
	to equal h.'''
	def setMonstersInHouses(self, h):
		self.monstersInHouses = h

	'''setGridSize(self, s) sets the gridSize value to equal s.'''
	def setGridSize(self, s):
		self.gridSize = s

	'''setHouse(self, b) sets the houses to the value b.'''
	def setHouse(self, b):
		self.houses = b

	'''setGridLength(self, l) sets the gridLength to the value l.'''
	def setGridLength(self, l):
		self.gridLength = l

	'''update(self) updates the monstersInHouses value.'''
	def update(self):
		self.monstersInHouses = self.monstersInHouses - 1

		


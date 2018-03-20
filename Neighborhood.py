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
		self.monstersInHouse = 0
		self.gridSize = size*size
		self.houses = genHouses(self, size)
	
	#generater
	def genHouses(self, size):
		neighborhood = []
		for x in range(0, size):
			streetHomes = []
			for y in range(0, size):
				tempHome = Home()
				self.monstersInHouse = self.monstersInHouse + tempHome.numMonsters()
				streetHomes.append(tempHome)
				super.add_observer(tempHome)
			neighborhood.append(streetHomes)
		return neighborhood

	#Getters
	def getMonstersInHouse(self):
		return self.monstersInHouse

	def getGridSize(self):
		return self.gridSize

	def getHouses(self):
		return self.houses


	#Setters
	def setMonstersInHouse(self, h):
		self.monstersInHouse = h
	def setGridSize(self, s):
		self.gridSize = s
	def setHouse(self, b):
		self.houses = b


		


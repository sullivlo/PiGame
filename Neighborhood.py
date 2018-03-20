from random import *
from Observable import *
from Home import *

class Neighborhood(Observable):
	'''Neighborhood is the class the holds, and observes the houses.
	What is being observed is the monsters in a given house, and
	keeps track of the total monsters in the entire neighborhood.
	The neighborhhod itself is a grid of houses.'''

	def __init__(self):
		Observable.__init__(self)
		self.monstersInHouse = 0
		self.peopleInHouse = 0
		self.houses = []
	
	#generaters 	
	def genMonstersInHouse():
		pass

	def genPeopleInHouse():
		pass

	def genHouses():
		pass

	#Getters

	def getMonstersInHouse(self):
		return self.monstersInHouse

	def getPeopleInHouse(self):
		return self.peopleInHouse

	def getHouses(self):
		return self.houses


	#Setters
	def setMonstersInHouse(self, h):
		self.monstersInHouse = h
	def setPeopleInHouse(self, a):
		self.peopleInHouse = a
	def setHouse(self, b):
		self.houses = b


		


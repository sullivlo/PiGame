from random import *
from Observable import *
from Home import *

class neighborhood(Observable):
	def __init__(self):
		Observable.__init__(self)
		self.monstersInHouse = []
		self.peopleInHouse = []
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


		


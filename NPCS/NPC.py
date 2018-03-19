from Observable import *
from random import *

class NPC(Observable):
	'''NPC is the overlying class for all the monsters/people'''
	def __init__(self):
		Observable.__init__(self)
		self.health = 0
		self.attack = 0
		self.unaffCandy = []
		self.altCandy = []
		self.name = ''
		self.alive = True

	def genHealth(self):
		pass
	def genAttack(self):
		pass

	# generate unaffective candy
	def genUnaffCandy(self):
		pass
	
	# generate very affective candy, called alt 
	def genAltCandy(self):
		pass
	#Getters
	def getHealth(self):
		return self.health
	def getAttack(self):
		return self.attack
	def getUnaffCandy(self):
		return self.unaffCandy
	def getName(self):
		return self.name
	def getAlive(self):
		return self.alive
	def getAltCabdy(self):
		return self.altCandy
	
	#Setters
	def setHealth(self, h):
		self.health = h
	def setAttack(self, a):
		self.attack = a
	def setUnaffCandy(self, c):
		self.unaffCandy = c
	def setName(self, n):
		self.name = n
	def setAlive(self, a):
		self.alive = a

	def setAltCandy(self, x):
		self.altCandy = x

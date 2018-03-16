from Observable import *
from random import *

class NPC(Observable):
	'''NPC is the overlying class for all the monsters/people'''
	def __init__(self):
		Observable.__init__(self)
		self.health = 0
		self.attack = 0
		self.unaffCandy = []
		self.name = ''
		self.alive = True

	def genHealth(self):
		pass
	def genAttack(self):
		pass
	def genUnaffCandy(self):
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
	#Setters
	def setHealth(self, h):
		self.health = h
	def setAttack(self, a):
		self.attack = a
	def setName(self, n):
		self.name = n
	def setAlive(self, a):
		self.alive = a
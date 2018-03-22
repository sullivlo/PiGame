from Observable import *
from random import *

'''NPC is the observable class for all of the monsters/person
init creates the NPC object with health, attack, unaffected Candy,
alt (string weapon), name, and is NPC alive'''
class NPC(Observable):
	def __init__(self):
		Observable.__init__(self)
		self.health = 0
		self.attack = 0
		self.unaffCandy = []
		self.altCandy = []
		self.name = ''
		self.alive = True
	'''Generates the health of the NPC'''
	def genHealth(self):
		pass
	'''Generates the attack of the NPC'''
	def genAttack(self):
		pass

	''' generate unaffective candy for that monsther or person'''
	def genUnaffCandy(self):
		pass
	
	''' generate very affective candy, called alt'''
	def genAltCandy(self):
		pass
	
	'''Getter for health
	-return NPC health'''
	def getHealth(self):
		return self.health
	'''Getter for attack
	-return NPC attack'''
	def getAttack(self):
		return self.attack
	'''Getter for unaffCandy
	-return NPC unaffCandy'''
	def getUnaffCandy(self):
		return self.unaffCandy
	'''Getter for getName
	-return NPC getName'''
	def getName(self):
		return self.name
	'''Getter for get Alive
	-return NPC getAlive'''
	def getAlive(self):
		return self.alive
	'''Getter for altCandy
	-return NPC AltCandy'''
	def getAltCandy(self):
		return self.altCandy
	
	'''Setter for setHealth
	-return NPC setHealth'''
	def setHealth(self, h):
		self.health = h
	'''Setter for setAttack
	-return NPC setAttack'''
	def setAttack(self, a):
		self.attack = a
	'''Setter for setUnaffCandy
	-return NPC setUnaffCandy'''
	def setUnaffCandy(self, c):
		self.unaffCandy = c
	'''Setter for setName
	-return NPC setName'''
	def setName(self, n):
		self.name = n
	'''Setter for setAlive
	-return NPC setAlive'''
	def setAlive(self, a):
		self.alive = a
	'''Setter for setAltCandy
	-return NPC setAltCandy'''
	def setAltCandy(self, x):
		self.altCandy = x

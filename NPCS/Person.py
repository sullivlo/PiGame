from random import *
from NPCS.NPC import *

'''Person is the observer class that creates the Person object
init creates the persons object with health, attack, unaffected Candy,
alt (string weapon), name, and is NPC alive'''
class Person(NPC):
	'''Persons are monsters/NPCs who have a health between of 100.
	They are not harmed by the plater. Persons help you by giving 
	you candy. Each piece of candy increases your health by 1 point.
	 A person can give you 1 piece of candy per turn. '''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Person'
		self.health = self.genHealth()
		self.attack = self.genAttack()
		self.unaffCandy = self.genUnaffCandy()
		self.altCandy = self.genAltCandy()
	
	"""Generates the Persons Health
	return the persons health"""
	def genHealth(self):
		return 100
	"""Generates the Persons attack
	return the persons attack"""
	def genAttack(self):
		return -1
	"""Generates the Persons altimate candy
	return the persons altimate candy"""
	def genAltCandy(self):
		return []
	"""Generates the Persons altimate candy
	return the persons altimate candy"""
	def genUnaffCandy(self):
		return ['HersheyKisses','SourStraws','ChocolateBars','NerdBombs']


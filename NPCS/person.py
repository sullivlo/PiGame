from random import *
from NPCS.NPC import *

class Person(NPC):
	'''Persons are monsters/NPCs who have a health between of 100.
	They are not harmed by the plater. Persons help you by giving 
	you candy. Each piece of candy increases your health by 1 point.
	 A person can give you 1 piece of candy per turn. '''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Person'
		self.health = self.genHealth()
		self.unaffCandy = self.genUnaffCandy()
		self.altCandy = self.genAltCandy()

		
	def genHealth(self):
		return 100
	def genAttack(self):
		return -1

	def genAltCandy(self):
		return []

	def genUnaffCandy(self):
		return ['HersheyKisses','SourStraws','ChocolateBars','NerdBombs']


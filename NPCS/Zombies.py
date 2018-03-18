from random import *
from NPC import *

class Zombies(NPC):
	'''Zombies are monsters/NPCs who have a health between 50 - 100.
	as well they had an attack rating between 0 and 10. They are harmed
	by all weapons, but SourStraws have twice an affect.'''

	def __init__(self):
		super.__init__(self)
		super.setName(self, 'Zombies')
		super.setHealth(self, genHealth(self))
		super.setUnaffCandy(self, genUnaffCandy(self))
		super.setAltCandy(self, getAltCandy(self))	
	
	def genHealth(self):
		return randint(50, 100)
	def genAttack(self):
		return randint(0, 10)
	def genUnaffCandy(self):
		return ['']
	def genAltCandy(self):
		return['SourStraws'] #2x

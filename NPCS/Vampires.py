from random import *
from NPC import *

class Vampires(NPC):
	'''Vampires are monsters/NPCs who have a health between 100 - 200.
	as well they had an attack rating between 10 and 20. They are harmed
	by all weapons, but ChocolateBars.'''

	def __init__(self):
		super.__init__(self)
		super.setName(self, 'Vampires')
		super.setHealth(self, genHealth(self))
		super.setUnaffCandy(self, genUnaffCandy(self))
		super.setAltCandy(self, genAltCandy(self))
		
	def genHealth(self):
		return randint(100, 200)
	def genAttack(self):
		return random.uniform(10, 20)
	def genUnaffCandy(self):
		return ['ChocolateBars']	
	def genAltCandy(self):
		return ['']

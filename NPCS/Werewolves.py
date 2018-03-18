
from random import *
from NPC import *

class Werewolves(NPC):
	'''Werewolves are monsters/NPCs whe have a health of 200.
	as well they had an attack rating between 0 and 40. They are harmed
	by all weapons, but ChocolateBars or SourStraws.'''

	def __init__(self):
		super.__init__(self)
		super.setName(self, 'Werewolves')
		super.setHealth(self, genHealth(self))
		super.setUnaffCandy(self, genUnaffCandy(self))
		super.setAltCandy(self, getAltCandy(self))		

	def genHealth(self):
		return 200
	def genAttack(self):
		return random.uniform(0, 40)
	def genUnaffCandy(self):
		return ['ChocolateBars', 'SourStraws']

	def genAltCandy(self):
		return ['']



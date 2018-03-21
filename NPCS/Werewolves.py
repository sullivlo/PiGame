
from random import *
from NPCS.NPC import *

class Werewolves(NPC):
	'''Werewolves are monsters/NPCs whe have a health of 200.
	as well they had an attack rating between 0 and 40. They are harmed
	by all weapons, but ChocolateBars or SourStraws.'''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Werewolves'
		self.health = self.genHealth()
		self.attack = self.genAttack()
		self.unaffCandy = self.genUnaffCandy()
		self.altCandy = self.genAltCandy()
	def genHealth(self):
		return 200
	def genAttack(self):
		return uniform(0, 40)
	def genUnaffCandy(self):
		return ['ChocolateBars', 'SourStraws']

	def genAltCandy(self):
		return ['']



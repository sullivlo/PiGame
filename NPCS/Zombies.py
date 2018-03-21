from random import *
from NPCS.NPC import *

class Zombies(NPC):
	'''Zombies are monsters/NPCs who have a health between 50 - 100.
	as well they had an attack rating between 0 and 10. They are harmed
	by all weapons, but SourStraws have twice an affect.'''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Zombies'
		self.health = self.genHealth()
		self.unaffCandy = self.genUnaffCandy()
		self.altCandy = self.genAltCandy()
	
	def genHealth(self):
		return random.randint(50, 100)
	def genAttack(self):
		return random.randint(0, 10)
	def genUnaffCandy(self):
		return ['']
	def genAltCandy(self):
		return['SourStraws'] #2x

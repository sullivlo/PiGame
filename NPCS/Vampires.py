from random import *
from NPCS.NPC import *

class Vampires(NPC):
	'''Vampires are monsters/NPCs who have a health between 100 - 200.
	as well they had an attack rating between 10 and 20. They are harmed
	by all weapons, but ChocolateBars.'''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Vampiress'
		self.health = self.genHealth()
		self.unaffCandy = self.genUnaffCandy()
        self.altCandy = self.genAltCandy()
		
	def genHealth(self):
		return randint(100, 200)
	def genAttack(self):
		return random.uniform(10, 20)
	def genUnaffCandy(self):
		return ['ChocolateBars']	
	def genAltCandy(self):
		return ['']

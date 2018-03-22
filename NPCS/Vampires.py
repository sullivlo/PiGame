from random import *
from NPCS.NPC import *

'''Vampires is the observer class that creates the Vampires object
init creates the Vampire object with health, attack, unaffected Candy,
alt (string weapon), name, and is NPC alive'''
class Vampires(NPC):
	'''Vampires are monsters/NPCs who have a health between 100 - 200.
	as well they had an attack rating between 10 and 20. They are harmed
	by all weapons, but ChocolateBars.'''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Vampires'
		self.health = self.genHealth()
		self.attack = self.genAttack()
		self.unaffCandy = self.genUnaffCandy()
		self.altCandy = self.genAltCandy()
	'''Generates the health of the vampires
	returns the health of the vampires'''
	def genHealth(self):
		return randint(100, 200)
	'''Generates the attack of the vampires
	returns the attack of the vampires'''
	def genAttack(self):
		return uniform(10, 20)
	'''Generates the unaffected candy of the vampires
	returns the list unaffected list of the vampires'''
	def genUnaffCandy(self):
		return ['ChocolateBars']
	'''Generates the altimate candy of the vampires
	returns the list of altimate candy of the vampires'''
	def genAltCandy(self):
		return ['']

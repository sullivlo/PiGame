from random import *
from NPCS.NPC import *

"""NPC observer that creates the Zombies object
init creates the NPC object with health, attack, unaffected Candy,
alt (string weapon), name, and if the zombie alive"""
class Zombies(NPC):
	'''Zombies are monsters/NPCs who have a health between 50 - 100.
	as well they had an attack rating between 0 and 10. They are harmed
	by all weapons, but SourStraws have twice an affect.'''

	def __init__(self):
		NPC.__init__(self)
		self.name = 'Zombies'
		self.health = self.genHealth()
		self.attack = self.genAttack()
		self.unaffCandy = self.genUnaffCandy()
		self.altCandy = self.genAltCandy()
	'''Generates the health of the Zombies
   	 -return the ghouls health'''
	def genHealth(self):
		return randint(50, 100)
	'''Generates the attack of the Zombies
    	-return the Zombies attack'''
	def genAttack(self):
		return uniform(0, 10)
	'''Generates the unnaffected candy of the Zombies
   	 -return the list of Zombies unaffected candy'''
	def genUnaffCandy(self):
		return ['']
	'''Generates the altimate candy of the Zombies
   	 -return the list of Zombies unaffected candy'''
	def genAltCandy(self):
		return['SourStraws'] #2x

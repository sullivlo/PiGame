
from random import *
from NPCS.NPC import *
"""NPC observer that creates the werewolves object
init creates the NPC object with health, attack, unaffected Candy,
altimate weapon, name, and is NPC alive"""
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
	'''Generates the health of the werewolve
	 -return the werewolve health'''
	def genHealth(self):
		return 200
	'''Generates the attack of the werewolve
	 -return the werewolve attack'''
	def genAttack(self):
		return uniform(0, 40)
	'''Generates the health of the werewolve
		-return the list of werewolve uneffected candy'''
	def genUnaffCandy(self):
		return ['ChocolateBars', 'SourStraws']
	'''Generates the altimate candy of the werewolve
		-return the list of werewolve altimate candy'''
	def genAltCandy(self):
		return ['']



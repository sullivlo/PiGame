from random import *
from Weapons import *

class Player(Object):
	''' Base Player class. '''
	def __init__(self):
		self.health = randint(100, 125)
		self.attack = randint(10, 20)
		self.weapons = popWeapons(self)

	def popWeapons(self):


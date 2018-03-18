
from random import *
from NPC import *

class persons(NPC):
	'''Persons are monsters/NPCs who have a health between of 100.
	They are not harmed by the plater. Persons help you by giving 
	you candy. Each piece of candy increases your health by 1 point.
	 A person can give you 1 piece of candy per turn. '''

	def __init__(self):
		super.__init__(self)
		super.setName(self, 'Persons')
		super.setHealth(self, genHealth(self))
		super.setUnaffCandy(self, genUnaffCandy(self))
		
	def genHealth(self):
		return 100
	def genAttack(self):
		return 
	def genUnaffCandy(self):
		return ['HersheyKisses','SourStraws','ChocolateBars','NerdBombs']

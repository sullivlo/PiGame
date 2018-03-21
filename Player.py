from random import *
from Weapons import *


class Player(object):

	''' Base Player class. '''
	def __init__(self):
		self.health = self.genHealth()
		self.attack = self.genAttack()
		self.weapons = self.popWeapons()
		self.posX = 0
		self.posY = 0
        
        #Populate the weapon List that the play holds
        #Changed control flow beucase tempList created readablibity issues
	def popWeapons(self):
		hersheykisses = HersheyKisses.HersheyKisses()
		weaponList = [HersheyKisses]
		for size in range(0,9):
			randWeapon = randint(0,2)
			weapon = tempList[randWeapon]
			if weapon == 'SourStraws':
				weaponList.append(SourStraws.SourStraws())
			elif weapon == 'Nerdbomb':
				weaponList.append(Nerdbomb.NerdBomb())
			elif weapon == 'ChocolateBars':
				weaponList.append(ChocolateBars.ChocolateBars())
		return weaponList

        #Initialize Player 
	def decreaseHealth(self, h):
		self.health = self.health - h

	def increaseHealth(self, h):
		self.health = self.health + h

	def genAttack(self):
		self.attack = random.randint(10, 20)

	def genHealth(self):

		self.health = randint(100, 125)

	def appendInventory(self, weapon):
		if weapon == 'SourStraws':
			weaponList.append(SourStraws.SourStraws())
		elif weapon == 'Nerdbomb':
			weaponList.append(Nerdbomb.NerdBomb())
		elif weapon == 'ChocolateBars':
			weaponList.append(ChocolateBars.ChocolateBars())

	#Create Player class getters
	def getHealth(self):
		return self.health

	def getAttack(self):
		return self.attack

	def getInventory(self):
		return self.weapons

	def getPosX(self):
		return self.posX

	def getPosY(self):
		return self.posY

	#Create Player class setters
	def setHealth(self, h):
		self.health = h

	def setAttack(self, a):
		self.attack = a

	def setPosX(self, x):
		self.posX = x

	def setPosY(self, y):
		self.posY = y

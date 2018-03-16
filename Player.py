from random import *
from Weapons import *

class Player(Object):
	''' Base Player class. '''
	def __init__(self):
		self.health = genHealth(self)
		self.attack = genAttack(self)
		self.weapons = popWeapons(self)

	def popWeapons(self):
		HersheyKisses = Weapons.HersheyKisses()
		weaponList = [HersheyKisses]
		tempList = ['SourStraws', 'NerdBomb', 'ChocolateBars']
		for size in range(0,9):
			randWeapon = randint(0,2)
			if tempList[randWeapon] == 'SourStraws':
				weaponList.append(Weapons.SourStraws())
			if tempList[randWeapon] == 'NerdBomb':
				weaponList.append(Weapons.NerdBomb())
			if tempList[randWeapon] == 'ChocolateBars':
				weaponList.append(Weapons.ChocolateBars())
		return weaponList

	def decreaseHealth(self, h):
		self.health = self.health - h

	def increaseHealth(self, h):
		self.health = self.health + h

	def genAttack(self):
		self.attack = randint(10, 20)

	def genHealth(self):
		self.health = randint(100, 125)
	#Getters
	def getHealth(self):
		return self.health

	def getAttack(self):
		return self.attack

	def getInventory(self):
		return self.weapons

	#Setters
	def setHealth(self, h):
		self.health = h

	def setAttack(self, a):
		self.attack = a

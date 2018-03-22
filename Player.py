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
	
	'''popWeapons(self) creates a list of different weapons objects
	for the users to hold.
	- Returns a list of Random weapons'''
	def popWeapons(self):
		hersheykisses = HersheyKisses.HersheyKisses()
		weaponList = [hersheykisses]
		tempList = ['SourStraws', 'Nerdbomb', 'ChocolateBars']
		for size in range(0,9):
			randWeapon = randint(0,2)
			weapon = tempList[randWeapon]
			if weapon == 'SourStraws':
				sourstraws = SourStraws.SourStraws()
				weaponList.append(sourstraws)
			elif weapon == 'Nerdbomb':
				nerdbomb = NerdBomb.NerdBomb()
				weaponList.append(nerdbomb)
			elif weapon == 'ChocolateBars':
				chocolatebars = ChocolateBars.ChocolateBars()
				weaponList.append(chocolatebars)
		return weaponList

	'''decreaseHealth(self, h) this method decreases the players health by
	the value of h.''' 
	def decreaseHealth(self, h):
		self.health = self.health - h

	'''genAttack(self) generates a random integer for the attack value of
	the player between 10 and 20.
	- Returns the random integer.'''
	def genAttack(self):
		return randint(10, 20)

	'''genHealth(self) generates a random integer for the health value of
	the player between 100 and 125.
	- Returns the random integer.'''
	def genHealth(self):
		return randint(100, 125)

	'''printInventory(self) prints the users inventory with a inventory slot
	number, the name of the weapon, the uses remaining, and the weapon mod.'''
	def printInventory(self):
		invSlot = 0
		for wp in self.weapons:
			print('Inventory Slot: {num}, Weapon: {name}, Uses: {uses}, Modifier {mod}'
				.format(num=invSlot, name=wp.getName(), uses=wp.getUses(), mod = wp.getModif()))
			invSlot = invSlot + 1

	'''appendInventory(self, weapon) this method adds a weapon from the parameter
	to the inventory of the player.'''
	def appendInventory(self, weapon):
		if weapon == 'SourStraws':
			self.weapons.append(SourStraws.SourStraws())
		elif weapon == 'Nerdbomb':
			self.weapons.append(Nerdbomb.NerdBomb())
		elif weapon == 'ChocolateBars':
			self.weapons.append(ChocolateBars.ChocolateBars())

	'''deleteWeapon(self, position) this method deletes a weapon
	from the player's inventory.'''
	def deleteWeapon(self, position):
		del self.weapons[position]

	'''genHealth(self) returns the player's health'''
	def getHealth(self):
		return self.health

	'''getAttack(self) returns the player's attack.'''
	def getAttack(self):
		return self.attack

	'''getInventory(self) returns the player's inventory'''
	def getInventory(self):
		return self.weapons

	'''getPosX(self) returns the players posX value.'''
	def getPosX(self):
		return self.posX

	'''getPosY(self) returns the player's posY value.'''
	def getPosY(self):
		return self.posY

	'''setHealth(self) sets the player's health value from h.'''
	def setHealth(self, h):
		self.health = h

	'''setAttack(self, a) sets the player's attack value from a.'''
	def setAttack(self, a):
		self.attack = a

	'''setPosX(self, x) sets the player's posX value from x.'''
	def setPosX(self, x):
		self.posX = x

	'''setPosX(self, y) sets the player's posY value from y.'''
	def setPosY(self, y):
		self.posY = y

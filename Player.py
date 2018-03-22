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

        #Initialize Player 
	def decreaseHealth(self, h):
		self.health = self.health - h

	def genAttack(self):
		return randint(10, 20)

	def genHealth(self):
		return randint(100, 125)

	def printInventory(self):
		invSlot = 0
		for wp in self.weapons:
			print('Inventory Slot: {num}, Weapon: {name}, Uses: {uses}, Modifier {mod}'
				.format(num=invSlot, name=wp.getName(), uses=wp.getUses(), mod = wp.getModif()))
			invSlot = invSlot + 1

	def appendInventory(self, weapon):
		if weapon == 'SourStraws':
			self.weapons.append(SourStraws.SourStraws())
		elif weapon == 'Nerdbomb':
			self.weapons.append(Nerdbomb.NerdBomb())
		elif weapon == 'ChocolateBars':
			self.weapons.append(ChocolateBars.ChocolateBars())

	def deleteWeapon(self, position):
		del self.weapons[position]

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

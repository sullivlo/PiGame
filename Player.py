from random import *
from Weapons import *


class Player(Object):
	''' Base Player class. '''
	def __init__(self):
		self.health = genHealth(self)
		self.attack = genAttack(self)
		self.weapons = popWeapons(self)
        
        #Populate the weapon List that the play holds
        #Changed control flow beucase tempList created readablibity issues
	def popWeapons(self):
		HersheyKisses = Weapons.HersheyKisses()
		weaponList = [HersheyKisses]
		for size in range(0,9):
			randWeapon = randint(0,2)
	
                        if(randWeapon == 0): 
                                weaponList.append(Weapons.SourStraws())
                        else if(randWeapon == 1):
                                weaponList.append(Weapons.NerdBomb())
                        else if(randWeapon == 2):
                                weaponList.append(Weapons.ChocolateBars())
                return weaponList

        #Initialize Player 
	def decreaseHealth(self, h):
		self.health = self.health - h

	def increaseHealth(self, h):
		self.health = self.health + h

	def genAttack(self):
		self.attack = random.randint(10, 20)

	def genHealth(self):
		self.health = random.randint(100, 125)
	#Create Player class getters
	def getHealth(self):
		return self.health

	def getAttack(self):
		return self.attack

	def getInventory(self):
		return self.weapons

	#Create Player class setters
	def setHealth(self, h):
		self.health = h

	def setAttack(self, a):
		self.attack = a

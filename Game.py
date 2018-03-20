import math
from random import *
import Neighborhood
import Player

class Game(object):
	'''Game is how the all the objects come and work together.
	Here contains how everything is built to actually play
	the game as a user. It brings all the differnet objects
	together and has them work to complete the game.'''

	def __init__(self):
        self.player = Player.Player()
        self.neighborhood = Neighborhood.Neighborhood(randint(2, 10))
        self.turn = True  # player turn = true, monster turn = false
        				  #	once anyone attacks you switch to what is itsnt now
        self.gameover = False

    def move(self):
    	nextPos = input("\nWhat direction would you like to go in?"
    		+"\nN for North\nS for South\nE for East\nW for West").upper()
    	if isValidMove(nextPost):
    		if (nextPos == 'N'):
    			self.player.setPosY(self.player.getPosY()-1)
    		elif (nextPos == 'W'):
    			self.player.setPosX(self.player.getPosX()-1)
    		elif (nextPos == 'S'):
    			self.player.setPosY(self.player.getPosY()+1)
    		elif (nextPos == 'E'):	
    			self.player.setPosX(self.player.getPosX()+1)
    	else:
    		print("Not a valid move.")


    def isValidMove(self, nextPos):
    	validMove = true
    	if (nextPos == 'N') and (self.player.getPosY() == 0):
    		validMove = false
    	elif (nextPos == 'W') and (self.player.getPosX == 0):
    		validMove = false
    	elif (nextPos == 'S') and (self.player.getPosY == self.neighborhood.getGridLength()):
    		validMove = false
    	elif (nextPos == 'E') and (self.player.getPosY == self.neighborhood.getGridLength()):	
    		validMove = false
    	return validMove

    def getInventory(self): 
    	invSlot = 0
        print("\n--------------------------- Inventory -----------------------------------")
        for weapon in self.player.getInventory():
        	wName = weapon.getName()
        	wUses = weapon.getUses()
        	wModif = weapon.getModif()
        	print('\tInventory Slot: {num}, Weapon: {name}, Uses: {uses}, Modifier {mod}'
        		.format(num=invSlot, name=wName, uses=wUses, mod = wModif))
            invSlot = invSLot + 1
    def playerHealth(self):
    	print("\nPlayer Health: {}".format(player.getHealth()))

    def totalMonsterCount(self):
        print("\nTotal Monsters Remaining: {}".format(neighborhood.getMonstersInHouses()))
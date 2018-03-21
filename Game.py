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
                          #    once anyone attacks you switch to what is itsnt now
        self.gameover = False


    def run(self):
        while(self.gameover == False):

            self.gameover = isGameOver()
            

    def displayGrid(self):
        print("\n---------------Neighborhood----------------")
        size = self.neighborhood.getGridLength()
        for x in range(0, size):
            pos = ""
            for y in range(0, size):
                if self.player.getPosX() == x and self.player.getPosY == y:
                    pos = "{pos} P".format(pos = pos)
                elif self.neighborhood.getHouses()[x][y].numMonster() == 0:
                    pos = "{pos} E".format(pos = pos)
                else:
                    pos = "{pos} O".format(pos = pos)
            print("\n{pos}".format(pos = pos))

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

    def isGameOver(self):
        gameOver = False
        if self.player.getHeath()<=0:
            gameOver = True
            print("Player has died. You have failed you mission. :(")
        elif self.neighborhood.getMonstersInHouses()==0:
            gameOver = True
            print("You have killed all the Monster and have saved your friends!")

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

    def getWeapon(self):
        invSize = 0
        self.getInventory()
        selected = int(input("\nWhat weopon would you like to use?\nInput the Inventory Slot number."))
        return selected

    def playerAttack(self):
        selected = self.getWeapon()
        weapon = self.player.getInventory()[selected]
        weapon.decreaseUses()
        tmpAttValue = self.player.getAttack() * weapon.getModif()
        for monster in self.neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()].getMonsters():
            if monster == 'Zombies':
                if weapon in monster.getAltCandy():
                    monster.setHealth(monster.getHeath()-(2*tmpAttValue))
                else:
                    monster.setHealth(monster.getHeath()-tmpAttValue)
            elif monster == 'Vampires':
                if weapon not in monster.getUnAffCandy():
                    monster.setHealth(monster.getHeath()-tmpAttValue)
            elif monster == 'Werewolves':
                if weapon not in monster.getUnAffCandy():
                    monster.setHealth(monster.getHeath()-tmpAttValue)
            elif monster == 'Ghouls':
                if weapon in monster.getAltCandy():
                    monster.setHealth(monster.getHeath()-(5*tmpAttValue))
                else:
                    monster.setHealth(monster.getHeath()-tmpAttValue)


    def playerHealth(self):
        print("\nPlayer Health: {}".format(player.getHealth()))

    def totalMonsterCount(self):
        print("\nTotal Monsters Remaining: {}".format(neighborhood.getMonstersInHouses()))

    def monstersAttack(self):
        tmpAttValue = 0
        for i in self.Neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()].getMonsters():
            tmpAttValue = tmpAttValue + i.getAttack()
        self.player.setHealth(self.player.getHealth() - tmpAttValue)
        print("\nPlayer Attacked by the monster, yikes! Lost hp: {}".format(tmpAttValue))
    
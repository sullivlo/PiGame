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
        self.neighborhood = Neighborhood.Neighborhood(randint(2, 5))
        self.turn = True  # player turn = true, monster turn = false
                          #    once anyone attacks you switch to what is itsnt now
        self.gameover = False


    def run(self):
        print("\nOh No! You have woken up in your home today to find "+
            "that some of you family has been mutated to monsters.")
        print("\nBut it gets. You have walked outside and see that "+
            "some of your neighbors have had the same fate.")
        print("\nIt is your mission to not only save your family but"+
            " to save the entire neighborhood.")
        print("Using all of your Halloween candy change the monsters"+
            " back to your friends and family members.")
        print("Here is the map of the neighborhood. You are P. "+
            "If a house is empty an E will display at its place."+
            " All the houses that still have monsters will have an O.")


        while(self.gameover == False):
            print("\n---------------Player Turn----------------")
            self.displayGrid()
            self.currentHome()
            cmd = input("\nWhat action would you like to take?\n")
            cmd = cmd.lower()
            if cmd == "attack":
                self.playerAttack()
            elif cmd == "move":
                self.move()
            elif cmd == "inventory":
                self.getInventory()
            elif cmd == "health":
                self.playerHealth()
            elif cmd == "monstersLeft":
                self.totalMonsterCount()
            elif cmd == "quit":
                self.gameover = True
                return
            else:
                print("Not a vaild action.")
            self.gameover = self.isGameOver()
            if(self.gameover == False):
                print("\n---------------Monster's Turn----------------")
                self.monstersAttack()

    def currentHome(self):
        print("\nCurrent home has:")
        for mon in self.neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()].getMonsters():
            if mon.getName() is not 'Person':
                print("\n{name} with {health}".format(name = mon.getName(), health = mon.getHealth()))
            else:
                print("\nPerson here.")

    def displayGrid(self):
        print("\n---------------Neighborhood----------------")
        size = self.neighborhood.getGridLength()
        for y in range(0, size):
            pos = ""
            for x in range(0, size):
                if self.player.getPosX() == x and self.player.getPosY() == y:
                    pos = "{pos} P".format(pos = pos)
                elif self.neighborhood.getHouses()[x][y].numMonster() == 0:
                    pos = "{pos} E".format(pos = pos)
                else:
                    pos = "{pos} O".format(pos = pos)
            print("\n{pos}".format(pos = pos))

    def move(self):
        nextPos = input("\nWhat direction would you like to go in?"
            +"\nN for North\nS for South\nE for East\nW for West\n").upper()
        if self.isValidMove(nextPos):
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
        validMove = True
        print(self.neighborhood.getGridLength())
        print(self.player.getPosX())
        print(self.player.getPosY())
        if (nextPos == 'N') and (self.player.getPosY() == 0):
            validMove = False
        elif (nextPos == 'W') and (self.player.getPosX() == 0):
            validMove = False
        elif (nextPos == 'S') and (self.player.getPosY() == self.neighborhood.getGridLength()-1):
            validMove = False
        elif (nextPos == 'E') and (self.player.getPosX() == self.neighborhood.getGridLength()-1):    
            validMove = False
        return validMove

    def isGameOver(self):
        gameOver = False
        currHealth = self.player.getHealth()
        if currHealth <= 0:
            gameOver = True
            print("\nPlayer has died. You have failed you mission. :(")
        elif self.neighborhood.getMonstersInHouses()==0:
            gameOver = True
            print("\nYou have killed all the Monster and have saved your friends!")
        return gameOver

    def getInventory(self): 
        print("\n---------------------- Inventory ------------------------")
        self.player.printInventory()

    def getWeapon(self):
        invSize = 0
        self.getInventory()
        selected = int(input("\nWhat weopon would you like to use?\nInput the Inventory Slot number.\n"))
        tempWeapon = self.player.getInventory()[selected]
        return tempWeapon

    def playerAttack(self):
        tempWeapon = self.getWeapon()
        tempWeapon.decreaseUses()
        tmpAttValue = self.player.getAttack() * tempWeapon.getModif()
        pos = 0
        currHouse = self.neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()]
        for monster in currHouse.getMonsters():
            if monster.getName() == 'Zombies':
                if tempWeapon.getName() in monster.getAltCandy():
                    monster.setHealth(monster.getHealth()-(2*tmpAttValue))
                else:
                    monster.setHealth(monster.getHealth()-tmpAttValue)
            elif monster.getName() == 'Vampires':
                if tempWeapon.getName() not in monster.getUnaffCandy():
                    monster.setHealth(monster.getHealth()-tmpAttValue)
            elif monster.getName() == 'Werewolves':
                if tempWeapon.getName() not in monster.getUnaffCandy():
                    monster.setHealth(monster.getHealth()-tmpAttValue)
            elif monster.getName() == 'Ghouls':
                if tempWeapon.getName() in monster.getAltCandy():
                    monster.setHealth(monster.getHealth()-(5*tmpAttValue))
                else:
                    monster.setHealth(monster.getHealth()-tmpAttValue)
            elif monster.getName() == 'Person':
                self.addWeapon()
            if monster.getHealth() <= 0:
                currHouse.deleteMonster(pos)
                currHouse.newPerson(pos)
            pos = pos +1



    def playerHealth(self):
        print("\nPlayer Health: {}".format(self.player.getHealth()))

    def totalMonsterCount(self):
        print("\nTotal Monsters Remaining: {}".format(self.neighborhood.getMonstersInHouses()))

    def addWeapon(self):
        if len(self.player.getInventory()) < 10:
            tempList = ['SourStraws', 'NerdBomb', 'ChocolateBars', 'HersheyKisses']
            weapon = randint(0,3)
            self.player.appendInventory(tempList[weapon])

    def monstersAttack(self):
        tmpAttValue = 0
        for i in self.neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()].getMonsters():
            tmpAttValue = tmpAttValue + i.getAttack()
            if i.getName() is 'Person':
                self.addWeapon()
        self.player.decreaseHealth(tmpAttValue)
        print("\nPlayer Attacked by the monster, yikes! Lost hp: {}".format(tmpAttValue))
    
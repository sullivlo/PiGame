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

    ''' run(self) runs the entire game. It contains two while loops. One is the actual
    game while loop that checks for if the game is over. The other while loop is for
    checking if the player is attacking. When the player attacks his turn is over.'''
    def run(self):
        print("\nOh No! You have woken up in your home today to find "+
            "that some of you family has been mutated to monsters.")
        print("\nBut it gets. You have walked outside and see that "+
            "some of your neighbors have had the same fate.")
        print("\nIt is your mission to not only save your family but"+
            " to save the entire neighborhood.")
        print("Using all of your Halloween candy change the monsters"+
            " back to your friends and family members.")
        print("\nHere is the map of the neighborhood. You are P. "+
            "\nIf a house is empty an E will display at its place."+
            " \nAll the houses that still have monsters will have an O.")


        while(self.gameover == False):
            print("\n---------------Player Turn----------------")
            self.display()
            attack = False
            while(attack == False):
                cmd = input("\nWhat action would you like to take?\n")
                cmd = cmd.lower()
                if cmd == "attack":
                    self.playerAttack()
                    attack = True
                elif cmd == "move":
                    self.move()
                    self.display()
                elif cmd == "inventory":
                    self.getInventory()
                elif cmd == "health":
                    self.playerHealth()
                elif cmd == "monstersleft":
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
                self.gameover = self.isGameOver()

    '''currentHome(self) prints the list of current monsters in a given home. If there is a person
    it will also print a person. If the house is empty it will state that as well.'''
    def currentHome(self):
        print("\nCurrent home has:")
        monst = self.neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()].getMonsters()
        if len(monst)==0:
            print("This house is empty.")
        for mon in monst:
            if mon.getName() is not 'Person':
                print("{name} with {health}".format(name = mon.getName(), health = mon.getHealth()))
            else:
                print("Person here.")

    '''display(self) is a method that calls all the individual items that need to be displayed for the
    user.'''
    def display(self):
        self.displayGrid()
        self.currentHome()
        self.displayOptions()

    '''displayOptions(self) displays the different options a user has.'''
    def displayOptions(self):
        print("\nThese are you options. Attacking ends your turn.")
        print("\nattack|move|inventory|health|monstersLeft|quit")

    '''displayGrid(self) prints the entire neighborhood that a user is in.
    If a house is empty it prints an E. If a house has a monster or person
    in it, it prints an O. If the user is at that home it prints a P.'''
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

    '''move(self) is the method that allows the user to traverse the
    neighborhood.'''
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


    '''isValidMove(self, nextPos) is used to decide if a move is valid. It is called
    by move when checking to see if the next position is on the grid. 
    - Returns True if the move is allowed.
    - Returns False if it is not.'''
    def isValidMove(self, nextPos):
        validMove = True
        if (nextPos == 'N') and (self.player.getPosY() == 0):
            validMove = False
        elif (nextPos == 'W') and (self.player.getPosX() == 0):
            validMove = False
        elif (nextPos == 'S') and (self.player.getPosY() == self.neighborhood.getGridLength()-1):
            validMove = False
        elif (nextPos == 'E') and (self.player.getPosX() == self.neighborhood.getGridLength()-1):    
            validMove = False
        return validMove

    '''isGameOver(self) is used to decide if the game is over. It checks
    the player's health, and then checks the total number of monsters in
    the neighborhood.
    - Returns True if the game is over.
    - Returns False if it is not.'''
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

    '''getInventory(self) is the method that calls the player class to print the
    player's Inventory.'''
    def getInventory(self): 
        print("\n---------------------- Inventory ------------------------")
        self.player.printInventory()

    '''getWeapon(self) prints the inventory and then asks the user for what weapon they
    want to use. If it is not a valid answer it asks again recurively.
    - Returns the Inventory slot number of the weapon.'''
    def getWeapon(self):
        self.getInventory()
        selected = 0
        try:
            selected = int(input("\nWhat weopon would you like to use?\nInput the Inventory Slot number.\n"))
            if selected < 0 or selected > len(self.player.getInventory()):
                print("Not a valid slot. Try again")
                selected = self.getWeapon()
        except ValueError as e:
            print("Not a valid slot. Try again")
            selected = self.getWeapon()
        return selected

    '''playerAttack(self) is the method that allows the user to attack all the weapons in a house.
    It finds the total attack value, and then checks each monster to see if it can attack that
    monster, and if it the attack has a special bonus.'''
    def playerAttack(self):
        selected = self.getWeapon()
        tempWeapon = self.player.getInventory()[selected]
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
            pos = pos +1
        if tempWeapon.getUses() == 0:
            self.player.deleteWeapon(selected)



    '''playerHealth(self) prints the player's health'''
    def playerHealth(self):
        print("\nPlayer Health: {}".format(self.player.getHealth()))

    '''totalMonsterCount(self): prints the total monsters in the neighborhood.'''
    def totalMonsterCount(self):
        print("\nTotal Monsters Remaining: {}".format(self.neighborhood.getMonstersInHouses()))

    '''addWeapon(self) is the method called to add a weapon to the player's inventory.'''
    def addWeapon(self):
        if len(self.player.getInventory()) < 10:
            tempList = ['SourStraws', 'NerdBomb', 'ChocolateBars', 'HersheyKisses']
            weapon = randint(0,3)
            self.player.appendInventory(tempList[weapon])

    '''monstersAttack(self) the method that allows the monsters to attack the player.'''
    def monstersAttack(self):
        tmpAttValue = 0
        for i in self.neighborhood.getHouses()[self.player.getPosX()][self.player.getPosY()].getMonsters():
            tmpAttValue = tmpAttValue + i.getAttack()
            if i.getName() is 'Person':
                self.addWeapon()
        self.player.decreaseHealth(tmpAttValue)
        print("\nPlayer Attacked by the monster, yikes! Lost hp: {}".format(tmpAttValue))
    
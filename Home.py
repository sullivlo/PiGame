from random import *
from NPCS import *
from Observable import *
from Observer import *

class Home(Observable, Observer):
	'''Home is an Observer of the monsters inside of it,
	as well as observed by the neighborhood it lies in. 
	A home can have up to 10 NPC's ranging from a person
	to the four different monsters. The population of a
	home is randomly generated and notifies when the
	population is changed.'''

	def __init__(self):
        Observable.__init__(self)
        Observer.__init__(self)
        self.monsters = popHome(self)

    def popHome(self):
    	monsterList = []
    	homePop = randint(0,10)
    	possibleMon = ['Person', 'Vampire', 'Werewolves','Zombie', 'Ghouls']
    	for numMon in range(0, homePop):
    		randSelected = randint(0, 4)
    		selected = possibleMon[randSelected]
    		if select == 'Person':
    			person = NPC.person() 
    			super.add_Observer(self, person)
    			monsterList.append(person)
    		if select == 'Vampire':
    			vampire = NPC.Vampires() 
    			super.add_Observer(self, vampire)
    			monsterList.append(vampire)
    		if select == 'Werewolves':
    			werewolves = NPC.Werewolves() 
    			super.add_Observer(self, werewolves)
    			monsterList.append(werewolves)
    		if select == 'Zombie':
    			zombie = NPC.Zombies() 
    			super.add_Observer(self, zombie)
    			monsterList.append(zombie)
    		if select == 'Ghouls':
    			ghouls = NPC.Ghouls() 
    			super.add_Observer(self, ghouls)
    			monsterList.append(ghouls)
    	return monsterList

    def getMonsters(self):
    	return self.monsters

    def numMonster(self):
    	total = 0
    	for numMonster in self.monsters:
    		if numMonster.getName() not in ['Person']:
    			total = total + 1
    	return total

    def newPerson(self, position):
    	person = NPC.person()
    	super.add_Observer(person)
    	self.monsters.insert(position, person)

    def deleteMonster(self, position):
    	del self.monsters[position]
    	self.newPerson(self, position)
    	self.update()

    def update(self):
    	super.notify()




from random import *
from NPCS.NPC import *


"""NPC observer that creates the ghouls object
init creates the NPC object with health, attack, unaffected Candy,
alt (string weapon), name, and is NPC alive"""
class Ghouls(NPC):
    '''Ghouls are monsters/NPCs who have a health between 40 - 80.
    as well they had an attack rating between 15 and 30. They are harmed
    by all weapons, but NerdBombs have five times an affect.'''


    def __init__(self):
        NPC.__init__(self)
        self.name = 'Ghouls'
        self.health = self.genHealth()
        self.attack = self.genAttack()
        self.unaffCandy = self.genUnaffCandy()
        self.altCandy = self.genAltCandy()
    '''Generates the health of the ghoul
    -return the ghouls health'''
    def genHealth(self):
        return randint(40, 80)
    '''Generates the attack of the ghoul
    -return the ghouls attack'''
    def genAttack(self):
        return uniform(15, 30)
    '''Generates the unattected candy of the ghoul
    -return list of ghouls unaffected candy'''
    def genUnaffCandy(self):
        return ['']
    '''Generates the altimate candy of the ghoul
    -return list of ghouls altimate candy'''
    def genAltCandy(self):
        return ['NerdBombs'] #5x        

                       

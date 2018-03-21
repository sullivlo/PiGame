from random import *
from NPCS.NPC import *

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
    
    def genHealth(self):
        return randint(40, 80)
    def genAttack(self):
        return uniform(15, 30)
    def genUnaffCandy(self):
        return ['']
    def genAltCandy(self):
        return ['NerdBombs'] #5x        

                       

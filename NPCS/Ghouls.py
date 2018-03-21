from random import *
from NPCS.NPC import *

class Ghouls(NPC):
    '''Ghouls are monsters/NPCs who have a health between 40 - 80.
    as well they had an attack rating between 15 and 30. They are harmed
    by all weapons, but NerdBombs have five times an affect.'''

    def __init__(self):
        super.__init__(self)
        super.setName(self, 'Ghouls')
        super.setHealth(self, genHealth(self))
        super.setUnaffCandy(self, genUnaffCandy(self))
        super.setAltCandy(self, genAltCandy(self))
    
    def genHealth(self):
        return random.uniform(40, 80)
    def genAttack(self):
        return random.uniform(15, 30)
    def genUnaffCandy(self):
        return ['']
    def genAltCandy(self):
        return ['NerdBombs'] #5x        
    
                       

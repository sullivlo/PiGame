from random import *
from Weapons.Weapon import *

class NerdBomb(Weapon):

    ''' NerdBomb provide an attack modifier between 3.5 - 5.
    They can be used a single time. '''

 
    def __init__(self):
        super.__init__(self)
        super.setModif(self, genModif(self))
        super.setUses(self, 1)
        super.setName(self, "NerdBomb")

    def genModif(self):
        return random.uniform(3.5, 5)

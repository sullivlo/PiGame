from random import *
from Weapons.Weapon import *

class NerdBomb(Weapon):

    ''' NerdBomb provide an attack modifier between 3.5 - 5.
    They can be used a single time. '''

 
    def __init__(self):
        Weapon.__init__(self)
        self.modif = self.genModif()
        self.uses = 1
        self.name = 'NerdBomb'

    def genModif(self):
        return random.uniform(3.5, 5)

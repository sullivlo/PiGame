from random import *
from Weapon import *

class NerdBomb(Weapon):

    ''' NerdBomb provide an attack modifier between 3.5 - 5.
    They can be used a single time. '''

    def __init__(self):
        Weapon.__init__(self)
        setModif(self, random.uniform(3.5, 5))
        setUses(self, 1)
        setName(self, "NerdBomb")

    def genModif(self):
        setModif(self, random.uniform(3.5, 5))
        return getModif(self)

from random import *
from Weapon import *

class SourStraws(Weapon):

    ''' SourStraws provide an attack modifier between 1 - 1.75.
    They can be used twice. '''

    def __init__(self):
        super.__init__(self)
        super.setModif(self, genModif(self))
        super.setUses(self, 2)
        super.setName(self, "SourStraws")

    def genModif(self):
        return random.uniform(1, 1.75)

from random import *
from Weapons.Weapon import *

class SourStraws(Weapon):

    ''' SourStraws provide an attack modifier between 1 - 1.75.
    They can be used twice. '''

    def __init__(self):
        super.__init__()
        super.setModif(self.genModif())
        super.setUses(2)
        super.setName("SourStraws")

    def genModif(self):
        return random.uniform(1, 1.75)

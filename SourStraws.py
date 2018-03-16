from random import *
from Weapons.Weapon import *

class SourStraws(Weapon):

    ''' SourStraws provide an attack modifier between 1 - 1.75.
    They can be used twice. '''

    def __init__(self):
        super.__init__(self)
        super.setModif(self, uniform(1, 1.75))
        super.setUses(self, 2)
        super.setName(self, "SourStraws")

    def genModif(self):
        super.setModif(self, uniform(1, 1.75))
        return super.getModif(self)
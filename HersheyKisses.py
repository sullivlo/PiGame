from random import *
from Weapons.Weapon import *

class HersheyKisses(Weapon):

    ''' HersheyKisses provide an attack modifier between 1.
    They can be used a million times. '''

    def __init__(self):
        super.__init__(self)
        super.setModif(self, 1)
        super.setUses(self, 1000000)
        super.setName(self, "HersheyKisses")

    def genModif(self):
        super.setModif(self, 1)
        return super.getModif(self)
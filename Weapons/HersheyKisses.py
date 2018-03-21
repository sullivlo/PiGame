from random import *
from Weapons.Weapon import *

class HersheyKisses(Weapon):

    ''' HersheyKisses provide an attack modifier between 1.
    They can be used a million times. '''

    def __init__(self):
        Weapon.__init__(self)
        Weapon.setModif(self, self.genModif())
        Weapon.setUses(self, 1000000)
        Weapon.setName(self, "HersheyKisses")

    def genModif(self):
        return 1


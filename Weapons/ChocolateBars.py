from random import *
from Weapons.Weapon import *

class ChocolateBars(Weapon):

    ''' ChocolateBars provide an attack modifier between 2 - 2.4.
    They can be used four times. '''

    def __init__(self):
       	Weapon.__init__(self)
        Weapon.setModif(self, self.genModif())
        Weapon.setUses(self, 4)
        Weapon.setName(self, 'ChocolateBars')

    def genModif(self):
        return uniform(2, 2.4)
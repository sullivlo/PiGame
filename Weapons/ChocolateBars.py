from random import *
from Weapons.Weapon import *

class ChocolateBars(Weapon):

    ''' ChocolateBars provide an attack modifier between 2 - 2.4.
    They can be used four times. '''

    def __init__(self):
        super.__init__(self)
        super.setModif(self, genModif(self))
        super.setUses(self, 4)
        super.setName(self, 'ChocolateBars')

    def genModif(self):
        return uniform(2, 2.4)
from random import *
from Weapons.Weapon import *

class ChocolateBars(Weapon):

    ''' ChocolateBars provide an attack modifier between 2 - 2.4.
    They can be used four times. '''

    def __init__(self):
       	Weapon.__init__(self)
        self.modif = self.genModif()
        self.uses = 4
        self.name = 'ChocolateBars'

    def genModif(self):
        return random.uniform(2, 2.4)
import math
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

    '''genModif(self) sets the modif value of the weapon to a
    random double between 2 and 2.4'''
    def genModif(self):
        return round(uniform(2, 2.4),2)
import math
from random import *
from Weapons.Weapon import *

class SourStraws(Weapon):

    ''' SourStraws provide an attack modifier between 1 - 1.75.
    They can be used twice. '''

    def __init__(self):
        Weapon.__init__(self)
        self.modif = self.genModif()
        self.uses = 2
        self.name = 'SourStraws'

    '''genModif(self) sets the modif value of the weapon to a
    random double between 1 and 1.75'''
    def genModif(self):
        return round(uniform(1, 1.75),2)

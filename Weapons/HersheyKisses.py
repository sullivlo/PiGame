import math
from random import *
from Weapons.Weapon import *

class HersheyKisses(Weapon):

    ''' HersheyKisses provide an attack modifier between 1.
    They can be used a million times. '''

    def __init__(self):
        Weapon.__init__(self)
        self.modif =  self.genModif()
        self.uses = 1000000
        self.name = 'HersheyKisses'

    '''genModif(self) sets the modif value to 1'''
    def genModif(self):
        return 1


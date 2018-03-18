from random import *
from Weapon import *

class HersheyKisses(Weapon):

    ''' HersheyKisses provide an attack modifier between 1.
    They can be used a million times. '''

    def __init__(self):
        Weapon.__init__(self)
        setModif(self, 1)
        setUses(self, 1000000)
        setName(self, "HersheyKisses")

    def genModif(self):
        setModif(self, 1)
        return getModif(self)

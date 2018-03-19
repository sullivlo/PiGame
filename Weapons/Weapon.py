from random import *

class Weapon(object):

    ''' Base Weapons class. '''

    def __init__(self):
        self.modif = 0
        self.uses = 0
        self.name = 'HersheyKisses'

    def getUses(self):
        return self.uses

    def getName(self):
        return self.name

    def getModif(self):
        return self.modif

    def setName(self, name):
        self.name = name

    def setUses(self, uses):
        self.uses = uses

    def setModif(self, modif):
        self.modif = modif

    def decreseUses(self):
        self.uses = self.uses - 1

    def genModif(self):
        pass

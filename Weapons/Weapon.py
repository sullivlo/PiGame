from random import *


"""Weapon is the observable class for all of the weapons
init creates the weapon object with uses, name, modifier, decrease uses"""

class Weapon(object):

    ''' Base Weapons class. '''

    def __init__(self):
        self.modif = 0
        self.uses = 0
        self.name = ''
    
    '''Gets the number of uses a weapon has left
    -return the uses left'''
    def getUses(self):
        return self.uses
    
    '''Gets the name of a weapon
    -return the weapons name'''
    
    def getName(self):
        return self.name
    
    '''Gets the modifer of the the weapon 
    -return the weapons modifer '''
    def getModif(self):
        return self.modif

    '''Sets the name of the weapon'''
   
    def setName(self, name):
        self.name = name
    
    '''Sets the uses of the weapon'''
    def setUses(self, uses):
        self.uses = uses
    
    '''Sets the weaon mod'''
    def setModif(self, modif):
        self.modif = modif
     
    '''modifies the uses by 1 for weapon'''
    def decreaseUses(self):
        if self.uses != 0:
            self.uses = self.uses - 1

    def genModif(self):
        pass

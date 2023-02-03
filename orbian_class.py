from math import pi
from random import shuffle, sample
from random import randint
import time

class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()

        # This is the only variable
        self.__adult = False

    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True

    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######

    def getName(self):
        return str(self.__NAME)
    
    def __gt__(self, other):
        return self.__getHeadVolume() + self.__getBodyVolume() > other.__getHeadVolume() + other.__getBodyVolume()

    def __getHeadRadius(self):
        return self.__HEAD_RADIUS
    
    def __getBodyRadius(self):
        return self.__BODY_RADIUS
    
    def __getBodyHeight(self):
        return self.__BODY_HEIGHT
    
    def __eq__(self,other):
        return self.__getBodyVolume() + self.__getHeadVolume() == other.__getBodyVolume() + other.__getHeadVolume()

    def getVolume(self):
        vol = self.__getBodyVolume() + self.__getHeadVolume()
        return round(vol)

    def getAge(self):
        age = (time.time() - self.__BIRTH_TIME) / 5
        return round(age)

    def __len__(self):
        return self.__BODY_HEIGHT + self.__HEAD_RADIUS * 2
    
    def __add__(self, other):
        __HEAD_RADIUS = (self.__HEAD_RADIUS + other.__HEAD_RADIUS) * .25
        __BODY_RADIUS = (self.__BODY_RADIUS + other.__BODY_RADIUS) * .25
        __BODY_HEIGHT = .125 * (len(self) + len(other))

        babyName = (self.getName() + other.getName() ).lower()
        babyName = "".join(sample(babyName, len(babyName)//2))

        babyOrbian = Orbian(babyName, __HEAD_RADIUS, __BODY_RADIUS, __BODY_HEIGHT)

        return babyOrbian


from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

        
"""The issue is that PenguinDuck and RubberDuck both cannot fly, 
    but they are definitely ducks (and most ducks CAN fly). 
    So code ends up duplicated. """

class Duck:
    
    def quack(self): #method inherited by all ducks (All good so far)
        print("All ducks can quack!")

    def display(self): #method that s reimplemented by every duck since they are displayed differently (All good so far)
        print("I'm a generic duck!")

    def fly(self): #another method that SHOULD is inherited by all ducks (oh-oh)
        print("I can fly!")

class WildDuck(Duck):

    def display(self):
        print("I'm a wild duck!")

class CityDuck(Duck):

    def display(self):
        print("I'm a city duck!")

class RubberDuck(Duck):

    def display(self):
        print("I'm a rubber duck!")

    def fly(self):
        """here, since all ducks should be able to fly, we might forget to re-implement the method"""
        print("I can't fly!!!")

class PenguinDuck(Duck):

    def display(self):
        print("I'm a rubber duck!")

    def fly(self): 
        """here we are forced to implement the fly method 
        even though it's a duplicate of RubberDuck's 
        (and we cannot just consider PenguinDuck a child of RubberDuck)"""
        print("I can't fly!!!")

def main():
    pass

if __name__ == "__main__":
    main()
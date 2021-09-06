from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)

"""The solution is to seperate the base classes (Decaf and Esspreso) 
from their expanded features (added topings) 
Each possible expansion being made into a seperate class (a seperate decorator). 
These classes (decorators) both ARE and HAVE a Beverage type class/object. 
The IS part of this is straight-forward: A Caramel is a beverage that should have caramel added. 
The HAS part simply means that the connection between Caramel and the base beverage is made 
through composition. (see main() for example)."""

class ABeverage(ABC): 
    """Base abstract Beverage class, to be expanded upon using decorators.
    Provides some useful implementations to it's children (like setter and getter for description)
    so it should be abstract, not an interface."""
    def __init__(self, desc: str) -> None:   
        self.description = desc

    def getDescription(self):
        return self.description

    def setDescription(self, new_desc):
        self.description = new_desc

    def cost(self):
        return 0

class Decaf(ABeverage):
    def __init__(self, desc) -> None:
        super().__init__(desc) 
    def cost(self):
        """Cost method now only has the responsibility of finguring out cost of a Decaf without any toppings"""
        return 3 
        
            
class Espresso(ABeverage):
    def __init__(self, desc) -> None:
        super().__init__(desc) 
    def cost(self):
        """Cost method now only has the responsibility of finguring out cost of an Espresso without any toppings"""
        return 2

class AAddonDecorator(ABeverage, ABC):
    """Base abstract Decorator class used to describe what all decorators should have.
    Note that decorators both ARE ABeverage and HAVE ABeverage (Inheritance + Composition)"""
    def __init__(self, beverage, desc: str) -> None:
        super().__init__(desc)
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + self.description

    def cost(self):
        return self.beverage.cost() 

class CaramelDecorator(AAddonDecorator):
    """Decorator for a beverage that should have some caramel added"""
    def __init__(self, beverage, desc: str) -> None:
        super().__init__(beverage, desc)

    def cost(self):
        """The cost method in the decorator is now free to only take into account the specific addon"""
        return self.beverage.cost() + 1

class ShotDecorator(AAddonDecorator):
    """Decorator for a beverage that should have a number of espresso shots added"""
    def __init__(self, beverage, desc: str, nr_of_shots: int) -> None:
        super().__init__(beverage, desc)
        self.shots = nr_of_shots

    def cost(self):
        """The cost method in the decorator is now free to only take into account the specific addon"""
        return self.beverage.cost() + 2*self.shots
   
def main():

    decaf = Decaf("For Normal Nancy")

    decaf_with_caramel = CaramelDecorator(decaf, " with caramel")

    print(f"First order: {decaf_with_caramel.getDescription()}, cost: {decaf_with_caramel.cost()}")

    espresso = Espresso("For Daredevil-David")

    espresso_extreme = ShotDecorator(espresso, " with 15 extra shots of espresso", 15)

    print(f"Second order: {espresso_extreme.getDescription()}, cost: {espresso_extreme.cost()}")

    espresso2 = Espresso("For Complicated Columbus")

    espresso2_complicated_p1 = CaramelDecorator(espresso2, " with caramel")
    
    espresso2_complicated_p2 = ShotDecorator(espresso2_complicated_p1, " with 2 extra shots of espresso", 2)

    print(f"Third order: {espresso2_complicated_p2.getDescription()}, cost: {espresso2_complicated_p2.cost()}")

if __name__ == "__main__":
    main()
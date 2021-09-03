from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)

class Problem:

    def __init__(self) -> None:
        """Describes the issue the pattern should solve and exemplifies a hierarchy in which the issue can be observed"""
        self.problem = "This pattern solves an instance where \n\
The Decorator pattern provides an alternative to subclassing for extending functionality. \n\
In the example, we want our beverages to have a lot of toppings available to them. \n\
A naive solution would be to create a class for each possible combination, but this would result in a class \n\
explosion (the number of classes in your program quickly rises needlessly. \n\
Another issue with the design that would be noticed quickly in practice would be instances \n\
where you have two orders of milk with one beverage (or 3 and so on and so forth).\n"

    class ABeverage(ABC): 
        def __init__(self, desc: str, has_soy: bool, has_milk: bool, has_caramel: bool) -> None:
            """Abstract class to model the common aspects of every beverage a customer may want"""
            self.description = desc
            self.has_soy = has_soy
            self.has_milk = has_milk 
            self.has_caramel = has_caramel

        def getDescription(self):
            return self.description

        def setDescription(self, new_desc):
            self.description = new_desc

        def cost(self):
            return 0


    class Decaf(ABeverage):
        def __init__(self, desc, has_soy: bool, has_milk: bool, has_caramel: bool) -> None:
            super().__init__(desc, has_soy, has_milk, has_caramel) 
        def cost(self):
            """Method to caculate the cost of a Decaf (with specific topics taken into account)"""
            pass 
            
                
    class Espresso(ABeverage):
        def __init__(self, desc, has_soy: bool, has_milk: bool, has_caramel: bool) -> None:
            super().__init__(desc, has_soy, has_milk, has_caramel) 
        def cost(self):
            """Method to caculate the cost of an Espresso (with specific topics taken into account)"""
            pass 

    class Tea(ABeverage): 
        """Oh-oh! tea doesn't come with caramel! (I think) 
        So using those boolean flags was a bad idea (over-specification just to accomodate bad design)"""

        def __init__(self, desc, has_soy: bool, has_milk: bool, has_caramel: bool) -> None:
            super().__init__(desc, has_soy, has_milk, has_caramel) 
        def cost(self):
            """Method to caculate the cost of a Tea (with specific topics taken into account)"""
            pass 

   
class Solution:
    def __init__(self) -> None:
        self.solution = "\nThe solution is to seperate the base classes (Decaf and Esspreso) \n\
from their expanded features (added topings) \n\
Each possible expansion being made into a seperate class (a seperate decorator). \n\
These classes (decorators) both ARE and HAVE a Beverage type class/object. \n\
The \"IS\" part of this is straight-forward: A Caramel is a beverage that should have caramel added. \n\
The \"HAS\" part simply means that the connection between Caramel and the base beverage is made \n\
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

    prob = Problem()
    sol = Solution()
    print(prob.problem, sol.solution)

    decaf = sol.Decaf("For Normal Nancy")

    decaf_with_caramel = sol.CaramelDecorator(decaf, " with caramel")

    print(f"First order: {decaf_with_caramel.getDescription()}, cost: {decaf_with_caramel.cost()}")

    espresso = sol.Espresso("For Daredevil-David")

    espresso_extreme = sol.ShotDecorator(espresso, " with 15 extra shots of espresso", 15)

    print(f"Second order: {espresso_extreme.getDescription()}, cost: {espresso_extreme.cost()}")

    espresso2 = sol.Espresso("For Complicated Columbus")

    espresso2_complicated_p1 = sol.CaramelDecorator(espresso2, " with caramel")
    
    espresso2_complicated_p2 = sol.ShotDecorator(espresso2_complicated_p1, " with 2 extra shots of espresso", 2)

    print(f"Third order: {espresso2_complicated_p2.getDescription()}, cost: {espresso2_complicated_p2.cost()}")

if __name__ == "__main__":
    main()
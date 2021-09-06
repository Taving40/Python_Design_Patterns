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

def main():
    pass

if __name__ == "__main__":
    main()
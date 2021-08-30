from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

class Problem:

    def __init__(self):
        """Describes the issue the pattern should solve and exemplifies a hierarchy in which the issue can be observed"""
        self.issue = "The issue is that PenguinDuck and RubberDuck both cannot fly, \n\
            but they are definitely ducks (and most ducks CAN fly). \n\
            So code ends up duplicated. \n"

    class Duck:
        def __init__(self):
            pass
        
        def quack(self): #method inherited by all ducks (All good so far)
            print("All ducks can quack!")

        def display(self): #method that s reimplemented by every duck since they are displayed differently (All good so far)
            print("I'm a generic duck!")

        def fly(self): #another method that SHOULD is inherited by all ducks (oh-oh)
            print("I can fly!")

    class WildDuck(Duck):
        def __init__(self):
            pass

        def display(self):
            print("I'm a wild duck!")

    class CityDuck(Duck):
        def __init__(self):
            pass

        def display(self):
            print("I'm a city duck!")

    class RubberDuck(Duck):
        def __init__(self):
            pass

        def display(self):
            print("I'm a rubber duck!")

        def fly(self): #here, bcs all ducks should be able to fly, we might forget to re-implement
            print("I can't fly!!!")
    
    class PenguinDuck(Duck):
        def __init__(self):
            pass

        def display(self):
            print("I'm a rubber duck!")

        def fly(self): #here we are forced to implement the fly method even though it's a duplicate of RubberDuck's (and we cannot just consider PenguinDuck a child of RubberDuck)
            print("I can't fly!!!")

class Solution:

    def __init__(self):
        self.solution = "The solution is to turn the fly method into an interface in the base class \n\
            to ensure that every child Duck class implements it (since all Ducks should have something to do with flying) \n\
            but we create a separate interface for every type of behaviour that the fly interface can take \n\
            and each child implements one of those.\n"

    class IFlyStrategy(ABC):

        @abstractmethod
        def fly(self):
            pass
    
    class ConcreteStrategyFlyCannot(IFlyStrategy):
        def fly(self):
            print("I can't fly!!!")

    class ConcreteFlyStrategyCan(IFlyStrategy):
        def fly(self):
            print("I can fly!!!")

    class Duck:
        def __init__(self, fly_strategy):
            self._fly_strategy = fly_strategy

        def quack(self): 
            print("All ducks can quack!")

        def display(self): 
            print("I'm a generic duck!")

        def fly(self): 
            self._fly_strategy.fly()

    class WildDuck(Duck):
        def __init__(self, fly_strategy):
            self._fly = fly_strategy

        def display(self):
            print("I'm a wild duck!")

    class CityDuck(Duck):
        def __init__(self, fly_strategy):
            self._fly = fly_strategy

        def display(self):
            print("I'm a city duck!")

    class RubberDuck(Duck):
        def __init__(self, fly_strategy):
            self._fly = fly_strategy

        def display(self):
            print("I'm a rubber duck!")

    
    class PenguinDuck(Duck):
        def __init__(self, fly_strategy):
            self._fly = fly_strategy

        def display(self):
            print("I'm a rubber duck!")

def main():

    prob = Problem()
    print(prob.issue)
    sol = Solution()
    print(sol.solution)
    
    simple_duck = sol.Duck(sol.ConcreteFlyStrategyCan())
    simple_duck.fly()

    rubber_duck = sol.Duck(sol.ConcreteStrategyFlyCannot())
    rubber_duck.fly()


if __name__ == "__main__":
    main()
    
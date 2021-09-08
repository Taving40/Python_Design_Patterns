from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""The solution is to turn the fly method into an interface in the base class 
    to ensure that every child Duck class implements it (since all Ducks should have something to do with flying) 
    but we create a separate interface for every type of behaviour that the fly interface can take 
    and each child implements one of those."""


class IFlyStrategy(ABC):
    """Interface for Strategy type classes that model the flying behavior"""
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
    
    simple_duck = Duck(ConcreteFlyStrategyCan())
    simple_duck.fly()

    rubber_duck = Duck(ConcreteStrategyFlyCannot())
    rubber_duck.fly()

if __name__ == "__main__":
    main()
    
from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from random import randrange

"""This pattern is useful when instantiating objects (so generally always useful) 
It encapsulates the instantiation of objects so that it becomes uniform across all classes.
Note: especially useful when you need to do some logic to instantiate an object or 
when you want to switch the way you instantiate objects at run-time (polymorphism)"""

class IAnimal(ABC):
    def sound(self):
        pass
    def __str__(self) -> str:
        pass

class Dog(IAnimal):
    def sound(self):
        return "bark"
    def __str__(self) -> str:
        return "dog"

class Cat(IAnimal):
    def sound(self):
        return "meow"
    def __str__(self) -> str:
        return "cat"
            

def main():

    """Let's say we wish to instantiate a random number of cats and a random number of dogs."""
    warm_household = []
    for _ in range(randrange(10)):
        warm_household.append(Cat())

    for _ in range(randrange(15)):
        warm_household.append(Dog())

    print(list(map(str,warm_household)).count("dog"), "dogs")
    print(list(map(str,warm_household)).count("cat"), "cats \n\n\n")
        

    """Let's say we wish to instantiate a random number of cats and the same number of dogs."""
    warm_household = []
    for _ in range(randrange(15)):
        warm_household.append(Cat())
        warm_household.append(Dog())
    
    print(list(map(str,warm_household)).count("dog"), "dogs")
    print(list(map(str,warm_household)).count("cat"), "cats \n\n\n")

    """Let's say we wish to instantiate a random number of all cats OR all dogs (randomly choosing between one or the other)"""
    warm_husehold = []
    flag = randrange(0, 1)
    if flag:
        for _ in range(randrange(15)):
            warm_husehold.append(Dog())
    else:
        for _ in range(randrange(15)):
            warm_husehold.append(Cat())

    print(list(map(str,warm_household)).count("dog"), "dogs")
    print(list(map(str,warm_household)).count("cat"), "cats \n\n\n")

    """We quickly see that there are multiple ways we might wish to instantiate the objects.
    We will also quite likely like to repeat those ways of instantiating them.
    So, encapsulating this behavior would be for the best."""

if __name__ == "__main__":
    main()
from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""The Facade pattern is a class which interacts with all the "plumbing" of your hierarchy,
letting your clients (other pieces of code) interact with the complex part through an easier to use medium.
(Useful when your hierarchy is very decoupled).
((When following the "singluar responsibility" principle, you might end up with a lot of classes))."""

class IFacade(ABC):
    def __init__(self):
        """The Facade should either create the objects it needs or be provided with them"""
        pass

class ConcreteFacade(IFacade):
    def __init__(self, obj_a=None, obj_b=None, obj_c=None):
        self.obj_a = obj_a 
        self.obj_b = obj_b 
        self.obj_c = obj_c 
        if obj_a is None:
            self.obj_a = ConcreteA()
            self.obj_b = ConcreteB()
            self.obj_c = ConcreteC()
            self.obj_a.obj_b = self.obj_b
            self.obj_b.obj_c = self.obj_c
            self.obj_c.obj_b = self.obj_b

    def do_logic(self, request):
        self.obj_c.do_logic(request)
        self.obj_b.do_logic()
        self.obj_a.do_logic()

class IA(ABC):
    """Class A does not make sense without a reference to an object B"""
    def __init__(self, obj_b):
        pass

class ConcreteA(IA):
    def __init__(self, obj_b=None):
        self.obj_b = obj_b
        self.x = 0

    def do_logic(self):
        self.x = self.obj_b.x + 1
        print(f"Did logic in A, based off B. a.x:{self.x}")

class IB(ABC):
    """Class B does not make sense without a reference to an object C"""
    def __init__(self, obj_c):
        pass

class ConcreteB(IB):
    def __init__(self, obj_c=None):
        self.obj_c = obj_c
        self.x = 0
    
    def do_logic(self):
        self.x += 1
        print(f"Did logic in B, which took into account C: b.x:{self.x}")

class IC(ABC):
    """Class C does not make sense without a reference back to the associated object B"""
    def __init__(self, obj_b):
        self.obj_b = obj_b

class ConcreteC(IC):
    def __init__(self, obj_b=None):
        self.obj_b = obj_b
        self.x = 0
    
    def do_logic(self, request):
        self.x += 1
        print(f"Did logic in C, for client request: {request}. c.x: {self.x}")
        self.obj_b.do_logic()

def main():
    """In this example, the main function acts as a client."""
    facade = ConcreteFacade()

    facade.do_logic("hello")

if __name__ == '__main__':
    main()
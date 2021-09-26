from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""This pattern pairs a ConcreteAbstraction with a ConcreteImplementor, letting other classes
inheriting from AAbstraction vary independently. Same with other classes inhereting from IImplementor. 
Note: In practice you would have more ConcreteAbstraction and ConcreteImplementor classes.
The problem this pattern solves becomes clear when you consider the AAbstraction children classes
and the IImplementor children classes as two sets. By decoupling you essentially can combine any
AAbstraction with any IImplementor. If we had not done this, we would have needed a new (abstraction, implementation)
tuple for every possible combination that this pattern offers."""

class AAbstraction(ABC):
    """Abstract class parent for ConcreteAbstraction.
    All children of AAbstraction MUST HAVE a child of IImplementor."""
    pass

class ConcreteAbstraction(AAbstraction):
    """An example of a ConcreteAbstraction, which needs to have a ConcreteImplementor"""
    pass

class IImplementor(ABC):
    """Interface for all implemnetations we might have."""
    pass

class ConcreteImplementor(IImplementor):
    """An example of a ConcreteImplementor, which needs to be given to a  ConcreteAbstraction"""
    pass

def main():
    pass

if __name__ == '__main__':
    main()
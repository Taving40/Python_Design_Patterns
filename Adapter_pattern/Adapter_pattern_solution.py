from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""The Adapter pattern is essentially a wrapper around an interface implementation
so that it makes it compatible with another interface.
The Adapter implements the interface that the client wants to use (ITarget)
and adapts the corresponding methods in Adaptee so that it makes sense.
Note: The behavior that the client wants is within the Adaptee's method.
The Adapter DOES NOT CHANGE that behavior, 
the client simply cannot access it any other way (or it wouldn't be smart to do so)"""

class ITarget(ABC):
    @abstractmethod
    def request(self) -> None:
        """The "signature" of the class that it would implement this interface.
        This is the standard that a client would expect to be able to make use of."""
        pass

class ISource(ABC):
    @abstractmethod
    def request_but_different(self):
        pass

class Adapter(ITarget):
    """Is repsonsible for implementing the request method for
    in a way that is compatible with what the client wants
    and what the Adaptee provides."""
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self) -> None:
        self.adaptee.request_but_different()

class Adaptee(ISource):
    """The Adaptee is the implementation of the interface that we want to adapt."""
    def request_but_different(self):
        """A concrete example of this pattern's usefulness would be :
        -when you think you might wish to change this method (request_but_different) in the future,
        but want the client using it to not see any difference
        -when this Adaptee is an external library you don't have control over
        and you might want to change that library in the future
        -when the ITarget "request" method is a standard used frequently """
        
        print("Print from Adaptee")

def main():
    """In this instance, let's say the main function is the client."""

    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(type(adapter.__class__)) 
    """notice that this can be (and that's the main point of the pattern) treated as ITarget through polymorphism"""
    adapter.request()

if __name__ == '__main__':
    main()
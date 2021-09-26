from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""This example models a site with 2 different display options (perhaps one for mobile and one for desktops).
In each "View" there can be different MediaResources (either an Artist ((musician)) or a book,
which have different implementations).
To handle all of this without the bridge pattern we would need 4 different classes,
however, if we wished to expand the number of views or the number of MediaResources (which is a likely possibility)
that number would grow very quickly. USING the bridge pattern, we need only add one extra class each time."""

class AView(ABC):
    """Abstract class parent for ConcreteAbstraction.
    All children of AAbstraction MUST HAVE a child of IImplementor."""
    def __init__(self, media_resource) -> None:
        self.media_resource = media_resource

    @abstractmethod
    def display():
        """Display method that puts all the fields on the screen in the order they are supposed to go."""
        pass

class LongView(AView):
    """An example of a ConcreteAbstraction, which needs to have a ConcreteImplementor"""
    def display():
        pass

class ShortView(AView):
    """An example of a ConcreteAbstraction, which needs to have a ConcreteImplementor"""
    def display():
        pass

class IMediaResource(ABC):
    """Interface for all implemnetations we might have."""
    pass

class Artist(IMediaResource):
    """An example of a ConcreteImplementor, which needs to be given to a  ConcreteAbstraction"""
    pass

class Book(IMediaResource):
    """An example of a ConcreteImplementor, which needs to be given to a  ConcreteAbstraction"""
    pass

def main():
    pass

if __name__ == '__main__':
    main()
from __future__ import annotations
from abc import ABC, abstractmethod

""" """

class AbstractClass(ABC):
    def TemplateMethod(self):
        """We can say structurally what this method should do, but not in detail.
        This is why we let operation1 and operation2 be implemented by a concrete class instead."""
        '''some logic''' #Should take care since this part, between the varying operations
        self.operation1()
        '''some logic''' #Shouldn't really change, meaning that this is somewhat dangerous
        self.operation2()
        '''some logic''' #Because it makes assumptions about the future of the codebase
   
    @abstractmethod
    def operation1(self):
        pass
   
    @abstractmethod
    def operation2(self):
        pass

class ConcreteClass(AbstractClass):
    """Is responsible for implementing opeartion1 and opeartion2."""
    def opeartion1(self):
        pass

    def operation2(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
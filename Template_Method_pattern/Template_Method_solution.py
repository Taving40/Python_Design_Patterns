from __future__ import annotations
from abc import ABC, abstractmethod

""" This pattern provides a way to change what varies in a certain algorithm from case to case. 
The things that are varying should be relating to behavior, not just parameters."""

class AbstractClass(ABC):
    def TemplateMethod(self):
        """We can say structurally what this method should do, but not in detail.
        This is why we let operation1 and operation2 be implemented by a concrete class instead."""
        '''some logic'''
        self.operation1()
        '''some logic'''
        self.operation2()
        '''some logic'''
   
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

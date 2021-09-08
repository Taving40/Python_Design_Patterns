from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""The solution is to have the Observer object notify the other Observable objects 
    not the other way around, since that would be incredibly resource consuming.
    For this we need the Observables to register with the Observer (so it knows who to notify)."""

class IObservable(ABC): 
    """Interface base for Observable classes"""
    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setState(self, state):
        pass

    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class IObserver(ABC): 
    """Interface for Observer type classes"""
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def update(self):
        pass

class ConcreteObservable(IObservable):
    def __init__(self, state) -> None:
        self.state = state
        self.observers = []

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        self.notify()
    
    def add(self, observer):
        self.observers.append(observer)
    
    def add(self, observers: list):
        self.observers.extend(observers)

    def add(self, observers: tuple):
        self.observers.extend(observers)
    
    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.state)

class ConcreteObserver(IObserver):
    def __init__(self, data) -> None:
        self.data = data
        
    def update(self, new_data):
        self.data = new_data

def main():

    observable = ConcreteObservable("current")
    observer1, observer2, observer3 = ConcreteObserver(observable.getState()), ConcreteObserver(observable.getState()), ConcreteObserver(observable.getState())
    observable.add((observer1, observer2, observer3))
    print(f"Observers now have the following data about Observable: {observer1.data}, {observer2.data}, {observer3.data}")
    observable.setState("new")
    print(f"Observers now have the following data about Observable: {observer1.data}, {observer2.data}, {observer3.data}")

if __name__ == "__main__":
    main()
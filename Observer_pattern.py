from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

#TODO: look at type of relationship between concrete observable and observer
#ideally: observer holds a reference to observable and it uses that to update itself after it has been notified
class Problem:

    def __init__(self) -> None:
        """Describes the issue the pattern should solve and exemplifies a hierarchy in which the issue can be observed"""
        self.problem = "This pattern solves an instance where you have an Observable object that changes state \n\
        and many other Observer objects that need to be notified (and updated) when that happens.\n"

    class Observable:

        def __init__(self, state) -> None:
            self.state = state

        def getState(self):
            return self.state

        def setState(self, state):
            self.state = state

    class Observer:
        def __init__(self, data) -> None:
            self.data = data

        def update(self, new_data):
            self.data = new_data    

class Solution:
    def __init__(self) -> None:
        self.solution = "The solution is to have the Observer object notify the other Observable objects \n\
        not the other way around, since that would be incredibly resource consuming.\n\
        For this we need the Observables to register with the Observer (so it knows who to notify).\n"

    class IObservable(ABC): #"Interface" base for Observable classes

        def __init__(self) -> None:
            pass

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

        def notify(self):
            pass

    class IObserver(ABC): #"Interface" base for Observer classes
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

    prob = Problem()
    sol = Solution()
    print(prob.problem, sol.solution)

    observable = sol.ConcreteObservable("current")
    observer1, observer2, observer3 = sol.ConcreteObserver(observable.getState()), sol.ConcreteObserver(observable.getState()), sol.ConcreteObserver(observable.getState())
    observable.add((observer1, observer2, observer3))
    print(f"Observers now have the following data about Observable: {observer1.data}, {observer2.data}, {observer3.data}")
    observable.setState("new")
    print(f"Observers now have the following data about Observable: {observer1.data}, {observer2.data}, {observer3.data}")

if __name__ == "__main__":
    main()
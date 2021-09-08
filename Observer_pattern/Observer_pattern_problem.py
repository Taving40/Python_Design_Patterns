from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod

"""This pattern solves an instance where you have an Observable object that changes state 
    and many other Observer objects that need to be notified (and updated) when that happens."""

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

def main():
    pass
    
if __name__ == "__main__":
    main()
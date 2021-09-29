from __future__ import annotations
from abc import ABC, abstractmethod

""" Sometimes you don't want to care about whether you're dealing with a single unitary object
or a COMPOSITE object (a collection of objects for example). This pattern allows you to do that.
When you have some data that you can organize into a hierarchy, performing computation over that 
data becomes trivial using Composite pattern. 
This hierarchy models a to-do list manager."""

class TodoList(ABC):
    """Interface for both composite and unitary objects that make up the desired tree structure.
    Through polymorphism, we can apply computation to those objects, without caring about their type."""
    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def uncheck(self):
        pass
    """There is a discussion to be had about potentially adding "Add" and "Remove" methods to TodoList
    One point against this would be that Todo objects would end up depending on methods that they have no business
    using in any context. Adding the Add and Remove methods to Project instead would screw up the whole concept of this pattern.
    A recommended solution is to make the hierarchy immutable."""

class Todo(TodoList):
    """Base object that is not a Composite"""
    def __init__(self):
        self.checked = False

    def check(self):
        self.checked = True

    def uncheck(self):
        self.checked = False

class Project(TodoList):
    """Example of a Composite object"""
    def __init__(self, *todo_list):
        self.checked = False
        self.todo_list = todo_list

    def check(self):
        self.checked = True
        for todo in self.todo_list:
            todo.check()
    
    def uncheck(self):
        self.checked = False
        for todo in self.todo_list:
            todo.uncheck()


def main():
    leaf1 = Todo()
    leaf2 = Todo()
    node1 = Project(leaf1, leaf2)
    leaf3 = Todo()
    node2 = Project(leaf3)
    root = Project(node1, node2)

    root.check()
    print("Smallest task status after checking the associated project as done: ", leaf1.checked)
    root.uncheck()
    print("Smallest task status after unchecking the associated project as done: ", leaf1.checked)

if __name__ == '__main__':
    main()
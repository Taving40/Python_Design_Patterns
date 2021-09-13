from __future__ import annotations
from abc import ABC, abstractmethod #abstract base class (deriving from this results in an abstract class)
from time import sleep

"""This example models a porgammable remote (the Invoker) for a set of lights (the Receivers)"""

class Invoker:
    """The Invoker has ICommand(s) which it can call upon to act upon the Receiver(s)
    (Specific to context)"""
    def __init__(self, command_on_off = None, command_flicker = None) -> None:
        self.__command_on = command_on_off
        self.__command_flicker = command_flicker
    def setCommandOnOff(self, command):
        self.__command_on = command
    def setCommandFlicker(self, command):
        self.__command_flicker = command
    def doCommandOnOff(self):
        self.__command_on.execute()
    def undoCommandOnOff(self):
        self.__command_on.unexecute()
    def doCommandFlicker(self):
        self.__command_flicker.execute()
    def undoCommandFlicker(self):
        self.__command_flicker.unexecute()
    

class ICommand(ABC):
    """Interface for the Command(s). 
    (Generally the same in any context you might want to use Command pattern in)"""
    @abstractmethod
    def __init__(self) -> None:
        pass
    @abstractmethod
    def execute(self) -> None:
        pass
    @abstractmethod
    def unexecute(self) -> None:
        pass

class ConcreteCommandOnOff(ICommand):
    """Actual Command that we wish to enact."""
    def __init__(self, *receiver_lights) -> None:
        """The Command can be associated with some lights and not others, since the remote is fully configurable"""
        self.__receiver_lights = receiver_lights
    def execute(self) -> None:
        for light in self.__receiver_lights:
            light.On()
    def unexecute(self) -> None:
        for light in self.__receiver_lights:
            light.Off()

class ConcreteCommandFlicker(ICommand):
    def __init__(self, *receiver_lights) -> None:
        """The Command can be associated with some lights and not others, since the remote is fully configurable"""
        self.__receiver_lights = receiver_lights
    def execute(self):
        for light in self.__receiver_lights:
            light.On()
        for _ in range(5):
            sleep(1)
            for light in self.__receiver_lights:
                light.Off()
            sleep(1)
            for light in self.__receiver_lights:
                light.On()
    def unexecute(self):
        for light in self.__receiver_lights:
            light.Off()
        for _ in range(5):
            sleep(1)
            for light in self.__receiver_lights:
                light.On()
            sleep(1)
            for light in self.__receiver_lights:
                light.Off()

class ReceiverLight:
    """The Receiver is the end object that gets acted upon
    (Specific to context)"""
    def __init__(self, name) -> None:
        self.name = name
        self.on = False
    def On(self):
        self.on = True
    def Off(self):
        self.on = False


def main():
    light1, light2 = ReceiverLight("Livingroom"), ReceiverLight("Kitchen")
    on_off = ConcreteCommandOnOff(light1, light2)
    flicker = ConcreteCommandFlicker(light1)
    remote = Invoker(on_off, flicker)

    """Similarly to the Strategy pattern, the Commands can vary independently from the "Clients" 
    (either the Invoker, or some other bigger context that makes use of a set of Invokers) """

    print(f"Livingroom light is on: {light1.on}\nKitchen light is on: {light2.on}\n")

    remote.doCommandOnOff()

    print(f"Livingroom light is on: {light1.on}\nKitchen light is on: {light2.on}\n")

    remote.undoCommandOnOff()

    print(f"Livingroom light is on: {light1.on}\nKitchen light is on: {light2.on}\n")


if __name__ == '__main__':
    main()
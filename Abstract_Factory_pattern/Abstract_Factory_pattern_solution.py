from __future__ import annotations
from abc import ABC #abstract base class (deriving from this results in an abstract class)
from abc import abstractmethod
import sys as sys
"""The Abstract Factory pattern provides an interface for creating
FAMILIES of related or dependent objects.
(Useful when building UI controls for different OSes)
((Where you'd have a family of buttons/etc for each platform))"""

class IFactory(ABC):
    @abstractmethod
    def getAlert(self):
        pass
    @abstractmethod
    def getButton(self):
        pass

class ConcreteFactoryLinux(IFactory):
    def getAlert(self) -> ConcreteAlertLinux:
        return ConcreteAlertLinux()
    def getButton(self) -> ConcreteButtonLinux:
        return ConcreteButtonLinux()

class ConcreteFactoryWindows(IFactory):
    def getAlert(self) -> ConcreteAlertWindows:
        """do some logic related to alerts..."""
        return ConcreteAlertWindows("I'm a Windows alert!", True)
    def getButton(self) -> ConcreteButtonWindows:
        return ConcreteButtonWindows()

class IButton(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def press(self):
        pass

class IAlert(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def alert(self):
        pass

class ConcreteAlertLinux(IAlert):
    def __init__(self, description):
        self.description = description

    def alert(self):
        print("I'm a Linux alert!")

class ConcreteAlertWindows(IAlert):
    def __init__(self, description, will_force_update):
        self.description = description
        self.will_force_update = will_force_update

    def alert(self):
        print("I'm a Windows alert!")
        if self.will_force_update:
            self.force_update()

    def force_update(self):
        print("Forcing update...")
        sys.exit(0)

class ConcreteButtonLinux(IButton):
    def __init__(self, requires_privilege: bool):
        self.pressed = False
        self.requires_privilege = requires_privilege
    def press(self):
        self.pressed = True
        print("I'm a Linux button!")
        self.pressed = False

class ConcreteButtonWindows(IButton):
    def __init__(self):
        self.pressed = False
    def press(self):
        self.pressed = True
        print("I'm a Windows button!")
        self.pressed = False


def main():
    windows_factory = ConcreteFactoryWindows()

    windows_button = windows_factory.getButton()
    windows_button.press()
    """Now that we have a windows button, 
    let's say we wish to also add an alert to it"""
    windows_alert = windows_factory.getAlert()
    """Notice how there is no danger for us to build a Linux alert
    since the factory is designed specifically for windows UI elements""" 
    windows_alert.alert()
    print("All my homies hate Windows")

if __name__ == '__main__':
    main()
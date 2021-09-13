# Naming conventions

* class starting with "I" - interface (does not have implementations, cannot be instantiated)
* class starting with "A" - abstract (may have implementations, cannot be instantiated)
* class starting with "Concrete" - instantiable class derived from abstract class or interface

## Summary

* [Strategy pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Strategy_pattern): This pattern defines a family of algorithms, encapsulates each one and makes them **INTERCHANGEABLE**. "Strategy" let's the algorithm vary independently from "clients" (other classes which need a form of that algorithm) that use it. 

* [Observer pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Observer_pattern): This pattern defines a **One-to-Many dependency between objects**, so that when one object changes state, all of its dependencies are notified and updated automatically.

* [Decorator pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Decorator_pattern): This pattern attaches additional responsibilities to an object **DYNAMICALLY**. Decorators provide a flexible alternative to subclassing for extending functionality.

* [Factory Method pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Factory_Method_pattern): This pattern defines an **INTERFACE FOR CREATING AN OBJECT**, but lets sublcasses decide WHICH class to instantiate. Factory Method pattern lets a class defer instantiation to subclasses.

* [Abstract Factory pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Abstract_Factory_pattern): This pattern provides an interface for creating **FAMILIES OF DEPENDENT OR RELATED OBJECTS**, without specifying their concrete classes. (basically the abstract factory pattern is a set of Factory Methods)

* [Singleton pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Singleton_pattern): This pattern ensures a class has **only one instace** and provides a global point of access to it. ([critique](https://www.youtube.com/watch?v=-FRm3VPhseI), as I understand it: you should avoid globals and if your app is growing, you might wish to have multiple instances of what you initially thought would only ever be a single thing)

* [Command pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Command_pattern): This pattern encapsulates a request as an object thereby letting you parameterize other objects with different requests and support undoable operations.

## Resources

Example ideas taken from Head First: Design Patterns and Christopher Okhravi's youtube series: [Design Patterns](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)

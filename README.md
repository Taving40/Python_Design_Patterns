# About

* A few brief examples of common design patterns implemented in python. These examples are meant to be used as a starting point for serious implementations.

## Naming conventions

* class starting with "I" - interface (does not have implementations, cannot be instantiated)
* class starting with "A" - abstract (may have implementations, cannot be instantiated)
* class starting with "Concrete" - instantiable class derived from abstract class or interface
* client - piece of code (usually encapsulated) that will make use of another class (it's being "serviced" by it).

## Summary

* [Strategy pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Strategy_pattern): This pattern defines a family of algorithms, encapsulates each one and makes them **interchangeable**. "Strategy" let's the algorithm vary independently from "clients" (other classes which need a form of that algorithm) that use it.

* [Observer pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Observer_pattern): This pattern defines a **One-to-Many dependency between objects**, so that when one object changes state, all of its dependencies are notified and updated automatically.

* [Decorator pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Decorator_pattern): This pattern attaches additional responsibilities to an object **dynamically**. Decorators provide a flexible alternative to subclassing for extending functionality.

* [Factory Method pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Factory_Method_pattern): This pattern defines an **interface for creating an object**, but lets sublcasses decide WHICH class to instantiate. Factory Method pattern lets a class defer instantiation to subclasses.

* [Abstract Factory pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Abstract_Factory_pattern): This pattern provides an interface for creating **families of dependent or related objects**, without specifying their concrete classes. (basically the abstract factory pattern is a set of Factory Methods)

* [Singleton pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Singleton_pattern): This pattern ensures a class has **only one instace** and provides a global point of access to it. ([critique](https://www.youtube.com/watch?v=-FRm3VPhseI), as I understand it: you should avoid globals and if your app is growing, you might wish to have multiple instances of what you initially thought would only ever be a single thing)

* [Command pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Command_pattern): This pattern **encapsulates a request** as an object thereby letting you parameterize other objects with different requests and support undoable operations.

* [Adapter pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Adapter_pattern): This pattern converts the interface of a class into another interface that clients expect. Adapter **lets classes work together** that couldn't otherwise because of incompatible interfaces.

* [Facade pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Facade_pattern): This pattern provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher level interface that **makes the subsystem easier to use**.

* [Proxy pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Proxy_pattern): This pattern provides a surrogate (placeholder) for another object to **control access** to it.

* [Bridge pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Bridge_pattern): This pattern **decouples** an **abstraction** from its **implementation** so that the two can vary independently.

* [Template Method pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Template_Method_pattern): This pattern defines the **skeleton** of an algorithm, **differing some steps** to sublcasses. Tempalte method lets sublclasses redefine certains teps of an algorithm without changing the algorithm structure.

* [Composite pattern](https://github.com/Taving40/Python_Design_Patterns/tree/main/Composite_pattern): This pattern composes objects into **tree structures** to represent "part-whole" (any object is part of the whole and the whole is made of parts) hierarchies. Composite lets clients **treat** individual objects and compositions of objects **uniformly**.

## Resources

Example ideas taken from Head First: Design Patterns and Christopher Okhravi's youtube series: [Design Patterns](https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc)

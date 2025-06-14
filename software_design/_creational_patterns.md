
# Creational design patterns
They provide object creation mechanisms that increase flexibility and reuse of existing code.

<br>

## Factory Method
**Provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.**

### 🚨 The problem
Imagine that you’re creating a logistics management application. The first version of your app can only handle transportation by trucks, but ater a while your app becomes popular, and you receive requests from sea transportation companies to incorporate sea logistics into the app.

At present, most of your code is coupled to the `Truck` class. Adding `Ships` into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

### ✅ The solution
This pattern suggests that you replace direct object construction calls (using the new operator) with calls to a special factory method. The objects are still created via the new operator, but it’s being called from within the factory method. Objects returned by a factory method are often referred to as products.

Creator classes:

![Factory method creator classes](images/factory_metod1.png)

Product classes:

![Factory method product classes](images/factory_metod2.png)

The code that uses the factory method (often called the client code) doesn’t see a difference between the actual products returned by various subclasses. The client treats all the products as abstract Transport. The client knows that all transport objects are supposed to have the deliver method, but exactly how it works isn’t important to the client.

### 🛠️ Structure

![Factory method Structure](images/factory_metod3.png)

- The `Product` interface is common to all objects that can be produced by the creator and its subclasses.
- `Concrete Products` are different implementations of the product interface.
- The `Creator` class declares the factory method that returns new product objects. It’s important that the return type of this method matches the product interface. You can declare the factory method as abstract to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type. Note, despite its name, product creation is not the primary responsibility of the creator. Usually, the creator class already has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes. Here is an analogy: a large software development company can have a training department for programmers. However, the primary function of the company as a whole is still writing code, not producing programmers
- `Concrete Creators` override the base factory method so it returns a different type of product. Note that the factory method doesn’t have to create new instances all the time. It can also return existing objects from a cache, an object pool, or another source.

### 💡 Applicability
Use the Factory Method when:
- you don’t know beforehand the exact types and dependencies of the objects your code should work with
- you want to provide users of your library or framework with a way to extend its internal components
- you want to save system resources by reusing existing objects instead of rebuilding them each time

### ⚖️ Pros & Cons
| Pros | Cons |
| ---- | ---- |
| Avoids tight coupling between the creator and the concrete products | The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes. |
| Single Responsibility Principle: you can move the product creation code into one place in the program, making the code easier to support |  |
| Open/Closed Principle: you can introduce new types of products into the program without breaking existing client code |  |

<br>

## Abstract Factory
**Lets you produce families of related objects without specifying their concrete classes.**

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### 💡 Applicability
aaa

### ⚖️ Pros & Cons
| Pros | Cons |
| ---- | ---- |
| aaaa | aaaa |

<br>

## Builder
**Lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.**

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### 💡 Applicability
aaa

### ⚖️ Pros & Cons
| Pros | Cons |
| ---- | ---- |
| aaaa | aaaa |

<br>

## Prototype
**Lets you copy existing objects without making your code dependent on their classes.**

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### 💡 Applicability
aaa

### ⚖️ Pros & Cons
| Pros | Cons |
| ---- | ---- |
| aaaa | aaaa |

<br>

## Singleton
**Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.**

### 🚨 The problem
The Singleton pattern solves two problems at the same time (but violates the Single Responsibility Principle):

- Ensure that a class has just a single instance (common reason for this is to control access to some shared resource—for example, a database or a file)

- Provide a global access point to that instance. Global variables are very handy, but also very unsafe, since any code can potentially overwrite the contents of those variables and crash the app. This pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.

### ✅ The solution
All implementations of the Singleton have these two steps in common:

- Make the default constructor private, to prevent other objects from using the `new` operator with the Singleton class.
- Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

If your code has access to the Singleton class, then it’s able to call the Singleton’s static method. So whenever that method is called, the same object is always returned.

### 🛠️ Structure

![Singleton structure](images/singleton1.png)

The Singleton class declares the static method getInstance that returns the same instance of its own class.

The Singleton’s constructor should be hidden from the client code. Calling the getInstance method should be the only way of getting the Singleton object.

### 💡 Applicability
Use the Singleton pattern pattern when:
- a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program
- you need stricter control over global variables

### ⚖️ Pros & Cons

| Pros | Cons |
| ---- | ---- |
| You can be sure that a class has only a single instance | The pattern solves two problems at the time, violating the Single Responsibility Principle | 
| You gain a global access point to that instance | The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other |
| The singleton object is initialized only when it’s requested for the first time | The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times |
|  | It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don’t write the tests. Or don’t use the Singleton pattern |

<br>
<br>

---

Images sources: https://refactoring.guru/design-patterns/

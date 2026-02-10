
# Structural design patterns
They explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.

## Adapter
Allows objects with incompatible interfaces to collaborate.

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### ⚖️ Drawbacks
aaa

<br>

## Bridge

### 🚨 The problem
Lets you split a large class or a set of closely related classes into two separate hierarchies (abstraction and implementation) which can be developed independently of each other.

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### ⚖️ Drawbacks
aaa

<br>

## Composite
Lets you compose objects into tree structures and then work with these structures as if they were individual objects.

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### ⚖️ Drawbacks
aaa

<br>

## Decorator
Lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### ⚖️ Drawbacks
aaa

<br>

## Facade
Defines a high-level, unified, simplified interface to make a subsystem (library, a framework, or any other complex set of classes) easier to use.

### 🚨 The problem
Imagine that you have to make your code work with a broad set of objects that belong to a sophisticated library or framework. Ordinarily, you’d need to initialize all of those objects, keep track of dependencies, execute methods in the correct order, etc. As a result, the business logic of your classes would become tightly coupled to the implementation details of 3rd-party classes, making it hard to comprehend and maintain.

### ✅ The solution
A facade is a class that provides a simple interface to a complex subsystem which contains lots of moving parts.

It might provide limited functionality in comparison to working with the subsystem directly; however, it includes only those features that clients really care about. It's handy when a sophisticated library has dozens of features, but you just need a tiny bit of them.

### 🛠️ Structure
![facade1](images/facade1.png)

- The Facade provides convenient access to a particular part of the subsystem’s functionality. It knows where to direct the client’s request and how to operate all the moving parts.
- Additional Facade classes can be created to prevent polluting a single facade with unrelated features that might make it yet another complex structure; they can be used by both clients and other facades.
- The Complex Subsystem consists of dozens of various objects. To make them all do something meaningful, you have to dive deep into the subsystem’s implementation details, such as initializing objects in the correct order and supplying them with data in the proper format. Subsystem classes aren’t aware of the facade’s existence. They operate within the system and work with each other directly.
- The Client uses the facade instead of calling the subsystem objects directly.

### ⚖️ Drawbacks
It's useless if the subsystem is already simple, it would add an unnecessary layer. There's also the risk of a facade becoming a "god object", a large object coupled to all classes of an app

<br>

## Flyweight
Lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### ⚖️ Drawbacks
aaa

<br>

## Proxy
Lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

### 🚨 The problem
aaa

### ✅ The solution
aaa

### 🛠️ Structure
aaa

### ⚖️ Drawbacks
aaa

<br>

---

Images sources: https://refactoring.guru/design-patterns/

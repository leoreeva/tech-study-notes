
# Creational design patterns
They provide object creation mechanisms that increase flexibility and reuse of existing code.

<br>

## Factory Method
It provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

### 🚨 The problem
Imagine that you’re creating a logistics management application. The first version of your app can only handle transportation by trucks, but ater a while your app becomes popular, and you receive requests from sea transportation companies to incorporate sea logistics into the app.

At present, most of your code is coupled to the `Truck` class. Adding `Ships` into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

### ✅ The solution
This pattern suggests that you replace direct object construction calls (using the new operator) with calls to a special factory method. The objects are still created via the new operator, but it’s being called from within the factory method. Objects returned by a factory method are often referred to as products.

Creator classes:

![alt text](images/factory_metod1.png)

Product classes:

![alt text](images/factory_metod2.png)

The code that uses the factory method (often called the client code) doesn’t see a difference between the actual products returned by various subclasses. The client treats all the products as abstract Transport. The client knows that all transport objects are supposed to have the deliver method, but exactly how it works isn’t important to the client.

### 🛠️ Structure

![alt text](images/factory_metod3.png)

- The `Product` interface is common to all objects that can be produced by the creator and its subclasses.
- `Concrete Products` are different implementations of the product interface.
- The `Creator` class declares the factory method that returns new product objects. It’s important that the return type of this method matches the product interface. You can declare the factory method as abstract to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type. Note, despite its name, product creation is not the primary responsibility of the creator. Usually, the creator class already has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes. Here is an analogy: a large software development company can have a training department for programmers. However, the primary function of the company as a whole is still writing code, not producing programmers
- `Concrete Creators` override the base factory method so it returns a different type of product. Note that the factory method doesn’t have to create new instances all the time. It can also return existing objects from a cache, an object pool, or another source.


<br>

## Abstract Factory
aaa

<br>

## Builder
aaa

<br>

## Prototype
aaa

<br>

## Singleton
aaa

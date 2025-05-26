# SOLID principle

https://andreacavallo.medium.com/s-o-l-i-d-i-5-principi-dalla-oop-alla-programmazione-funzionale-617ba2b6a691

https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898

In software programming, SOLID is an acronym for 5 design principles intended to make object-oriented designs more understandable, flexible, and maintainable.

## S = Single Responsability (SRP)
A class should have one, and only one, reason to change.
An object should have only one responsibility (a reason to change). It is supposed to simplify modifications. The cohesion is stronger, dependency coupling is looser and the code is less complex.

**Wrong**:
```java
public class Employee {
    private String name;
    private double salary;
    // getter and setter methods

    public void calculateSalary() {
        // calculates the employee's salary
    }

    public void saveToDatabase() {
        // saves the employee's data to the database
    }

    public void generatePaySlip() {
        // generates the employee's payslip
    }

    public void sendEmailNotification() {
        // sends an email notification to the employee
    }
}
```

**Correct**:
```java
...
```

## O = Open Closed (OCP)
Entities should be open for extension, but closed for modification.
Entity can be extended by adding what is needed, but it can never be modified. This significantly reduces the risk of breaking existing functionality and provides a looser coupling.

## L = Liskov Substitution (LSP)
Subtypes must be substitutable for their base types.
The principle says that it is possible to use base type and get a correct result as the outcome. It can be said that the LSP confirms abstractions are correct.

## I = Interface Segregation (ISP)
Classes that implement interfaces, should not be forced to implement methods they do not use.
Big interfaces should be split into smaller ones so there are no methods that are not used implemented. Classes know only about methods related to them providing decoupling and easier modifications.

## D = Dipendency Inversion (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
This reduces dependencies in the code modules. Code is much more easier to maintain if abstractions and details are isolated from each other.

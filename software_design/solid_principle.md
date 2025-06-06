# SOLID principle

In software programming, SOLID is an acronym for 5 design principles intended to make object-oriented designs more understandable, flexible, and maintainable.

<br>

## S = Single Responsability (SRP)
Classes and objects should have one, and only one, responsibility (reason to change). 

This separation of responsibilities makes code more modular, more maintainable, less complex, and promotes the reduction of bugs due to changes in one responsibility that may affect another.

**Before**:
```java
public class Employee {
    private String name;
    private double salary;
    // getter and setter methods

    public void saveToDatabase() {
        // saves the employee's data to the database
    }

    public void generatePaySlip() {
        // generates the employee's payslip
    }

    public void calculateSalary() {
        // calculates the employee's salary
    }
}
```

**After**:
```java
public class Employee {
    private String name;
    private double salary;
    // getter and setter methods
}

public class DatabaseManager {
    public void saveEmployee(Employee employee) {
        // save employee to db
    }
}

public class PaySlipGenerator {
    public void generatePaySlip(Employee employee) {
        // generate pay slip of employee
    }
}

public class SalaryCalculator {
    public double calculateSalary(Employee employee) {
        // calculate salary of employee
        // ...
        return salary;
    }
}
```

<br>

## O = Open Closed (OCP)
Entities should be open for extension (can be extended by adding what is needed), but closed for modification (should never be modified). 

On a practical standpoint, classes are “open” to extensions via interface implementation or inheritance, but “closed” to modifications, since the existing behavior remains unchanged. This significantly reduces the risk of breaking existing functionality and provides a looser coupling.

```java
interface Vehicle {
    double calculateTaxCost();
}

class Car implements Vehicle {
    private double engineCapacity;

    public Car(double engineCapacity) {
        this.engineCapacity = engineCapacity;
    }

    public double getEngineCapacity() {
        return engineCapacity;
    }

    public double calculateTaxCost() {
        return engineCapacity * 2.5;
    }
}

class Motorcycle implements Vehicle {
    private double engineCapacity;

    public Motorcycle(double engineCapacity) {
        this.engineCapacity = engineCapacity;
    }

    public double getEngineCapacity() {
        return engineCapacity;
    }

    public double calculateTaxCost() {
        return engineCapacity * 1.5;
    }
}

class TaxCalculator {
    public double calculateTotalTax(List<Vehicle> vehicles) {
        double totalTax = 0;
        for (Vehicle vehicle : vehicles) {
            totalTax += vehicle.calculateTaxCost();
        }
        return totalTax;
    }
}

public class Main {
    public static void main(String[] args) {
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Car(2000));
        vehicles.add(new Motorcycle(500));

        TaxCalculator taxCalculator = new TaxCalculator();
        double totalTax = taxCalculator.calculateTotalTax(vehicles);

        System.out.println("Total tax: " + totalTax);
    }
}
```
In this example, if we wanted to add new vehicle types (e.g. truck), we would not have to modify the `TaxCalculator` class. We would simply have to create a new class that implements the Vehicle interface and provide an implementation of the `calculateTaxCost()` method. The `TaxCalculator` class would remain unchanged and would be able to calculate taxes for new vehicle types without any modifications.

<br>

## L = Liskov Substitution (LSP)
Subtypes must be substitutable for their base types.
The principle says that it is possible to use base type and get a correct result as the outcome. It can be said that the LSP confirms abstractions are correct.

// TODO: CONTINUE FROM HERE

https://andreacavallo.medium.com/s-o-l-i-d-i-5-principi-dalla-oop-alla-programmazione-funzionale-617ba2b6a691

https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898

<br>

## I = Interface Segregation (ISP)
Classes that implement interfaces, should not be forced to implement methods they do not use.
Big interfaces should be split into smaller ones so there are no methods that are not used implemented. Classes know only about methods related to them providing decoupling and easier modifications.

<br>

## D = Dipendency Inversion (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
This reduces dependencies in the code modules. Code is much more easier to maintain if abstractions and details are isolated from each other.
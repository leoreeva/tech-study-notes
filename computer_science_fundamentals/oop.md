# OOP (object-oriented programming)

[work in progress]

https://www.interviewbit.com/oops-interview-questions/

some concepts: Encapsulation, Inheritance, Polymorphism, Abstraction, Composition, etc.


### 1. Classes and Objects

**Class**: A blueprint for creating objects
**Object**: An instance of a class

```python
class Dog:
    def __init__(self, name: str):
        self.name = name

    def bark(self) -> str:
        return f"{self.name} says woof!"

# Object creation
my_dog = Dog("Buddy")
print(my_dog.bark())  # "Buddy says woof!"
```

### 2. Encapsulation

Bundling data and methods that operate on that data within a single unit (class). Hide internal details.

```python
class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance  # Protected attribute (convention)

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount

    def get_balance(self) -> float:
        return self._balance

    # External code can't directly modify _balance improperly
```

### 3. Inheritance

Create new classes based on existing ones, inheriting attributes and methods.

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} meows"
```

### 4. Polymorphism

Objects of different classes can be treated as objects of a common parent class. Same interface, different implementations.

```python
def make_animal_speak(animal: Animal) -> None:
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

make_animal_speak(dog)  # Works with Dog
make_animal_speak(cat)  # Works with Cat
# Both have speak() method but behave differently
```

### 5. Abstraction

Hide complex implementation details, expose only necessary features.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process payment - subclasses define how"""
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Complex credit card logic hidden here
        print(f"Processing ${amount} via credit card")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Complex PayPal API logic hidden here
        print(f"Processing ${amount} via PayPal")
        return True

# Client code doesn't care about implementation details
processor: PaymentProcessor = CreditCardProcessor()
processor.process_payment(100.00)
```

### 6. Composition

"Has-a" relationship. Build complex objects from simpler ones.

```python
class Engine:
    def start(self) -> str:
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self) -> str:
        return self.engine.start()

# Prefer composition over inheritance when possible
```
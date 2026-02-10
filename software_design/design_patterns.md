# Design Patterns

> "Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice."

In software terms, a design pattern is a language-independent reusable solution/template to commonly occurring problems. It's not a library/framework, not algorithms, not a copy-paste solution and finally not mandatory (knowing when NOT to use them is equally important)

## [Creational Patterns](./01_creational_patterns.md)
**Focus:** How objects are created

Creational patterns provide flexibility in *what* gets created, *who* creates it, *how* it's created, and *when*. They abstract the instantiation process, making systems independent of how objects are created, composed, and represented.

| Pattern  | One-Line Summary | Difficulty | Progress |
|----------|------------------|------------|----------|
| **[Singleton](./_creational_patterns.md#singleton)** | Ensure a class has only one instance | ⭐ | ✅ |
| **[Prototype](./_creational_patterns.md#prototype)** | Clone objects instead of creating new | ⭐ | ✅ |
| **[Factory Method](./_creational_patterns.md#factory-method)** | Define an interface for creating objects | ⭐⭐ | ✅ |
| **[Builder](./_creational_patterns.md#builder)** | Construct complex objects step by step | ⭐⭐ | ❌ |
| **[Abstract Factory](./_creational_patterns.md#abstract-factory)** | Create families of related objects | ⭐⭐⭐ | ❌ |


## [Structural Patterns](./02_structural_patterns.md)
**Focus:** How objects are composed and related

As systems grow, managing relationships between objects becomes challenging. Structural patterns help organize classes and objects into larger structures while keeping them flexible and efficient.

| Pattern  | One-Line Summary | Difficulty | Progress |
|----------|------------------|------------|----------|
| **[Adapter](./structural_patterns.md#adapter)** | Convert interface to another interface | ⭐ | ❌ |
| **[Facade](./structural_patterns.md#facade)** | Provide simplified interface to subsystem | ⭐ | ✅ |
| **[Composite](./structural_patterns.md#composite)** | Treat objects and compositions uniformly | ⭐⭐ | ❌ |
| **[Decorator](./structural_patterns.md#decorator)** | Add behavior to objects dynamically | ⭐⭐ | ❌ |
| **[Proxy](./structural_patterns.md#proxy)** | Control access to an object | ⭐⭐ | ❌ |
| **[Bridge](./structural_patterns.md#bridge)** | Decouple abstraction from implementation | ⭐⭐⭐ | ❌ |
| **[Flyweight](./structural_patterns.md#flyweight)** | Share common state to save memory | ⭐⭐⭐ | ❌ |


## [Behavioral Patterns](./03_behavioral_patterns.md)
**Focus:** How objects communicate and distribute responsibility

Objects need to collaborate to accomplish tasks. Behavioral patterns define clear communication protocols, making interactions flexible and maintainable.

| Pattern  | One-Line Summary | Difficulty | Progress |
|----------|------------------|------------|----------|
| **[Iterator](./behavioral_patterns.md#iterator)** | Access collection elements sequentially | ⭐ | ❌ |
| **[Template Method](./behavioral_patterns.md#template-method)** | Define skeleton of algorithm in base class | ⭐ | ❌ |
| **[Chain of Responsibility](./behavioral_patterns.md#chain-of-responsibility)** | Pass requests along a chain of handlers | ⭐⭐ | ❌ |
| **[Command](./behavioral_patterns.md#command)** | Encapsulate requests as objects | ⭐⭐ | ❌ |
| **[Memento](./behavioral_patterns.md#memento)** | Save and restore object state | ⭐⭐ | ❌ |
| **[Observer](./behavioral_patterns.md#observer)** | Define one-to-many dependency | ⭐⭐ | 🚧 |
| **[Strategy](./behavioral_patterns.md#strategy)** | Define family of interchangeable algorithms | ⭐⭐ | ❌ |
| **[Mediator](./behavioral_patterns.md#mediator)** | Reduce coupling between objects | ⭐⭐⭐ | ❌ |
| **[State](./behavioral_patterns.md#state)** | Change behavior when state changes | ⭐⭐⭐ | ❌ |
| **[Visitor](./behavioral_patterns.md#visitor)** | Add operations without modifying classes | ⭐⭐⭐ | ❌ |
| **[Interpreter](./behavioral_patterns.md#interpreter)** | Define grammar and interpreter for language | ⭐⭐⭐ | ❌ |

## Reasons
Why Use Design Patterns?
- **Proven Solutions**. Patterns have been tested by many developers over time. You're not reinventing the wheel.
- **Common Vocabulary**. "Let's use the Observer pattern" communicates more than explaining pub-sub from scratch.
- **Better Design**. Patterns encourage loose coupling, high cohesion, and maintainable code.
- **Avoid Pitfalls**. Patterns document not just solutions but also consequences and trade-offs.
- **Learn from Experts**. Patterns capture expertise from experienced developers.

When NOT to Use Patterns? Warning Signs of Pattern Abuse:
- Using patterns in simple problems that don't need them
- Forcing a pattern because you recently learned it
- Over-engineering for future requirements that may never come
- Making code more complex to fit a pattern
- Using multiple patterns when one simple solution would work

The goal is clean, maintainable code—not using as many patterns as possible.

## ⚠️ Important Notes
- **Patterns are not rules**: They're guidelines. Break them when it makes sense.
- **Context matters**: A pattern perfect for one problem might be terrible for another.
- **Keep it simple**: No pattern is better than the wrong pattern.
- **Python is not Java**: Some patterns (like Singleton) have better alternatives in Python.
- **Patterns evolve**: Modern languages have features that reduce pattern complexity.
- For **interview prep**, focus on: Singleton, Factory Method, Strategy, Observer, Decorator, and Adapter (most commonly discussed).

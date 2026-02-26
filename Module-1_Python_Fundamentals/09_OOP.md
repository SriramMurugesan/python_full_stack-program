# Topic 9: Professional Object-Oriented Programming (OOP)

OOP in Python is both flexible and powerful. To reach the expert level, you must understand not just the "four pillars" but also how Python manages classes internally.

## 1. The Core Anatomy: `self` and `__init__`
- **`self`**: A reference to the current instance of the class. It is **not** a keyword; you could name it anything, but `self` is the naming convention (PEP 8).
- **`__init__`**: The constructor. It initializes the object's state.

---

## 2. Advanced Class Features

### Class vs. Static Methods
- **`@classmethod`**: Receives the class (`cls`) as the first argument. Used for factory methods.
- **`@staticmethod`**: Doesn't receive any implicit first argument. Just a namespace-contained function.
- **`@property`**: Allows a method to be accessed like an attribute (Encapsulation/Getters).

### Dunder (Magic) Methods
Methods surrounded by double underscores that allow objects to interact with Python's built-in syntax:
- `__str__`: Controls what `print(obj)` shows.
- `__repr__`: Controls the "developer" representation of the object.
- `__len__`, `__add__`, `__eq__`: Operator overloading.

---

## 3. The 4 Pillars (Expert Perspective)

### A. Encapsulation (Access Modifiers)
Python uses naming conventions for access control (no strict `private/public` keywords):
- **Public:** `self.name`
- **Protected:** `_self.name` (Internal use hint).
- **Private:** `__self.name` (Triggers **Name Mangling** to prevent accidental overrides).

### B. Inheritance & The MRO
Python supports **Multiple Inheritance**.
- **MRO (Method Resolution Order):** The order in which Python searches for a method in a class hierarchy. Use `ClassName.mro()` to see it.
- **`super()`**: Dynamically refers to the parent class based on the MRO.

### C. Polymorphism
Achieved via **Method Overriding** and **Duck Typing** ("If it walks like a duck and quacks like a duck, it's a duck").

### D. Abstraction (ABC)
Using the `abc` module to define interfaces. Abstract methods MUST be implemented by any non-abstract child.

---

## 4. Design Principles (SOLID)
Experts follow these patterns:
1. **Single Responsibility:** A class should do one thing.
2. **Open/Closed:** Classes should be open for extension but closed for modification.
3. **Liskov Substitution:** Subtypes must be substitutable for their base types.
4. **Interface Segregation:** Better many small interfaces than one large one.
5. **Dependency Inversion:** Depend on abstractions, not concretions.

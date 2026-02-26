# Module 1: Top Python Expert Interview Questions

These questions are designed to test not just your knowledge of syntax, but your understanding of how Python works under the hood.

## 🟢 Level 1: Junior / Fresher
1. **Explain the difference between `is` and `==`.**
   - *Answer:* `==` checks for **equality** (do they have the same value?), while `is` checks for **identity** (do they point to the exact same object in memory?).
2. **What is a "Generator" and why use it over a list?**
   - *Answer:* Generators use "lazy evaluation" (yielding one item at a time). They are memory efficient because they don't store the entire sequence in memory at once.
3. **What are "Mutable" vs "Immutable" types in Python?**
   - *Answer:* Mutable types (List, Set, Dict) can be changed after creation. Immutable types (Int, Float, String, Tuple) cannot.
4. **How does Python handle memory management?**
   - *Answer:* Python uses a private heap for objects and a **Garbage Collector** that uses reference counting and cycle detection to free memory.

## 🟡 Level 2: Mid-Level / Professional
5. **Describe the LEGB rule.**
   - *Answer:* It stands for Local, Enclosing, Global, and Built-in. It defines the order in which Python looks up variable names.
6. **What is the difference between `@classmethod` and `@staticmethod`?**
   - *Answer:* A `@classmethod` takes `cls` as its first argument and can access class-level state. A `@staticmethod` behaves like a normal function but belongs to the class's namespace.
7. **What is "Duck Typing" in Python?**
   - *Answer:* It's a programming concept where the type of an object is determined by its behavior (methods/properties) rather than its explicit class. "If it walks like a duck and quacks like a duck, it's a duck."
8. **How does the `with` statement work under the hood?**
   - *Answer:* It invokes the Context Manager protocol, specifically calling the `__enter__` method at the start and the `__exit__` method at the end (even if an error occurs).

## 🔴 Level 3: Senior / Architect
9. **Explain the Python MRO (Method Resolution Order).**
   - *Answer:* It is the order Python uses to search for a method in multiple inheritance. It uses the **C3 Linearization** algorithm. You can check it using `ClassName.mro()`.
10. **What is Name Mangling and why is it used?**
    - *Answer:* When you prefix a variable with `__` (e.g., `__salary`), Python renames it internally to `_ClassName__salary` to prevent it from being accidentally overridden in subclasses.
11. **Explain the difference between `__str__` and `__repr__`.**
    - *Answer:* `__str__` is for users (readable string); `__repr__` is for developers (unambiguous representation, ideally enough to recreate the object).
12. **What are "Closures" in Python?**
    - *Answer:* A closure is a function object that remembers values in its enclosing scope even if they are no longer in memory. It happens when a nested function references a variable from the outer function.

## 🏆 Bonus: Expert Scenario
**Question:** If you have a large list of 10 million integers and you need to check for the existence of numbers frequently, which data structure would you use and why?
**Answer:** I would convert the list to a **Set**. While a list has $O(n)$ search time, a set uses a hash table providing $O(1)$ average-case search time, which is significantly faster for large datasets.

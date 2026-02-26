# 09_OOP_examples.py
from abc import ABC, abstractmethod

"""
Step-by-step guide to Professional OOP in Python.
Demonstrates MRO, Decorators (@property), and Dunder Methods.
"""

# --- 1. Advanced Class Features (Decorators) ---
class Employee:
    company = "Antigravity AI"  # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private variable

    # Getter using @property
    @property
    def salary(self):
        return f"${self.__salary:,}"

    # Factory method using @classmethod
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

# --- 2. Multiple Inheritance & MRO ---
class A:
    def greet(self): print("Hello from A")

class B(A):
    def greet(self): print("Hello from B")

class C(A):
    def greet(self): print("Hello from C")

class D(B, C):
    pass

# --- 3. Dunder Methods (Magic Methods) ---
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by Master Author"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

# --- Execution & Demonstration ---
if __name__ == "__main__":
    print("--- Decorators (@property & @classmethod) ---")
    emp = Employee.from_string("Sriram-150000")
    print(f"Employee: {emp.name} | Salary: {emp.salary}")

    print("\n--- MRO (Multiple Inheritance) ---")
    d_obj = D()
    d_obj.greet()  # Calls B's greet due to MRO
    print(f"MRO for D: {[cls.__name__ for cls in D.mro()]}")

    print("\n--- Dunder Methods ---")
    b1 = Book("Python Expert", 500)
    b2 = Book("Clean Code", 300)
    print(f"Book String: {b1}")
    print(f"Total Pages (b1 + b2): {b1 + b2}")

    print("\n--- Abstraction ---")
    class Validator(ABC):
        @abstractmethod
        def validate(self, data): pass

    class EmailValidator(Validator):
        def validate(self, data):
            return "@" in data

    v = EmailValidator()
    print(f"Is valid email? {v.validate('test@example.com')}")

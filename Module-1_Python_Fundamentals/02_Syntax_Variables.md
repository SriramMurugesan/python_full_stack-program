# Topic 2: Python Syntax, Variables, and Data Types

## 1. Professional Python Syntax
Python's syntax is designed for readability. However, being an "expert" requires understanding the underlying rules:

### Indentation (The Suite)
- Unlike C++ or Java that use `{ }`, Python uses **indentation** to define blocks of code (called "suites").
- Standard practice is **4 spaces** per indentation level. Mixtures of tabs and spaces should be avoided (PEP 8 requirement).

### Comments
- **Single-line:** Use `#`.
- **Multi-line / Docstrings:** Use triple quotes (`"""` or `'''`). Docstrings are used to document modules, classes, and functions.

---

## 2. Variables & Memory Management
Variables in Python are not "containers" for values but **references** to objects in memory.

```python
x = 5
y = x  # y now references the same object as x
```

### Dynamic Typing
Python is **dynamically typed**, meaning the type of a variable is determined at runtime based on the value it holds. You can reassign a variable to a different type anytime:
```python
data = 10    # data is int
data = "Hi"  # data is now str
```

### Naming Conventions (PEP 8)
- **Snake_case:** For variables and functions (`my_variable`).
- **PascalCase:** For classes (`MyClass`).
- **UPPER_CASE:** For constants (`PI = 3.14`).

---

## 3. Comprehensive Data Types

| Type | Description | Example |
| :--- | :--- | :--- |
| **int** | Arbitrary precision integers (no limit on size). | `10`, `-99` |
| **float** | 64-bit floating point numbers. | `10.5`, `3e2` |
| **complex** | Numbers with real and imaginary parts. | `2 + 3j` |
| **bool** | Logic values. | `True`, `False` |
| **str** | Immutable sequence of characters. | `"Hello"` |
| **NoneType**| Represents the absence of a value. | `None` |

---

## 4. Advanced Operations

### Type Conversion (Casting)
- **Implicit:** Python automatically converts types (e.g., `int + float = float`).
- **Explicit:** Using functions like `int()`, `float()`, `str()`, `bool()`.

### The `id()` and `type()` functions
- `type(obj)`: Returns the class of the object.
- `id(obj)`: Returns the unique memory address of the object.

```python
num = 10
print(type(num)) # <class 'int'>
print(id(num))   # Unique memory ID
```
---

## 5. Input and Output
- `print(value, ..., sep=' ', end='\n')`: Highly customizable output.
- `input("prompt")`: Always returns data as a **string**. You must cast it if you need numbers.

# Topic 4: Functions and Modules

## 1. Professional Function Anatomy
A function is a reusable block of code. To become an expert, you must understand how Python handles arguments and scope.

### Function Definition
```python
def function_name(parameter1, parameter2="Default"):
    """Docstring: Explains what the function does."""
    # Logic here
    return result
```

### Advanced Arguments
- **Positional vs. Keyword Arguments:** You can call functions using specific parameter names.
- **`*args` (Arbitrary Positional Arguments):** Allows a function to accept any number of positional arguments (passed as a tuple).
- **`**kwargs` (Arbitrary Keyword Arguments):** Allows a function to accept any number of keyword arguments (passed as a dictionary).

---

## 2. Variable Scope (The LEGB Rule)
Python follows a strict hierarchy to look up variables:
1. **L (Local):** Defined inside the current function.
2. **E (Enclosing):** Defined in nested functions (closures).
3. **G (Global):** Defined at the top level of the script.
4. **B (Built-in):** Predefined Python names (e.g., `print`, `len`).

> [!IMPORTANT]
> To modify a global variable inside a function, you must use the `global` keyword. For enclosing variables, use `nonlocal`.

---

## 3. Lambda Functions & Recursion
- **Lambda:** Anonymous, one-line functions.
  `square = lambda x: x * x`
- **Recursion:** A function calling itself. Essential for tree traversals and complex algorithms.

---

## 4. Modules and Packages
A module is simply a `.py` file. A package is a directory containing modules and an `__init__.py` file.

### Importing Strategies
- `import math`: Simple import.
- `from math import sqrt, pi`: Specific import (avoids `math.` prefix).
- `import numpy as np`: Importing with an alias.

### The `__name__ == "__main__"` Pattern
This ensures that certain code only runs when the script is executed directly, not when it is imported as a module.
```python
if __name__ == "__main__":
    main_logic()
```

### `sys.path` and search order
When you `import x`, Python searches in:
1. The current directory.
2. `PYTHONPATH` environment variable.
3. Standard library directories.
4. Third-party `site-packages`.

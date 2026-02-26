# Topic 7: Professional Exception Handling

Exceptions are not just "errors"; they are signals used to handle unexpected events gracefully. A master developer writes code that doesn't just crash but reacts.

## 1. The Full Exception Block
To handle exceptions like a pro, you need the complete `try-except-else-finally` structure:

```python
try:
    # 1. Critical code that might fail
    file = open("data.txt", "r")
except FileNotFoundError as e:
    # 2. Handles a specific error
    print(f"Error: {e}")
else:
    # 3. Runs ONLY if the 'try' block succeeded
    print("File read successfully.")
finally:
    # 4. ALWAYS runs (Used for cleanup like closing files/DBs)
    print("Execution finished.")
```

---

## 2. Exception Hierarchy
Python exceptions are classes. It is best practice to catch **specific** exceptions rather than a generic `Exception`.

- **`BaseException`**: The root of all exceptions.
  - **`Exception`**: The base for almost all user exceptions.
    - `ArithmeticError` (`ZeroDivisionError`)
    - `LookupError` (`IndexError`, `KeyError`)
    - `ValueError`
    - `TypeError`

---

## 3. Raising Exceptions & Custom Errors
You can manually trigger an error using the `raise` keyword.

### Custom Exceptions
You can create your own error types by inheriting from the `Exception` class:
```python
class InsufficientFundsError(Exception):
    """Raised when account balance is too low."""
    pass

def withdraw(amount):
    if amount > 100:
        raise InsufficientFundsError("You only have 100 coins!")
```

---

## 4. Expert Best Practices
- **Catch specific errors:** Never do `except: pass`. It hides bugs.
- **Keep `try` blocks small:** Only wrap the lines that are actually likely to fail.
- **Use `finally` for cleanup:** Ensure resources (files, network connections) are released.
- **Don't use exceptions for flow control:** Exceptions are expensive; use `if/else` for logic whenever possible.

# Topic 3: Operators and Control Statements

## 1. Professional Operators
Python offers a rich set of operators for various manipulations:

### Arithmetic & Assignment
- **Floor Division (`//`):** Divides and rounds down to the nearest integer.
- **Power (`**`):** Exponentiation (e.g., `2**3 = 8`).
- **Modulus (`%`):** Returns the remainder.
- **Compound Assignment:** `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.

### Comparison & Logical
- **Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`.
- **Logical:** `and`, `or`, `not`. Python uses **Short-circuiting** (e.g., in `A or B`, if A is True, B is not evaluated).

### Bitwise Operators (The Expert Level)
Used for manipulating data at the bit level:
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (Left Shift), `>>` (Right Shift).

### Identity & Membership
- **`is` / `is not`:** Check if two variables point to the same object in memory.
- **`in` / `not in`:** Check if a value exists within a sequence (string, list, tuple).

---

## 2. Decision Making (Control Flow)

### The Ternary Operator
A one-liner for `if-else`:
```python
status = "Adult" if age >= 18 else "Minor"
```

### Truthiness in Python
In Python, almost everything has a "Truth value":
- **Falsy values:** `None`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `False`.
- **Truthy values:** Everything else.

---

## 3. Iteration (Loops)

### The `range()` function
Generates a sequence of numbers: `range(start, stop, step)`.
- `range(5)` -> 0, 1, 2, 3, 4
- `range(2, 10, 2)` -> 2, 4, 6, 8

### Loop Else: A Unique Python Feature
Both `for` and `while` loops can have an `else` block. It executes **only if the loop completes normally** (i.e., it was NOT stopped by a `break` statement).

```python
for item in items:
    if item == "found":
        break
else:
    print("Item never found.")
```

### Loop Control Statements
- **`break`:** Exits the loop immediately.
- **`continue`:** Skips the rest of the current iteration and moves to the next.
- **`pass`:** A null statement (placeholder) that does nothing.

### Enumerate & Zip
- `enumerate(listing)`: Returns both the index and the value.
- `zip(list1, list2)`: Iterates over two lists simultaneously.

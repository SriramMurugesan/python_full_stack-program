# Topic 5: Advanced Data Structures

Python’s built-in data structures are optimized for efficiency. Choosing the right one is the hallmark of an expert.

## 1. List (Mutable & Ordered)
Lists are dynamic arrays. They are best for collections where order matters and you need to modify elements.

- **Methods:** `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`.
- **Expert Note:** Appending to a list is $O(1)$, but inserting at the beginning is $O(n)$ because all other elements must shift.

### List Comprehensions
The Pythonic way to create lists:
```python
squares = [x**2 for x in range(10) if x % 2 == 0]
```

---

## 2. Tuple (Immutable & Ordered)
Tuples are "locked" lists. They are faster and safer (prevents accidental modification).

- **Use case:** Returning multiple values from a function, or using as keys in a dictionary.
- **Unpacking:** `x, y = (10, 20)`

---

## 3. Set (Mutable & Unordered)
Sets store unique elements. They are based on **hash tables**.

- **Methods:** `add()`, `discard()`, `union()`, `intersection()`, `difference()`.
- **Expert Note:** Membership testing (`x in my_set`) is $O(1)$, making it extremely fast compared to lists $O(n)$.

---

## 4. Dictionary (Mutable & Mapped)
Dictionaries store key-value pairs. As of Python 3.7+, they maintain insertion order.

- **Methods:** `keys()`, `values()`, `items()`, `get()` (safer than `[]`), `update()`.
- **Expert Note:** Like sets, dictionaries are hash-table based. Lookups are $O(1)$ on average.

---

## 5. Performance Comparison

| Operation | List | Tuple | Set | Dictionary |
| :--- | :--- | :--- | :--- | :--- |
| **Search (x in s)** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ (Keys) |
| **Insertion** | $O(1)^*$ | N/A | $O(1)$ | $O(1)$ |
| **Deletion** | $O(n)$ | N/A | $O(1)$ | $O(1)$ |
| **Ordering** | Yes | Yes | No | Yes (3.7+) |

---

## 6. Advanced Concepts
- **Slicing:** `my_list[start:stop:step]`
- **Nested Structures:** Lists of dictionaries, dictionaries of sets, etc.
- **Deep vs Shallow Copy:** Using the `copy` module for nested structures.

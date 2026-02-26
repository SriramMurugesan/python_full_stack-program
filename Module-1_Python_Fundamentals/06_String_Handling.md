# Topic 6: Professional String Handling

In Python, strings are **immutable sequence of Unicode characters**. They are not just text; they are powerful objects with extensive built-in capabilities.

## 1. Immutability (Key Concept)
Once a string is created, it **cannot be changed**. Any "modification" (like `upper()`) actually creates a **new string object** in memory.

```python
s = "hello"
s[0] = "H" # Error! Strings are immutable.
```

---

## 2. Advanced Indexing & Slicing
Syntax: `string[start:stop:step]`

- **Negative Indexing:** `s[-1]` is the last char, `s[-2]` is second-to-last.
- **Reverse string:** `s[::-1]`
- **Step slicing:** `s[::2]` (every 2nd character).

---

## 3. The Evolution of String Formatting
Experts use the most efficient formatting method depending on the situation:

1. **Old Style (%):** `"%s is %d years old" % (name, age)` (Legacy).
2. **`.format()` Method:** `"{} is {}".format(name, age)` (More flexible).
3. **f-Strings (Python 3.6+):** `f"{name} is {age}"` (Recommended: Fastest and cleanest).

---

## 4. Comprehensive String Methods

| Method | Description |
| :--- | :--- |
| **`strip()`** | Removes whitespace (also `lstrip`, `rstrip`). |
| **`split(sep)`** | Breaks string into a list based on separator. |
| **`join(list)`** | Concatenates a list of strings using the string as a separator. |
| **`find()` / `index()`**| Locates a substring. `find` returns -1 if not found; `index` raises an error. |
| **`startswith()` / `endswith()`** | Checks prefix/suffix. |
| **`isalpha()` / `isdigit()`** | Validates content type. |

---

## 5. Multi-line Strings & Escape Characters
- **Triple Quotes:** `"""..."""` or `'''...'''` preserve line breaks and formatting.
- **Escape Sequences:** `\n` (newline), `\t` (tab), `\\` (backslash), `\'` (single quote).
- **Raw Strings:** `r"C:\Users\Name"` (Ignores escape characters, useful for file paths and regex).

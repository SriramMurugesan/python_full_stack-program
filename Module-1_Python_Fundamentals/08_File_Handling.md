# Topic 8: Professional File Handling

Handling files effectively involves more than just reading and writing; it requires safety, resource management, and understanding different data formats.

## 1. The Context Manager (The `with` Statement)
Experts **never** use `file.close()` manually. Instead, they use the `with` statement, which ensures that the file is closed correctly even if an exception occurs.

```python
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here
```

---

## 2. Comprehensive File Modes

| Mode | Description |
| :--- | :--- |
| **`r`** | **Read (Default):** Error if file doesn't exist. |
| **`w`** | **Write:** Overwrites existing file or creates new one. |
| **`a`** | **Append:** Adds data to the end without overwriting. |
| **`x`** | **Exclusive Creation:** Fails if the file already exists. |
| **`b`** | **Binary Mode:** For non-text files (images, PDFs). |
| **`+`** | **Update:** Open for both reading and writing (e.g., `r+`). |

---

## 3. Reading/Writing Techniques

### Reading Data
1. `f.read()`: Reads the **entire** file into memory (Caution: heavy for large files).
2. `f.readline()`: Reads a **single** line.
3. `f.readlines()`: Reads all lines into a **list**.
4. **Iterating:** (Best practice)
   ```python
   for line in f:
       print(line.strip())
   ```

### Writing Data
- `f.write(string)`: Writes a single string.
- `f.writelines(list)`: Writes a list of strings.

---

## 4. Path Management with `pathlib`
Modern Python avoids raw strings for paths. Use the `pathlib` module for cross-platform compatibility.

```python
from pathlib import Path

path = Path("my_folder") / "data.txt"
if path.exists():
    print(f"Reading from {path.absolute()}")
```

---

## 5. Handling JSON & Binary Data
### JSON (Standard for Web/Config)
```python
import json
data = {"name": "Sriram", "role": "Expert"}

# Save to file
with open("user.json", "w") as f:
    json.dump(data, f)
```

---

## 6. Expert Best Practices
- **Use relative paths** whenever possible for portability.
- **Check for file existence** before opening in `r` mode.
- **Encoding:** Always specify `encoding="utf-8"` when working with text to avoid cross-platform crashes.

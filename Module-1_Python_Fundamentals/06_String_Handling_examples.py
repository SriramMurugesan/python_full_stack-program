# 06_String_Handling_examples.py

"""
Step-by-step guide to Python String Handling.
Demonstrates advanced slicing, join/split patterns, and f-strings.
"""

# 1. Advanced Slicing [start:stop:step]
text = "Antigravity Programming"
print(f"Original: {text}")
print(f"Every 2nd char: {text[::2]}")     # AtgrvtyPormig
print(f"Reverse: {text[::-1]}")           # gnimmargorP ytivargitnA
print(f"First word: {text[:11]}")         # Antigravity

# 2. Join and Split (The Professional Way)
csv_data = "apple,banana,cherry,date"
fruits_list = csv_data.split(",")        # ['apple', 'banana', 'cherry', 'date']
print(f"\nSplit List: {fruits_list}")

# Using join() to reconstruct a string
hyphenated = "-".join(fruits_list)       # "apple-banana-cherry-date"
print(f"Joined with hyphens: {hyphenated}")

# 3. String Formatting Evolution
name = "Sriram"
level = "Expert"

# f-Strings (Recommended)
msg = f"Developer: {name.upper()} | Level: {level}"
print(f"\nFormatted: {msg}")

# 4. Search and Validation
content = "Python is beautiful"
print(f"\nStarts with 'Python'? {content.startswith('Python')}")
print(f"Index of 'beautiful': {content.find('beautiful')}")

# 5. Handling Multi-line and Whitespace
raw_path = r"C:\new_folder\test.py"  # Raw string ignores \n
print(f"\nRaw Path: {raw_path}")

multiline = """
    This is a multi-line string.
    It preserves indentation.
"""
print(f"Cleaned Multi-line:\n{multiline.strip()}")

# 05_Data_Structures_examples.py

"""
Step-by-step guide to Python Data Structures.
Demonstrates list comprehensions, slicing, set operations, and dictionary handling.
"""

# 1. Lists: Slicing and Comprehensions
print("--- Lists (Slicing & Comprehensions) ---")
numbers = list(range(1, 11))
print(f"Original: {numbers}")
print(f"Slicing (First 3): {numbers[:3]}")
print(f"Slicing (Last 3): {numbers[-3:]}")
print(f"Reversed: {numbers[::-1]}")

# List Comprehension: [expression for item in iterable if condition]
evens_squared = [x**2 for x in numbers if x % 2 == 0]
print(f"Even Squares: {evens_squared}")

# 2. Tuples: Unpacking
print("\n--- Tuples (Unpacking) ---")
point = (10, 20, 30)
x, y, z = point  # Tuple Unpacking
print(f"X: {x}, Y: {y}, Z: {z}")

# 3. Sets: Mathematical Operations
print("\n--- Sets (Set Theory) ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Union: {set_a | set_b}")         # Elements in either A or B
print(f"Intersection: {set_a & set_b}")  # Elements in both A and B
print(f"Difference (A-B): {set_a - set_b}") # In A but not in B

# 4. Dictionaries: Advanced Handling
print("\n--- Dictionaries (Mapping) ---")
config = {"host": "localhost", "port": 8080}

# Safe lookup using .get()
port = config.get("port", 443)  # Returns 443 if 'port' key doesn't exist
print(f"Port: {port}")

# Dictionary Comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
new_dict = {k: v * 10 for k, v in zip(keys, values)}
print(f"Constructed Dict: {new_dict}")

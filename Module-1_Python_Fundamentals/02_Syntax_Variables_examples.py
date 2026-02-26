# 02_Syntax_Variables_examples.py

"""
Step-by-step guide to Python Variables and Data Types.
This file demonstrates dynamic typing, naming conventions, and memory references.
"""

# 1. Variable Assignment & Dynamic Typing
# No need to declare types like 'int x = 10'
user_count = 1500           # Initially an integer
print(f"User Count: {user_count}, Type: {type(user_count)}")

user_count = "Fifteen Hundred" # Reassigned to a string
print(f"User Count: {user_count}, Type: {type(user_count)}")

# 2. Memory References (Expert Concept)
# Both variables point to the same object in memory initially
a = [1, 2, 3]
b = a
print(f"\n'a' id: {id(a)}")
print(f"'b' id: {id(b)}")
print(f"Are 'a' and 'b' the same object? {a is b}")

# 3. Comprehensive Data Types
pi_value = 3.14159           # float
complex_num = 3 + 5j         # complex
is_student = False           # bool
empty_val = None             # NoneType

print(f"\nComplex Number: {complex_num}, Real Part: {complex_num.real}")
print(f"The value is: {empty_val}, which is of type {type(empty_val)}")

# 4. Type Casting (Explicit Conversion)
age_str = "25"
age_int = int(age_str)       # Convert string to int
print(f"\nConversions: {age_int + 5}") # Works because it's now an int

# 5. Constants (Convention only)
MAX_LOGIN_ATTEMPTS = 5       # Written in ALL CAPS to signal it shouldn't be changed

# 6. Input/Output Deep Dive
name = input("\nEnter your name: ") or "Anonymous"
print(f"Hello, {name}!", sep=" | ", end=" -- Welcome aboard!\n")

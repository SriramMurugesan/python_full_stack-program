# 03_Operators_Control_examples.py

"""
Step-by-step guide to Python Operators and Control Flow.
Demonstrates short-circuiting, ternary operators, and the unique 'loop-else' pattern.
"""

# 1. Advanced Arithmetic & Bitwise
print("--- Advanced Operators ---")
a = 10
b = 3
print(f"Floor Division (10 // 3): {a // 3}")  # 3
print(f"Power (10 ** 3): {a ** 3}")             # 1000

# Bitwise (Binary level: 10 is 1010, 3 is 0011)
print(f"Bitwise AND (10 & 3): {a & 3}")        # 0010 -> 2
print(f"Bitwise OR  (10 | 3): {a | 3}")        # 1011 -> 11

# 2. Short-circuiting & Ternary Operator
print("\n--- Logic & Decision Making ---")
is_verified = True
has_permission = False

# Ternary Operator (One-liner if-else)
access_msg = "Access Granted" if is_verified or has_permission else "Access Denied"
print(f"Security Check: {access_msg}")

# 3. Loops and the 'Else' clause
print("\n--- Loops with Else ---")
numbers = [1, 2, 3, 4, 5]
target = 6

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    # This runs only if the loop finishes without a 'break'
    print(f"Target {target} was NOT found in the list.")

# 4. Enumerate and Zip (Professional Iteration)
print("\n--- Professional Iteration ---")
fruits = ["apple", "banana", "cherry"]

# Get index and value simultaneously
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit #{index}: {fruit}")

# Iterate over two lists together
prices = [50, 20, 100]
for fruit, price in zip(fruits, prices):
    print(f"{fruit.capitalize()} costs {price} coins.")

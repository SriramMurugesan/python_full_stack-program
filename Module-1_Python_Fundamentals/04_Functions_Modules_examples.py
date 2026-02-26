# 04_Functions_Modules_examples.py

"""
Step-by-step guide to Python Functions and Scope.
Demonstrates *args, **kwargs, lambda, and the LEGB scope rule.
"""

# 1. Advanced Argument Handling (*args and **kwargs)
def professional_greet(greeting, *names, **details):
    """
    Demonstrates flexible argument passing.
    *names collects positional arguments into a tuple.
    **details collects keyword arguments into a dictionary.
    """
    print(f"--- {greeting} ---")
    for name in names:
        print(f"Hello, {name}!")
    
    if 'location' in details:
        print(f"Welcome to {details['location']}!")

# Calling with various arguments
professional_greet("Morning", "Alice", "Bob", "Charlie", location="Python HQ", company="Google")

# 2. Variable Scope (LEGB Rule)
global_var = "I am Global"

def outer_function():
    enclosing_var = "I am Enclosing"
    
    def inner_function():
        local_var = "I am Local"
        print(f"\nInner sees: {local_var} | {enclosing_var} | {global_var}")
    
    inner_function()

outer_function()

# 3. Modifying Global State (Use with caution!)
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter incremented to: {counter}")

increment()

# 4. Lambda Functions (Anonymous)
# Standard way to write short logic
multiplier = lambda x, y: x * y
print(f"\nLambda Result (5 * 4): {multiplier(5, 4)}")

# 5. The __name__ == "__main__" Pattern
def main():
    print("\nMain function executed!")

if __name__ == "__main__":
    # This block only runs if you run this file directly
    main()

# 07_Exception_Handling_examples.py

"""
Step-by-step guide to Python Exception Handling.
Demonstrates specific exceptions, custom errors, and the 'else'/'finally' clauses.
"""

# 1. Custom Exception Definition
class AgeLimitError(Exception):
    """Raised when user age is below the requirement."""
    pass

# 2. The Complete try-except-else-finally Block
def register_user(age):
    try:
        print(f"\nAttempting to register user with age: {age}")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer sequence of digits.")
        if age < 18:
            raise AgeLimitError("You must be 18+ to register.")
    except TypeError as e:
        print(f"Type Error: {e}")
    except AgeLimitError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        # Catch-all for unexpected issues (use sparingly)
        print(f"Unexpected Error: {e}")
    else:
        # Runs ONLY if no exception was raised
        print("Success: User registered successfully!")
    finally:
        # Runs NO MATTER WHAT
        print("System: Registration attempt logged.")

# Testing the function
register_user(25)     # Success
register_user(16)     # Custom AgeLimitError
register_user("25")   # TypeError

# 3. Practical Resource Handling (Simulated)
print("\n--- Resource Cleanup Example ---")
try:
    print("Opening connection to 'Database'...")
    # Simulate a crash
    x = 1 / 0
except ZeroDivisionError:
    print("Caught a crash during database operation!")
finally:
    # This is critical! Ensures the connection closes even if we crash.
    print("Closing connection to 'Database' (Cleanup guaranteed).")

# Module 1: Python Master Practice Exercises

Mastery comes from solving problems. These exercises range from basic syntax to advanced OOP and file logic.

## 🟢 Level 1: Beginner (Syntax, Loops, Basics)
1. **The Dynamic Calculator:** Write a program that takes two inputs and an operator (`+`, `-`, `*`, `/`) and performs the calculation. Handle strings if the user enters "5" instead of 5.
2. **Even/Odd List:** Given a range (1 to 50), create a list containing only the even numbers using a `for` loop.
3. **Login logic:** Create a dictionary with 3 sets of usernames and passwords. Ask the user for input and verify if they exist in the dictionary.
4. **Multiplication Table:** Generate a multiplication table for a number provided by the user (up to 10).

## 🟡 Level 2: Intermediate (Data Structures, Functions, Strings)
5. **Word Counter:** Write a function that counts the frequency of each word in a given sentence and returns it as a dictionary.
6. **List Comprehension Magic:** Given a list of names, create a new list containing only names that start with "S" and convert them to uppercase using a single line of code.
7. **Set Theory:** Create two sets of student IDs for two different classes. Find:
   - Students in both classes.
   - Students only in the first class.
   - All unique students across both.
8. **Palindrome Checker:** Write a function that checks if a string is a palindrome (reads the same backward) using slicing.

## 🔴 Level 3: Advanced (Exceptions, Files, OOP)
9. **The Secure File Logger:** 
   - Ask the user for their name and a secret message.
   - Write this to a file named `secrets.txt` using the `with` statement.
   - Append a timestamp (search how to use the `datetime` module).
10. **Custom Error Handling:** Write a function `sqrt_robust(x)` that calculates the square root. Raise a `ValueError` with a custom message if `x` is negative.
11. **JSON Data Manager:** Create a script that reads a list of dictionaries from a `.json` file, updates one value, and saves it back.
12. **The OOP Payroll System:**
    - Create a base class `Employee` with `name` and `base_salary`.
    - Create a child class `Developer` that adds a `bonus` attribute.
    - Override a `calculate_pay()` method in both.
    - Use `@property` to keep the salary protected.

## 🏆 Graduation Challenge: The Mini Banking App
Create a class `Account` that:
1. Has a private `__balance`.
2. Has methods for `deposit(amount)` and `withdraw(amount)`.
3. Raises a custom `OverdraftError` if withdrawal exceeds balance.
4. Logs every transaction to a text file `statement.txt`.

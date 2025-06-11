# bad_script.py

import os

# Hardcoded credentials (Security Hotspot)
USERNAME = "admin"
PASSWORD = "123456"  # Hardcoded password - not secure

# Unused function (Code Smell)
def unused_function():
    print("This function is never used!")

# Repeated block of code (Duplication)
def compute_sum1():
    a = 10
    b = 20
    return a + b

def compute_sum2():
    a = 10
    b = 20
    return a + b

def login(username, password):
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Login failed.")
        return False

# Bug: return unreachable due to exception
def divide(a, b):
    try:
        result = a / b
        return result
        raise Exception("This line is unreachable!")  # Unreachable code
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

# Logic issue: variable shadowing + unused variable
def process_items(items):
    total = 0
    for item in items:
        total += item
        item = 999  # Shadowing (bad practice)
    unused_var = 123  # Dead code
    return total

if __name__ == "__main__":
    print("Welcome to Bad Script")
    login("admin", "123456")
    print("Result of divide:", divide(10, 0))
    print("Processed total:", process_items([1, 2, 3]))
    print("Sum1:", compute_sum1())
    print("Sum2:", compute_sum2())

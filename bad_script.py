def login(username, password):
    # SECURITY HOTSPOT: Hardcoded credentials
    if username == "admin" and password == "123456":
        return True
    return False

def calculate():
    # BUG: List index out of range
    numbers = [1, 2, 3]
    return numbers[5]

def bad_function():
    # CODE SMELL: Unused variable
    unused = 42
    
    # Deep nesting - readability issue
    if True:
        if True:
            if True:
                print("Deeply nested")

def duplicate_code():
    a = 10
    b = 20
    sum_ab = a + b
    print("Sum:", sum_ab)

def duplicate_code_copy():
    a = 10
    b = 20
    sum_ab = a + b
    print("Sum:", sum_ab)

def duplicate_code_copy2():
    a = 10
    b = 20
    sum_ab = a + b
    print("Sum:", sum_ab)

# ERROR: Syntax issue (missing closing parenthesis)
def broken_function(
    print("This won't work")

# Main script
if __name__ == "__main__":
    print("Welcome")
    is_logged_in = login("admin", "123456")
    print("Logged in:", is_logged_in)
    
    # INTENTIONAL BUG
    result = calculate()
    print("Calculation result:", result)

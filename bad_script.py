def login(username, password):
    if username == "admin" and password == "123456":
        return True
    return False

def login(username, password):  # 🔁 Duplicate function (code smell)
    if username == "admin" and password == "123456":
        return True
    return False

def calculate():
    a = 10
    b = 20
    sum_ab = a + b
    print("Sum:", sum_ab)

    # Hardcoded credentials (Security Hotspot)
    if a == 10:
        password = "admin123"  # ❗ Security issue

    if b > 10:
        print("B is greater than 10")

    for i in range(5):
        print("Looping:", i)

def unused_function():  # Dead code
    x = 100
    y = 200
    return x + y


if __name__ == "__main__":
    print("Welcome")
    is_logged_in = login("admin", "123456")
    print("Logged in:", is_logged_in)

    result = calculate()

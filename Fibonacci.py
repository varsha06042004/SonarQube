# Triggering SonarCloud analysis
# code is completed
def fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_num)
    return sequence

if __name__ == "__main__":
    try:
        num = int(input("Enter the number of Fibonacci terms: "))
        result = fibonacci(num)
        print("Fibonacci sequence:", result)
    except ValueError:
        print("Please enter a valid integer.")

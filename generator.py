def fibonacci_generator(n):
    """Generator function to generate Fibonacci numbers up to 'n'."""
    a, b = 0, 1  # Initialize the first two Fibonacci numbers

    while a <= n:
        yield a  # Yield the current Fibonacci number

        # Calculate the next Fibonacci number
        a, b = b, a + b


if __name__ == '__main__':
    fibonacci_sequence = fibonacci_generator(100)  # Generate Fibonacci numbers up to 100
    for num in fibonacci_sequence:
        print(num)  # Print each Fibonacci number

def fibonacci(n):
    """Return the nth Fibonacci number recursively."""
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

     

if __name__ == "__main__":
	print(fibonacci(0))  # Expected 0
	print(fibonacci(1))  # Expected 1
	print(fibonacci(5))  # Expected 5 (sequence: 0,1,1,2,3,5)
	print(fibonacci(7))  # Expected 13 (sequence: 0,1,1,2,3,5,8,13)
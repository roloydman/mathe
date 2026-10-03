def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(5))

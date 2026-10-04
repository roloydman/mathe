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


def power(base: float, exp: int) -> float:
    """Calculate base raised to exp using iterative multiplication."""
    if exp < 0:
        return 1 / power(base, -exp)
    result = 1
    for _ in range(exp):
        result *= base
    return result


def square_root(n: float) -> float:
    """Calculate square root of a non-negative number."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.5


if __name__ == "__main__":
    print(factorial(5))
    print(power(2, 3))
    print(square_root(9))

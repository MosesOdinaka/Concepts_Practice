def factorial(n):
    """
    Compute the factorial of a non-negative integer n.

    :param n: A non-negative integer.
    :return: The factorial of n
    """

    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def binomial_coefficient(n, k):
    """
    Compute the binomial coefficient C(n, k).

    :param n: The number of elements.
    :param k: The number of elements to choose.
    :return: The binomial coefficient C(n, k).
    """

    return factorial(n) // (factorial(k) * factorial(n - k))

# Example usage
n = 5
k = 2
print(f"C({n}, {k}) = {binomial_coefficient(n, k)}")

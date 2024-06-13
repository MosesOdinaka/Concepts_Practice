def binomial_coefficient_dp(n, k):
    """
    Compute the binomial coefficient C(n, k) using dynamic programming.

    :param n: The number of elements.
    :param k: The number of elements to choose.
    :return: The binomial coefficient C(n, k).
    """
    # Step 1: Initialize a 2D table with dimensions (n + 1) x (k + 1)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Step 2: Set base cases
    for i in range(n + 1):
        dp[i][0] = 1
        if i <= k:
            dp[i][i] = 1
    
    # Step 3: Fill the table using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, min(i, k + 1)):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    # Step 4: Return the result from dp[n][k]
    return dp[n][k]

# Example usage
n = 5
k = 2
print(f"C({n}, {k}) = {binomial_coefficient_dp(n, k)}")

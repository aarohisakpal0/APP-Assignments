# Assignment 4: Fibonacci using Dynamic Programming
# Techniques used:
# 1. Memoization (Top-Down)
# 2. Tabulation (Bottom-Up)

def fibonacci_memoization(n, memo=None):
    """Calculate nth Fibonacci number using memoization."""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = (fibonacci_memoization(n - 1, memo) +
               fibonacci_memoization(n - 2, memo))

    return memo[n]


def fibonacci_tabulation(n):
    """Calculate nth Fibonacci number using tabulation."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Take input from the user
n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    print("\nUsing Memoization:")
    print("The", n, "th Fibonacci number is:", fibonacci_memoization(n))

    print("\nUsing Tabulation:")
    print("The", n, "th Fibonacci number is:", fibonacci_tabulation(n))

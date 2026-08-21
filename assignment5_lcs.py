# Assignment 5: Longest Common Subsequence (LCS)
# Dynamic Programming

def lcs(sequence1, sequence2):
    m = len(sequence1)
    n = len(sequence2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    i = m
    j = n
    result = []

    while i > 0 and j > 0:
        if sequence1[i - 1] == sequence2[j - 1]:
            result.append(sequence1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()

    return ''.join(result), dp[m][n]


def main():
    print("=" * 55)
    print("       LONGEST COMMON SUBSEQUENCE (LCS)")
    print("          USING DYNAMIC PROGRAMMING")
    print("=" * 55)

    # Take two sequences as input
    sequence1 = input("\nEnter first sequence: ")
    sequence2 = input("Enter second sequence: ")

    # Calculate LCS
    subsequence, length = lcs(sequence1, sequence2)

    # Display result
    print("\n" + "=" * 55)
    print("                    RESULT")
    print("=" * 55)
    print("First Sequence  :", sequence1)
    print("Second Sequence :", sequence2)
    print("LCS             :", subsequence)
    print("Length of LCS   :", length)
    print("=" * 55)


if __name__ == "__main__":
    main()

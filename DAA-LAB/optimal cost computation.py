def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]

p = [30, 35, 15, 5, 10, 20, 25]

print("Optimal Cost =", matrix_chain_order(p))
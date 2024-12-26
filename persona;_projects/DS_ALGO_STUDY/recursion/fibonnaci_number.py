
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_with_dp(n, dp):
    if n == 0:
        dp[n] = 0
        return dp[n]
    if n == 1:
        dp[n] = 1
        return dp[n]
    dp[n] = fib_with_dp(n-1, dp) + fib_with_dp(n-2, dp)
    return dp[n]


dp = [-1]*11
print(fib_with_dp(10, dp))
print(dp)
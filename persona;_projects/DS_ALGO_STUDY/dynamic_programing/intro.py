"""
2 way to implement DP

1) recursion + memo --- top/down
2) tabulation --- bottom up

"""

"""
1) 1,1,2,3,5,8,13




"""

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# same imp can be done by dp

# first method, recursion + memo
def fib_dp(n, dp):
    if n <=1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib_dp(n-1, dp) + fib_dp(n-2, dp)
    print(dp)
    return dp[n]


# bottom up - tabulation


def fib_tab(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp)
    return dp[n]


# n = 2
# dp = [-1] * (n+1)
# print(fib_dp(n, dp))
# print(dp)
# print(fib(10))

print(fib_tab(10))

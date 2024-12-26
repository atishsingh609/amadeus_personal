

def fib(n, dp):

    if n == 0 or n==1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1, dp) + fib(n-2, dp)
    return dp[n]


n_1 = 8
dp_1 = [-1] * (n_1+1)
print(dp_1)

print(fib(n_1, dp_1))
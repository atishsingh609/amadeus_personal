"""
no of ways to reach bottom of a 2-d grid starting from top.
we can only move right or bottom
"""


def no_of_ways(m, n, memo={}):
    if (n, m) in memo:
        return memo[(n, m)]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n ==1:
        return 1
    memo[(n, m)] = no_of_ways(m-1, n) + no_of_ways(m, n-1)
    return memo[(n, m)]
    # return no_of_ways(m-1, n) + no_of_ways(m, n-1)

print(no_of_ways(200,300))
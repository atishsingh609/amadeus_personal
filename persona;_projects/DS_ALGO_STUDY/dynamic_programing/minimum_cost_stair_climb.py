"""
def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        ### we can say taht to reach nth step there is two option either we can come from n-1 ot n-1
        ## that depends on cost of n-1 and n-1. whatevent is minimum in them we can take it

        ###pattern -> dp[n] = cost[n] + min(dp[n-1] + dp[n-2])

        for i in range(2, n+1):
            dp[i] = cost[i] + min(dp[i-1] + dp[i-2])
        return min(dp[-1], dp[-2])


"""


def minCostClimbingStairs(cost) -> int:
    if not cost:
        return 0
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    ### we can say taht to reach nth step there is two option either we can come from n-1 ot n-1
    ## that depends on cost of n-1 and n-1. whatevent is minimum in them we can take it

    ###pattern -> dp[n] = cost[n] + min(dp[n-1] + dp[n-2])

    for i in range(2, n ):
        dp[i] = cost[i] + min(dp[i - 1] , dp[i - 2])
    return min(dp[-1], dp[-2])


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))



"""
top down approach 

dp



"""


def minCostClimbingStairs(self, cost) -> int:
    n = len(cost)
    dp = [-1] * n
    return min(self.solve(cost, n - 1, dp), self.solve(cost, n - 2, dp))


def solve(self, cost, n, dp):
    if n == 0:
        return cost[0]
    if n == 1:
        return cost[1]
    if dp[n] != -1:
        return dp[n]
    dp[n] = cost[n] + min(self.solve(cost, n - 2, dp), self.solve(cost, n - 1, dp))
    return dp[n]
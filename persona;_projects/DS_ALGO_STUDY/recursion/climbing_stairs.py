"""
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 ste


"""


class Solution:
    def __init__(self):
        self.dp = [0]*(46)
    def climbStairs(self, n: int) -> int:

        """
        there are two possiblity to finally come to nth stair.
        either you come from n-1 step or you can come for n-2 step.
        so, we get this relation f(n) = f(n-1) + f(n-2)

        for base case, for negative stairs -> return 0
        for zerostairs return -> 1
        for n <=3 -
        n = 0 -> 0
        n = 1 - > 1
        n = 2 -> 1+1, 2 => 2
        n = 3 - > 1+1+1, 2+1, 1+2 => 3
        """
        if n <= 3:
            self.dp[n] = n
            return self.dp[n]
        if self.dp[n] !=0:
            return self.dp[n]
        # for i in range(1, n+1):
        #     dp[n] = dp[n-1] + dp[n-2]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
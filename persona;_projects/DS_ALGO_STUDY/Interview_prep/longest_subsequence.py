class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[-1 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1) ]
        return self.longest_common(text1, text2, 0,0, dp)


    def longest_common(self, a,b, i, j, dp):

        if i == len(a) or j == len(b):
            return 0
        ans = 0
        if dp[i][j] !=-1:
            return dp[i][j]
        if a[i] == b[j]:
            ans = 1 + self.longest_common(a, b, i+1, j+1, dp)
        else:
            ans = max(self.longest_common(a, b, i+1, j, dp), self.longest_common(a, b, i, j+1, dp))
        dp[i][j] = ans
        return dp[i][j]

"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longest_common(text1, text2, 0,0)


    def longest_common(self, a,b, i, j):

        if i == len(a) or j == len(b):
            return 0
        ans = 0
        if a[i] == b[j]:
            ans = 1 + self.longest_common(a,b,i+1,j+1)
        else:
            ans = max(self.longest_common(a,b,i+1, j), self.longest_common(a,b,i, j+1))
        return ans


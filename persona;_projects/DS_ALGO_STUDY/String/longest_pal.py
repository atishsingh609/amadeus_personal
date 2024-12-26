"""
5. Longest Palindromic Substring
Medium
24.2K
1.4K
Companies
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

https://leetcode.com/problems/longest-palindromic-substring/submissions/



Used mirror image algo to determine if a substring is palindrome or not. There are two condition, whether the length
of string is odd or even. If it is even the mirror will be in between otherwise it will be at a character.

eg: bab --- mirror is a
bb - mirror will be between b and b.

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        currentLongPal = (0, 1)
        for i in range(1, len(s)):
            odd_pal = self.pal_around_center(s, i - 1, i + 1)
            even_pal = self.pal_around_center(s, i - 1, i)
            longestpal = max(odd_pal, even_pal, key=lambda x: x[1] - x[0])
            currentLongPal = max(longestpal, currentLongPal, key=lambda x: x[1] - x[0])
        return s[currentLongPal[0]: currentLongPal[1]]

    def pal_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        return [left + 1, right]
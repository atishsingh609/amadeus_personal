"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.



"""


def minWindow(s: str, t: str) -> str:
    start = 0
    end = 0
    cur_sub = ''
    ans = ''

    flag = True
    while end < len(s):
        cur_sub = cur_sub + s[end]
        if len(cur_sub) >= len(t):
            count = 0
            for ch in t:
                if ch in cur_sub:
                    count = count + 1
            if count == len(t):
                flag = True
            else:
                flag = False
            if flag:
                if len(ans) > 0:
                    if len(cur_sub) < len(ans):
                        ans = cur_sub
                else:
                    ans = cur_sub
                cur_sub = cur_sub[1:]
                start = start + 1
        end = end + 1
    return ans

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

""""
Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.
Your Task:
Complete the function search() which takes two strings pat, txt, as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(26) or O(256)

Constraints:
1 <= |pat| <= |txt| <= 105
Both string contains lowercase english letters




"""

"""
sliding window aproach



"""

def search(self, pat, txt):
    map = {}
    for p in pat:
        map[p] = map.get(p, 0) + 1
    i = 0
    j = 0
    k = len(pat)
    ans = 0
    cur = ''
    while j < len(txt):
        cur = txt[i:j + 1]
        if j - i + 1 < k:
            j = j + 1
        elif j - i + 1 == k:
            flag = True
            for s in cur:
                if s not in map:
                    flag = False
                    break
                if cur.count(s) != map.get(s, 0):
                    flag = False
                    break
            if flag:
                ans += 1
        # cur = cur.replace(txt[i], '', 1)
        i = i + 1
        j = j + 1
    return ans
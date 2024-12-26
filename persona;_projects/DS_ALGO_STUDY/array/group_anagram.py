"""
49. Group Anagrams
Medium
Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


"""


def groupAnagrams( strs: List[str]) -> List[List[str]]:
    anagram = {}
    for i in strs:
        temp_word = ''.join(sorted(i))
        if temp_word in anagram:
            anagram[temp_word].append(i)
        else:
            anagram[temp_word] = [i]
    return list(anagram.values())





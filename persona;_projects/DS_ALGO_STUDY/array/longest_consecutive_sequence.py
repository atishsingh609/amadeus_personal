"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


"""
def longestConsecutive(nums: List[int]) -> int:

        unique = set(nums)
        ans = 0

        while unique:
            high = low = unique.pop()
            while high + 1 in unique or low -1 in unique :
                if high + 1 in unique:
                    high = high + 1
                    unique.remove(high)
                if low -1 in unique:
                    low = low -1
                    unique.remove(low)
            ans = max(high - low + 1, ans)




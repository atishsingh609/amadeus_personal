""""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length


"""

"""
Solution: This problem is based on sliding window algo.

"""
def maxm_ones(nums, k):
    i = 0
    j = 0
    while j < len(nums):
        k -= 1-nums[j]
        if k < 0:
            k += 1-nums[i]
            i = i + 1
        j = j + 1
    return j-i

print(maxm_ones([1,1,1,0,0,0,1,1,1,0,0,0], 2))



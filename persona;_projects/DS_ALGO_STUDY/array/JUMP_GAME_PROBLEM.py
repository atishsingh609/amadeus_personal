"""
ADOBE, Intuit
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000

Algo ::
a = array[0]
b = array[0]
a and b will decrease.
value of b varies based on the comp with the current number. If current number is greater than b the value of b will be
updated. The value of b will be decreased by one in every iter.
when a will be zero, the value of b will be assign to a
"""


def minimum_no_of_jump(arr):
    a = arr[0]
    b = arr[0]
    jump = 1
    for i in range(1, len(arr)):
        if i == len(arr) -1:
            return jump
        a -= 1
        b -= 1
        b = max(arr[i], b)
        if a == 0:
            jump = jump + 1
            a = b

    return jump


# nums = [2,3,0,1,4]
array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minimum_no_of_jump(array))


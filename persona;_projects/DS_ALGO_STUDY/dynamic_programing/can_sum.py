"""
canSum(7, [5,2,4,3,7,8]) --true
"""

def canSum(target, nums, memo ={}):
    if target in memo:
        return memo[target]
    if target == 0 :
        return True
    if target < 0:
        return False
    for num in nums:
        current_target = target - num
        if canSum(current_target, nums, memo):
            memo[target] = current_target
            return True

    memo[target] = False
    return False

print(canSum(1000, [2, 2]))
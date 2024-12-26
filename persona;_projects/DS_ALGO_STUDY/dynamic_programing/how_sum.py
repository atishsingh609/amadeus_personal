""""
howSum(7, [5, 4, 3, 7]---> [4, 3] ---just one solution return
"""

def howSum(target, nums, memo= {}):

    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return

    for num in nums:
        cur_target = target - num
        ans = howSum(cur_target, nums)

        if ans is not None:
            ans.append(num)
            memo[target] = ans
            return memo[target]
    memo[target] = None
    return memo[target]
print(howSum(777, [ 7]))
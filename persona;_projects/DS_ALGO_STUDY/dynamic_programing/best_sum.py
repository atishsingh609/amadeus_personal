""""
bestSum[target, [numbers])

function should return shorted combination of numbers taht adds up to target.
"""

def bestSum(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return
    shortest = None
    for num in nums:
        rest = target - num
        ans_rest = bestSum(rest, nums)
        if ans_rest is not None:
            cur_ans = ans_rest[:]
            cur_ans.append(num)
            if shortest is None:
                shortest = cur_ans
            elif len(cur_ans) <= len(shortest):
                shortest = cur_ans
        memo[target] = shortest
    return memo[target]

print(bestSum(300, [1, 2, 3, 4, 5]))


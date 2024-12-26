def funDistance(inputDist, start, end):
    ans = []
    for dist in inputDist:
        if start < dist < end:
            ans.append(dist)
    if ans:
        return ans
    else:
        return [-1]

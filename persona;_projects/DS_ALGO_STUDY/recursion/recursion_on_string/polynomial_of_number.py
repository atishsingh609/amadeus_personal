def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    ans = power(a, b/2)
    if b % 2 == 0:
        # b is even
        return ans * ans
    else:
        # b is odd the power
        return a * ans * ans


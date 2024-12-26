"""
Amazon, PayTM, VmWare,

Array of length n, having int 1 to n with some element being repeated. count frequency of all element.
Time complexity - O(n)
Space complexity O(1) - No extra space
"""
a = [1, 2, 3, 1, 2, 3, 1, 5, 4, 6, 5]

def count_freq(a):
    result = {}
    for i in a:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
"""
Amazon, mmt, morgen
Given a number n, find the smallest number that has same set of digits as n and is greater than n. If n is the greatest
possible number with its set of digits, then print “not possible”.

Examples:
For simplicity of implementation, we have considered input number as a string.

Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"

"""


def next_greater_number(arr):
    n = len(arr)
    i = 0
    for i in range(n-1, 0, -1):
        if arr[i] > arr[i-1]:
            break
    if i == 1 and arr[i] < arr[i-1]:
        return "Next greater number not possible"
    element = arr[i-1]
    smallest = i
    for j in range(i+1, n):
        if element < arr[j] < arr[smallest]:
            smallest = j
    arr[smallest], arr[i-1] = arr[i-1], arr[smallest]
    arr = arr[:i] + sorted(arr[i:])
    return arr


# array = [2, 1, 8, 7, 6, 5]
array = [5, 3, 4, 9, 7, 6]
print(next_greater_number(array))
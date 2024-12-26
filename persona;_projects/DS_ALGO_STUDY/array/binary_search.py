"""
1) If array is sorted
2)If Array is increasing and decreasing
3)Sorted Array is rotated, and then given as i/p
4)Array is given as zigzaw format

We can implement binary search

time complexity- O(Logn)


"----------ALGO----------"
find the middle term then compare with the term we are searching for. If it lies left then consider that part otherwise
consider the right part.
"""

# without recursion

# low = 0
# high = len(a) -1
# while low <= high:
#     mid = (low + high)//2
#     if a[mid] == n:
#         print(mid)
#         break
#     elif a[mid] < n:
#         low = mid + 1
#     elif a[mid] > n:
#         high = mid - 1
#     else:
#         print("Not present")
#         break

# using recursion

def binary_search(arr, target, low, high):
    """
    O(Log n)
    :param arr:
    :param target:
    :param low:
    :param high:
    :return:
    """
    mid = (low + high)//2
    if low > high:
        return "Not Found"
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 10

print(binary_search(a, n, 0, 7))



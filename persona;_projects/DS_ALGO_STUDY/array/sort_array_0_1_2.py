"""
AMAZON, ADOBE, WALMART
sort the array in-place,
time complexity - O(n)
space complexity - O(1)

array = [1,1,1,0,1,2,1,2,0,0,0,2]

algo :
low = 0
mid = 0
high = len(array)
if array[mid] = 2, swap(array[mid], array[high]) & high --
if array[mid] = 0, swap(array[low], array[mid]) low ++, mid ++
if array[mid] = 1, no swap, mid++
"""


def sort_array(a):
    low = 0
    high = len(a) - 1
    mid = 0
    while mid <= high:
        if a[mid] == 2:
            a[mid] = a[high]
            a[high] = 2
            high = high - 1
        elif a[mid] == 0:
            a[mid] = a[low]
            a[low] = 0
            mid = mid + 1
            low = low + 1
        else:
            mid = mid + 1
    return a


array = [1, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 2]
print(sort_array(array))




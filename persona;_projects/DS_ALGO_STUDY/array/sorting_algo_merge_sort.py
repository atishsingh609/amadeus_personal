"""
1) Merge sort : divide and concur
array = [8,10,4,12,16,5,6,13]

Algo :: Whole array will be divided into sub arrays using mid point until every subarray has only one element.
Need to  use recursion
First divided the array then merge it(one by one).
"""


def merge(a, result, low, mid, high):
    i = k = low
    j = mid + 1
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            result[k] = a[i]
            k += 1
            i += 1
        else:
            result[k] = a[j]
            k += 1
            j += 1
    while i <= mid:
        result[k] = a[i]
        i += 1
        k += 1

    while j <= high:
        result[k] = a[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        a[i] = result[i]


def mergesort(arr, result, low, high):
    if low == high:
        return
    mid = int((low + high)/2)
    mergesort(arr, result, low, mid)
    mergesort(arr, result, mid+1, high)
    merge(arr, result, low, mid, high)
    # print(a)


a = [8, 4, 10, 13, 5, 7, 2, 1]
low = 0
high = 7
result = [0, 0, 0, 0, 0, 0, 0, 0]
mergesort(a, result, low, high)
print(a)





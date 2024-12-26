"""
a = [6,9,15,25,35,50,41,29,23,8]
find maximum number

we can use binary search algo here.(for array only increasing, only decreasing, and for increasing and decreasing)
we can use this algo for array first decreasing and then increasing

"""

def find_max(arr, low, high):
    if low == high: # to handle only one element in array
        return arr[low]
    if high == low + 1: # to handle two elements in array
        return arr[high] if arr[high] > arr[low] else arr[low]
    mid = int((low+high)/2)
    if arr[mid-1] < arr[mid] > arr[mid+1]:
        return arr[mid]
    elif arr[mid-1] < arr[mid] < arr[mid+1]:
        return find_max(arr, mid+1, high)
    else:
        return find_max(arr, low, mid-1)


a = [6, 9, 15, 25, 35, 50, 41, 29, 23, 8]
# a = [20,10]
print(find_max(a, 0, 10))




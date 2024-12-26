i = 0
def is_sorted(arr, size):

    if size == 0 or size == 1:
        return True
    if arr[0] > arr[1]:
        return False
    else:
        print(arr)
        ans = is_sorted(arr[1:], size-1)
        return ans


a = [1,2,3,4,5,6]
size = 6
print(is_sorted(a, size))
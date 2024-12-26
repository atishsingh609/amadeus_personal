
def linear_search(arr, b):
    if len(arr) == 0:
        return False
    if arr[0] == b:
        return True
    else:
        ans = linear_search(arr[1:], b)
        return ans


a = [1,2,3,4,5,6]
b = 8
print(linear_search(a, b))
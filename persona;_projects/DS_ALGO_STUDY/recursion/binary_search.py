def binary_search(arr, start, end, n):
    mid = int((start + end) / 2)
    if start > end:
        return -1
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return binary_search(arr, start, mid - 1, n)
    elif arr[mid] < n:
        return binary_search(arr, mid + 1, end, n)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(a, 0, len(a), 7))


def binary_search_new(arr, l, r, n):
    if l > r:
        return -1
    mid = int((l + r) / 2)
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return binary_search(arr, l, mid - 1, n)
    elif arr[mid] < n:
        return binary_search(arr, mid + 1, r, n)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search_new(a, 0, len(a), 7))

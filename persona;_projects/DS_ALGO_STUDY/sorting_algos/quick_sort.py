def quick_sort(arr, s, e):
    if s >= e:
        return
    # step first, partition the array
    p = partition(arr, s, e)
    # now recursion call, before and after partition
    quick_sort(arr, s, p - 1)
    quick_sort(arr, p + 1, e)


def partition(arr, s, e):
    pivot = arr[s]
    # count the number whic is less than pivot after pivot
    count = 0
    for i in range(s, e):
        if arr[i] < pivot:
            count = count + 1
    # now place the pivot element to it's right place by swaping
    pivot_index = s + count
    arr[s + count], arr[s] = arr[s], arr[s + count]

    # now place all smaller elements left of pivot and larger elememnt right of pivot
    i = s
    j = e-1
    while i < pivot_index and j > pivot_index:
        while arr[i] <= pivot:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if i < pivot_index and j > pivot_index:
            arr[i], arr[j] = arr[j], arr[i]
            # i = i + 1
            # j = j - 1
    return pivot_index

a = [5,1,1,2,0,0]
quick_sort(a, 0, len(a))
print(a)

def merge_sort(arr, s, e):
    if s >= e:
        return
    mid = int((s + e) / 2)
    merge_sort(arr, s, mid)
    merge_sort(arr, mid+1, e)
    merge(arr, s, e)


def merge(arr, s, e):
    mid = int((s+e)/2)
    first = arr[s:mid+1]
    second = arr[mid+1:e+1]
    print(first, " compare  ", second)
    index_1 = 0
    index_2 = 0
    main_array = s
    while(index_1 < len(first)) and (index_2 < len(second)):
        if first[index_1] < second[index_2]:
            arr[main_array] = first[index_1]
            main_array = main_array + 1
            index_1 = index_1 + 1

        else:
            arr[main_array] = second[index_2]
            main_array = main_array + 1
            index_2 = index_2 + 1

    while index_1 < len(first):

        arr[main_array] = first[index_1]
        main_array = main_array + 1
        index_1 = index_1 + 1

    while index_2 < len(second):
        arr[main_array] = second[index_2]
        main_array = main_array + 1
        index_2 = index_2 + 1
    print(arr)


a = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
print(merge_sort(a, 0, len(a)))
print(a)
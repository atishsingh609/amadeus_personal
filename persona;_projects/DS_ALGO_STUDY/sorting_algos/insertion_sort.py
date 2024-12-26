def insertion_sort(lst):
    """


    """
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j >= 0:
            if lst[j] > temp:
                lst[j+1] = lst[j]
            else:
                break
            j = j -1
        lst[j+1] = temp
    return lst


a = [19, 24, 16, 70, 5, 2, 4]
print(insertion_sort(a))



def insertion_sort_pr(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0:
            if arr[j] > arr[j+1]:
                arr[j+1] = arr[j]
            else:
                break
            j = j - 1
        arr[j+1] = temp

    return arr


print(insertion_sort_pr([10,30,20,50,40]))








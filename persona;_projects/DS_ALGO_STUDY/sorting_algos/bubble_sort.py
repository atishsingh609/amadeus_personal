
def bubble_sort(lst):
    """
    compare adjesent element and if current is greater than next then swap current with next.
    at end of each inner iteration, largest element will go in last.
    :param lst:
    :return:
    """
    for i in range(1, len(lst)):
        swapped = False
        for j in range(len(lst)- i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

    # for i in range(1, len(lst) -1):
    #     swapped = False
    #     for j in range(len(lst) - i):
    #         if lst[j] > lst[j+1]:
    #             lst[j], lst[j+1] = lst[j+1], lst[j]
    #             swapped = True
    #     if not swapped:
    #         break
    # return lst


















def bubble_sort_practice(arr):

    for i in range(1, len(arr)):
        swapped = False
        for j in range(len(arr) - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort_practice([20,22,25,8,72,45]))



#
#
#
#
#
#
# a = [10, 25, 6, 4, 29]
# print(bubble_sort(a))
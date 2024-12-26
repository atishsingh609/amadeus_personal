def selection_sort(lst):
    """
    select one element and serach for min value in rest of array and then swap it.
    space - o(1)
    time_complexity - o(n**2)

    :param lst:
    :return:
    """
    for i in range(len(lst) -1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
        print("current i:", a[i])
        print("current lst:", lst)
    return lst
a = [2,7,1,5,3,8,4, 10, 15, 9, 6, 4]
print(selection_sort(a))
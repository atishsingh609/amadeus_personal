def countOfElement(listInput1, listInput2):

    lowest = min(sorted(listInput1)[0], sorted(listInput2)[0])

    highest = max(sorted(listInput1)[-1], sorted(listInput2)[-1])

    count = 0
    for i in range(lowest, highest+1):
        if i in listInput1 and i not in listInput2:
            count = count + 1
        if i in listInput2 and i not in listInput1:
            count = count + 1
    return count

print(countOfElement([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,11,12,13,14,15,16,17,18]))

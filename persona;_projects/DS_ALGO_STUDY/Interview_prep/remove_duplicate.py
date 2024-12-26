def removeDuplicates(self, a: List[int]) -> int:
    i = 0

    for j in range(1, len(a)):
        if a[i] != a[j]:
            i = i + 1
            a[i] = a[j]
    return i + 1
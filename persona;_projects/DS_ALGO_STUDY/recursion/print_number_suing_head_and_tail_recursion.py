def print_number_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_number_1(n-1)


def print_number_2(n):
    if n == 0:
        return
    print_number_2(n - 1)
    print(n, end= " ")

print_number_1(10)
print("\n")
print_number_2(10)


nums = [[1, 2], [2, 4], [5, 3]]
nums.sort(key=lambda x: x[-1])
print(nums)
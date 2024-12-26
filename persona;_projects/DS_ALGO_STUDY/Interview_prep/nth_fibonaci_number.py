def fibonaci_number(n):

    if n == 0:
        return 0
    if n ==1:
        return 1
    a, b = 0, 1
    for i in range(n-1):
        a,b = b, a+b
    return b
    # return fibonaci_number(n-1) + fibonaci_number(n-2)

print(fibonaci_number(10))
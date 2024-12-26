"""
Function will be excuted in the backtracking mode.

"""


# def func_1(sum):
#     if sum == 5:
#         return
#     func_1(sum +1)
#     print(sum)

# print(func_1(1))

def fact(n):
    """
    Every time a function will be called it will return the value to previous call.
    for n =4 :
    4*fact(4-1) ----> 3*fact(3-1) -----> 2*fact(2-1) ----> 1
    4*3*2*1 --------> 3*2*1 -------------> 2*1-----------> 1
    :param n:
    :return:
    """
    if n ==1:
        return 1
    else:
        return n*fact(n-1)

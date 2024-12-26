""""
1) difference between list and tuple:


mutable and immutable

list slow
typle is fast

list is store in 2 block of memory.
"""

"""
lambda function
"""

func = lambda x, y: x + y
return_value = lambda input_1, input_2: input_1 + input_2

"""
use of lambda in map, filter

"""


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# get all even
print(list(filter(lambda i: i % 2 == 0, a)))


print(list(map(lambda i: i*i, a)))



a = list(map(lambda x: x**2, [i for i in range(21)]))
print(a)

"""
decorator 
"""


def decorator(fun):
    def wrapper(*args):
        print("calling decorator")
        abc = fun(*args)
        abc = abc +1
        return abc
    return wrapper


@decorator
def abcd(a,b,c,d):
    return a+b+c+d

print(abcd(1,2,3,4))

"""
generators
"""

def gen(n):
    for i in range(n):
        yield n


g = gen(150)
for i in range(10):
    print(g.next())


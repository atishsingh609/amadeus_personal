def decorator(func):
    def wrapper(a,b):
        a = a *a
        b = b * b
        return func(a,b)
    return wrapper

@decorator
def multiply_func(a,b):
    return a*b

print(multiply_func(2,3))

class Decorator:
    def __init__(self,func):
        self.func = func
        super().__init__()
        
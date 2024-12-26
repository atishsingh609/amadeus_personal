
class C:
    def __init__(self):
        self.abc = None
    @classmethod
    def fun(cls, arg1, arg2):
        print(arg1, " ", arg2,)

    @staticmethod
    def fun2():
        print("abc")


print(C.fun("pankhuri", "Muk"))
obj = C()
print(obj.fun("Atish", "K"))

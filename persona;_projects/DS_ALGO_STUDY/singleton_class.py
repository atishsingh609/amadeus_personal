class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, value):
        self.value = value

s1 = Singleton(20)
s2 = Singleton(10)
print(s1.value, s2.value)


